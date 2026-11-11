/** Composition d'un examen blanc. Ne reconstitue jamais une composition officielle inconnue. */
import type { Question } from '@/schemas/content';
import { isPlayable } from '@/services/scoring/score';
import { shuffle } from '@/features/quizzes/select';

export interface MockConfig {
  source: 'session' | 'teacher' | 'mix';
  session?: string;
  teacher?: string;
  chapters?: string[];
  count: number;
  minutes: number;
  seed: number;
}

export function buildMockExam(all: Question[], c: MockConfig): Question[] {
  let qs = all.filter((q) => isPlayable(q) && q.kind === 'archive');
  if (c.source === 'session' && c.session) {
    qs = qs.filter((q) => q.kind === 'archive' && q.provenance.session === c.session);
    // ordre de l'examen d'origine quand il est connu
    qs = [...qs].sort((a, b) => (a.kind === 'archive' && b.kind === 'archive' ? (a.provenance.originalNumber ?? 999) - (b.provenance.originalNumber ?? 999) || a.provenance.page - b.provenance.page : 0));
    return qs.slice(0, c.count);
  }
  if (c.source === 'teacher' && c.teacher) qs = qs.filter((q) => q.kind === 'archive' && (q.provenance.teacher ?? 'non attribué') === c.teacher);
  if (c.chapters?.length) qs = qs.filter((q) => c.chapters!.includes(q.chapter));
  return shuffle(qs, c.seed).slice(0, c.count);
}

export function remainingMs(startedAt: string, minutes: number | null, now: number): number | null {
  if (!minutes) return null;
  return Math.max(0, new Date(startedAt).getTime() + minutes * 60_000 - now);
}

export function formatClock(ms: number): string {
  const s = Math.ceil(ms / 1000);
  const m = Math.floor(s / 60);
  return `${String(m).padStart(2, '0')}:${String(s % 60).padStart(2, '0')}`;
}

/** Évaluation finale d'un chapitre : 15 questions mélangées, formats variés (archives + exercices), sans indice. */
export function buildFinalEval(all: Question[], chapterId: string, seed: number, n = 15): Question[] {
  const pool = all.filter((q) => isPlayable(q) && q.chapter === chapterId && !q.caseId);
  const archives = shuffle(pool.filter((q) => q.kind === 'archive'), seed);
  const exercises = shuffle(pool.filter((q) => q.kind === 'exercise'), seed + 1);
  const picked = [...exercises.slice(0, Math.min(4, exercises.length)), ...archives].slice(0, n);
  return shuffle(picked, seed + 2);
}
