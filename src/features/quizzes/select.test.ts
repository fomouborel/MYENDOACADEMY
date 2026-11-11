import { describe, expect, it } from 'vitest';
import { mcq } from '@/test/fixtures';
import { applyAttempt, emptyState } from '@/services/progress/questionState';
import { hintsAllowed, selectQuestions, shuffle } from './select';

const now = new Date('2026-03-01T12:00:00Z');
const a1 = mcq({ id: 'ENDO-2024-01-ADULTE-QCM-001', difficulty: 2 });
const a2 = mcq({ id: 'ENDO-2024-01-ADULTE-QCM-002', difficulty: 3, chapter: 'hyper', subchapter: 'diagnostic' });
const ex = { ...mcq(), id: 'ENDO-EX-thyroide-VF-001', kind: 'exercise', provenance: undefined, format: 'true-false', options: [], instruction: undefined, expected: ['VRAI'], answerStatus: 'authored', difficulty: 1 } as never;
const absent = mcq({ id: 'ENDO-2024-01-ADULTE-QCM-003', answerStatus: 'absent', expected: [] });
const all = [a1, a2, ex, absent];

describe('sélection des questions', () => {
  it('exclut toujours les questions non jouables', () => {
    expect(selectQuestions(all, { mode: 'free' }, new Map(), now).map((q) => q.id)).not.toContain(absent.id);
  });
  it('vérifier = difficulté 1 ; niveau examen = archives seulement', () => {
    expect(selectQuestions(all, { mode: 'check' }, new Map(), now).map((q) => q.id)).toEqual(['ENDO-EX-thyroide-VF-001']);
    expect(selectQuestions(all, { mode: 'exam-level' }, new Map(), now).every((q) => q.kind === 'archive')).toBe(true);
  });
  it('filtre par chapitre et par statut', () => {
    expect(selectQuestions(all, { mode: 'free', chapters: ['hyper'] }, new Map(), now).map((q) => q.id)).toEqual([a2.id]);
    const failed = new Map([[a1.id, applyAttempt(emptyState(a1.id), { id: 'x', questionId: a1.id, at: '2026-03-01T10:00:00Z', mode: 'training', selected: ['A'], correct: false, hintsUsed: 0, durationMs: 1 })]]);
    expect(selectQuestions(all, { mode: 'free', status: 'failed' }, failed, now).map((q) => q.id)).toEqual([a1.id]);
  });
  it('mélange déterministe et indices interdits au niveau examen', () => {
    expect(shuffle([1, 2, 3, 4, 5], 7)).toEqual(shuffle([1, 2, 3, 4, 5], 7));
    expect(hintsAllowed('exam-level')).toBe(false);
    expect(hintsAllowed('training')).toBe(true);
  });
});
