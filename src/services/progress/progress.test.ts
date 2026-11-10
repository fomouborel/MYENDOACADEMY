import { describe, expect, it } from 'vitest';
import type { Attempt, SessionRecord } from '@/schemas/progress';
import { mcq } from '@/test/fixtures';
import { dueDate, nextBox } from './srs';
import { applyAttempt, emptyState, isMastered, rebuildState, statusOf } from './questionState';
import { coverage } from './coverage';
import { chapterMastery } from './chapterMastery';

const att = (at: string, correct: boolean | null, hintsUsed = 0, questionId = 'Q'): Attempt => ({
  id: `${questionId}-${at}`, questionId, at, mode: 'training', selected: [], correct, hintsUsed, durationMs: 1000,
});

describe('révision espacée (Leitner)', () => {
  it('monte sans indice, stagne avec indice, retombe en cas d’erreur', () => {
    expect(nextBox({ box: 2, correct: true, hintsUsed: 0 })).toBe(3);
    expect(nextBox({ box: 2, correct: true, hintsUsed: 1 })).toBe(2);
    expect(nextBox({ box: 4, correct: false, hintsUsed: 0 })).toBe(1);
    expect(nextBox({ box: 5, correct: true, hintsUsed: 0 })).toBe(5);
  });
  it('les questions échouées reviennent plus vite que les maîtrisées', () => {
    const now = new Date('2026-01-01T10:00:00Z');
    expect(dueDate(1, now).getTime()).toBeLessThan(dueDate(5, now).getTime());
  });
});

describe('statut d’une question', () => {
  const now = new Date('2026-03-01T12:00:00Z');
  it('non commencée tant qu’aucune réponse n’est validée', () => {
    expect(statusOf(undefined, now)).toBe('not-started');
    expect(statusOf(emptyState('Q'), now)).toBe('not-started');
  });
  it('réussie puis échouée selon la dernière tentative', () => {
    const s1 = applyAttempt(emptyState('Q'), att('2026-03-01T09:00:00Z', true));
    expect(statusOf(s1, now)).toBe('success');
    const s2 = applyAttempt(s1, att('2026-03-01T09:05:00Z', false));
    expect(statusOf(s2, now)).toBe('failed');
  });
  it('une seule bonne réponse ne donne jamais la maîtrise', () => {
    const s = applyAttempt(emptyState('Q'), att('2026-03-01T09:00:00Z', true));
    expect(isMastered(s)).toBe(false);
  });
  it('maîtrise : réussites répétées sur plusieurs jours', () => {
    const s = rebuildState('Q', [
      att('2026-01-01T09:00:00Z', true),
      att('2026-01-02T09:00:00Z', true),
      att('2026-01-05T09:00:00Z', true),
      att('2026-01-12T09:00:00Z', true),
    ]);
    expect(isMastered(s)).toBe(true);
    expect(statusOf(s, new Date('2026-01-13T09:00:00Z'))).toBe('mastered');
    // à l'échéance de révision, la question repasse « à revoir » sans disparaître
    expect(statusOf(s, new Date('2026-03-01T09:00:00Z'))).toBe('to-review');
  });
  it('marquée à revoir par l’étudiante, brouillon = en cours', () => {
    const s = applyAttempt(emptyState('Q'), att('2026-03-01T09:00:00Z', true));
    expect(statusOf({ ...s, flagged: true }, now)).toBe('to-review');
    expect(statusOf({ ...emptyState('Q'), draft: true }, now)).toBe('in-progress');
  });
  it('les indices empêchent la progression de boîte', () => {
    const s = rebuildState('Q', [att('2026-01-01T09:00:00Z', true, 2), att('2026-01-03T09:00:00Z', true, 1), att('2026-01-06T09:00:00Z', true, 3)]);
    expect(s.box).toBe(1);
    expect(isMastered(s)).toBe(false);
  });
});

describe('couverture des archives', () => {
  it('compte uniquement les tentatives, pas les affichages', () => {
    const qs = [mcq({ id: 'ENDO-2024-01-ADULTE-QCM-001' }), mcq({ id: 'ENDO-2024-01-ADULTE-QCM-002' }), mcq({ id: 'ENDO-2024-01-ADULTE-QCM-003', answerStatus: 'absent', expected: [] })];
    const states = new Map([['ENDO-2024-01-ADULTE-QCM-001', applyAttempt(emptyState('ENDO-2024-01-ADULTE-QCM-001'), att('2026-03-01T09:00:00Z', false, 0, 'ENDO-2024-01-ADULTE-QCM-001'))]]);
    const c = coverage(qs, states, new Date('2026-03-01T12:00:00Z'));
    expect(c).toMatchObject({ available: 2, consultOnly: 1, worked: 1, failed: 1, remaining: 1, succeeded: 0 });
  });
});

describe('maîtrise d’un chapitre', () => {
  it('exige des questions maîtrisées ET deux évaluations finales réussies à des jours différents', () => {
    const q = mcq({ id: 'ENDO-2024-01-ADULTE-QCM-001' });
    const s = rebuildState(q.id, ['2026-01-01', '2026-01-02', '2026-01-05', '2026-01-12'].map((d) => att(`${d}T09:00:00Z`, true, 0, q.id)));
    const states = new Map([[q.id, s]]);
    const ev = (d: string, score: number): SessionRecord => ({ id: d, mode: 'final-eval', chapterId: 'thyroide', questionIds: [q.id], answers: {}, startedAt: `${d}T08:00:00Z`, finishedAt: `${d}T09:00:00Z`, timeLimitMinutes: null, score });
    expect(chapterMastery('thyroide', [q], states, [ev('2026-01-12', 0.9)]).level).toBe('solid');
    expect(chapterMastery('thyroide', [q], states, [ev('2026-01-12', 0.9), ev('2026-01-12', 0.8)]).level).toBe('solid');
    expect(chapterMastery('thyroide', [q], states, [ev('2026-01-12', 0.9), ev('2026-01-20', 0.8)]).level).toBe('mastered');
    expect(chapterMastery('thyroide', [q], new Map(), []).level).toBe('not-started');
  });
});
