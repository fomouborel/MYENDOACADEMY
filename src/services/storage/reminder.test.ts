import { describe, expect, it } from 'vitest';
import { needsBackupReminder } from './reminder';

describe('rappel de sauvegarde', () => {
  const now = new Date('2026-05-30T10:00:00Z');
  it('pas de rappel au tout début', () => expect(needsBackupReminder(5, undefined, now)).toBe(false));
  it('rappel si jamais exporté après 20 réponses', () => expect(needsBackupReminder(25, undefined, now)).toBe(true));
  it('rappel si la dernière sauvegarde a plus de 14 jours', () => {
    expect(needsBackupReminder(100, '2026-05-01T10:00:00Z', now)).toBe(true);
    expect(needsBackupReminder(100, '2026-05-25T10:00:00Z', now)).toBe(false);
  });
});
