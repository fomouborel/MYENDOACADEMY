import { describe, expect, it } from 'vitest';
import type { Attempt } from '@/schemas/progress';
import { mcq } from '@/test/fixtures';
import { rebuildState } from '@/services/progress/questionState';
import { errorNotebook, recentActivity, reviewSets, upcomingReviews } from './notebook';
import { buildFinalEval, buildMockExam, formatClock, remainingMs } from '@/features/exams/mockExam';

const A = 'ENDO-2024-01-ADULTE-QCM-001';
const B = 'ENDO-2024-01-ADULTE-QCM-002';
const qs = [mcq({ id: A }), mcq({ id: B, chapter: 'hyper', subchapter: 'diagnostic' })];
const att = (id: string, q: string, at: string, correct: boolean): Attempt => ({ id, questionId: q, at, mode: 'training', selected: ['A'], correct, hintsUsed: 0, durationMs: 1 });
const attempts = [att('1', A, '2026-03-01T09:00:00Z', false), att('2', A, '2026-03-02T09:00:00Z', false), att('3', B, '2026-03-02T10:00:00Z', true)];
const states = new Map([A, B].map((id) => [id, rebuildState(id, attempts)]));
const now = new Date('2026-03-03T12:00:00Z');

describe('carnet d’erreurs', () => {
  it('conserve chaque erreur avec réponse donnée, nombre d’échecs et de tentatives', () => {
    const nb = errorNotebook(qs, attempts, states, now);
    expect(nb).toHaveLength(1);
    expect(nb[0]).toMatchObject({ failures: 2, attempts: 2, resolved: false });
    expect(nb[0].lastWrong.selected).toEqual(['A']);
  });
});

describe('sessions de révision', () => {
  it('erreurs récentes, récurrentes, à revoir et non maîtrisées', () => {
    const sets = Object.fromEntries(reviewSets(qs, attempts, states, now, {}).map((s) => [s.kind, s.ids]));
    expect(sets['recent-errors']).toEqual([A]);
    expect(sets['recurrent-errors']).toEqual([A]);
    expect(sets['due']).toContain(A); // échouée : revient dès le lendemain
    expect(sets['not-mastered']).toEqual(expect.arrayContaining([A, B]));
  });
  it('les questions échouées passent avant les réussies', () => {
    const notMastered = reviewSets(qs, attempts, states, now, {}).find((s) => s.kind === 'not-mastered')!.ids;
    expect(notMastered[0]).toBe(A);
  });
  it('prochaines révisions et activité', () => {
    expect(upcomingReviews(states, new Date('2026-03-02T12:00:00Z')).length).toBeGreaterThan(0);
    expect(recentActivity(attempts, now, 3).map((d) => d.count)).toEqual([1, 2, 0]);
  });
});

describe('examens blancs et évaluation finale', () => {
  it('une session garde l’ordre d’origine ; un mix est limité au nombre demandé', () => {
    const s = buildMockExam(qs, { source: 'session', session: '2024-01', count: 10, minutes: 30, seed: 1 });
    expect(s.map((q) => q.id)).toEqual([A, B]);
    expect(buildMockExam(qs, { source: 'mix', chapters: ['hyper'], count: 1, minutes: 10, seed: 3 })).toHaveLength(1);
  });
  it('chronomètre', () => {
    expect(remainingMs('2026-03-03T12:00:00Z', 10, new Date('2026-03-03T12:09:00Z').getTime())).toBe(60_000);
    expect(remainingMs('2026-03-03T12:00:00Z', null, 0)).toBeNull();
    expect(formatClock(61_000)).toBe('01:01');
  });
  it('évaluation finale : questions du chapitre seulement, sans les étapes de cas cliniques', () => {
    const e = buildFinalEval([...qs, mcq({ id: 'ENDO-2024-01-ADULTE-QCM-003', caseId: 'c1', caseStep: 1 })], 'thyroide', 5);
    expect(e.map((q) => q.id)).toEqual([A]);
  });
});
