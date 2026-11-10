import type { Question } from '@/schemas/content';
import type { QuestionState } from '@/schemas/progress';
import { isPlayable } from '@/services/scoring/score';
import { statusOf } from './questionState';

export interface Coverage {
  available: number; // questions d'archives jouables
  consultOnly: number; // incomplètes / sans réponse : consultables seulement
  worked: number; // au moins une tentative validée
  succeeded: number; // dernière tentative juste (réussie ou maîtrisée)
  failed: number;
  toReview: number;
  mastered: number;
  remaining: number; // jamais tentées
}

/** Indicateur de couverture des archives (prompt § 9). Afficher ≠ travailler : seules les tentatives comptent. */
export function coverage(questions: Question[], states: Map<string, QuestionState>, now: Date): Coverage {
  const archive = questions.filter((q) => q.kind === 'archive');
  const playable = archive.filter(isPlayable);
  const c: Coverage = { available: playable.length, consultOnly: archive.length - playable.length, worked: 0, succeeded: 0, failed: 0, toReview: 0, mastered: 0, remaining: 0 };
  for (const q of playable) {
    const s = states.get(q.id);
    const st = statusOf(s, now);
    if (!s || s.attempts === 0) c.remaining += 1;
    else c.worked += 1;
    if (st === 'success' || st === 'mastered') c.succeeded += 1;
    if (st === 'failed') c.failed += 1;
    if (st === 'to-review') c.toReview += 1;
    if (st === 'mastered') c.mastered += 1;
  }
  return c;
}
