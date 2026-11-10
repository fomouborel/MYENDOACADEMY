import { beforeEach, describe, expect, it } from 'vitest';
import type { Attempt } from '@/schemas/progress';
import { DB_NAME, getAttempts, getStates, recordAttempt, resetDbConnection, setFlag } from './db';
import { BackupError, exportBackup, importBackup, parseBackup } from './backup';

const att = (id: string, questionId: string, at: string, correct: boolean): Attempt => ({ id, questionId, at, mode: 'training', selected: ['A'], correct, hintsUsed: 0, durationMs: 500 });

beforeEach(async () => {
  await resetDbConnection();
  await new Promise<void>((res) => {
    const r = indexedDB.deleteDatabase(DB_NAME);
    r.onsuccess = () => res();
    r.onerror = () => res();
  });
});

describe('sauvegarde automatique (IndexedDB)', () => {
  it('enregistre la tentative et met à jour l’état', async () => {
    await recordAttempt(att('1', 'Q1', '2026-01-01T10:00:00Z', true));
    await recordAttempt(att('2', 'Q1', '2026-01-02T10:00:00Z', false));
    const s = (await getStates()).get('Q1');
    expect(s).toMatchObject({ attempts: 2, successes: 1, failures: 1, lastCorrect: false, box: 1 });
    expect(await getAttempts('Q1')).toHaveLength(2);
  });
  it('persiste après « rechargement » (nouvelle connexion)', async () => {
    await recordAttempt(att('1', 'Q1', '2026-01-01T10:00:00Z', true));
    await resetDbConnection();
    expect((await getStates()).get('Q1')?.successes).toBe(1);
  });
});

describe('export / import JSON', () => {
  it('aller-retour complet (remplacement)', async () => {
    await recordAttempt(att('1', 'Q1', '2026-01-01T10:00:00Z', true));
    await setFlag('Q2', true);
    const backup = parseBackup(JSON.stringify(await exportBackup()));
    await recordAttempt(att('9', 'Q9', '2026-01-03T10:00:00Z', true));
    const rep = await importBackup(backup, 'replace');
    expect(rep.attemptsAdded).toBe(1);
    const states = await getStates();
    expect(states.has('Q9')).toBe(false);
    expect(states.get('Q1')?.successes).toBe(1);
    expect(states.get('Q2')?.flagged).toBe(true);
  });
  it('fusion sans doublon ni perte', async () => {
    await recordAttempt(att('1', 'Q1', '2026-01-01T10:00:00Z', true));
    const backup = await exportBackup();
    backup.data.attempts.push(att('2', 'Q1', '2026-01-04T10:00:00Z', false));
    await importBackup(backup, 'merge');
    expect(await getAttempts('Q1')).toHaveLength(2);
    expect((await getStates()).get('Q1')).toMatchObject({ attempts: 2, lastCorrect: false });
  });
  it('refuse un fichier invalide avec un message clair', () => {
    expect(() => parseBackup('pas du json')).toThrow(BackupError);
    expect(() => parseBackup('{"app":"autre"}')).toThrow(/ENDOCRINO ACADEMY/);
  });
});
