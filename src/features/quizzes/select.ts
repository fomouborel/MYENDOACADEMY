/** Sélection des questions d'une session (parcours de chapitre, leçon, entraînement libre). Logique pure. */
import type { Question } from '@/schemas/content';
import type { QuestionState } from '@/schemas/progress';
import { isPlayable } from '@/services/scoring/score';
import { statusOf } from '@/services/progress/questionState';
import { audienceOf } from '@/utils/audience';

export type QuizMode = 'check' | 'training' | 'exam-level' | 'lesson' | 'free';

export interface QuizFilters {
  mode: QuizMode;
  chapters?: string[];
  lesson?: string;
  audience?: 'all' | 'adulte' | 'pediatrie';
  status?: 'all' | 'not-started' | 'failed' | 'to-review';
  kind?: 'all' | 'archive' | 'exercise';
  limit?: number;
  seed?: number;
}

/** Mélange déterministe (même session = même ordre après un rechargement). */
export function shuffle<T>(items: T[], seed: number): T[] {
  const a = [...items];
  let s = seed || 1;
  for (let i = a.length - 1; i > 0; i--) {
    s = (s * 1103515245 + 12345) % 2147483648;
    const j = s % (i + 1);
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

export function selectQuestions(all: Question[], f: QuizFilters, states: Map<string, QuestionState>, now: Date): Question[] {
  let qs = all.filter(isPlayable);
  if (f.chapters?.length) qs = qs.filter((q) => f.chapters!.includes(q.chapter));
  if (f.lesson) qs = qs.filter((q) => q.lessonLinks.includes(f.lesson!));
  if (f.audience && f.audience !== 'all') qs = qs.filter((q) => audienceOf(q) === f.audience);
  if (f.kind && f.kind !== 'all') qs = qs.filter((q) => q.kind === f.kind);
  if (f.status && f.status !== 'all') qs = qs.filter((q) => statusOf(states.get(q.id), now) === f.status);

  switch (f.mode) {
    case 'check': // Vérifier ma compréhension : questions faciles
      qs = qs.filter((q) => q.difficulty === 1);
      break;
    case 'training': // M'entraîner : difficulté progressive
      qs = qs.filter((q) => q.difficulty <= 2).sort((a, b) => a.difficulty - b.difficulty);
      break;
    case 'exam-level': // Niveau examen : toutes les questions d'archives
      qs = qs.filter((q) => q.kind === 'archive');
      break;
    default:
      break;
  }
  if (f.mode === 'free' || f.mode === 'exam-level') qs = shuffle(qs, f.seed ?? 1);
  return f.limit ? qs.slice(0, f.limit) : qs;
}

/** Les indices sont désactivés au niveau examen (prompt § 10, étape 4). */
export const hintsAllowed = (mode: QuizMode) => mode !== 'exam-level';
