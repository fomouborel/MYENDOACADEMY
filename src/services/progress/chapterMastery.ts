import type { Question } from '@/schemas/content';
import type { QuestionState, SessionRecord } from '@/schemas/progress';
import { isPlayable } from '@/services/scoring/score';
import { isMastered } from './questionState';

export type MasteryLevel = 'not-started' | 'discovering' | 'progressing' | 'solid' | 'mastered';

export const MASTERY_LABEL: Record<MasteryLevel, string> = {
  'not-started': 'Non commencé',
  discovering: 'Découverte',
  progressing: 'En progression',
  solid: 'Solide',
  mastered: 'Maîtrisé',
};

export interface ChapterMastery {
  level: MasteryLevel;
  workedRatio: number; // part des questions jouables tentées
  masteredRatio: number; // part des questions jouables maîtrisées
  successRate: number | null; // réussite sur les dernières tentatives notées
  finalEvalsPassed: number; // évaluations finales ≥ 75 %, jours distincts
}

/**
 * Un chapitre n'est « maîtrisé » qu'avec des résultats stables :
 * ≥ 80 % des questions maîtrisées ET ≥ 2 évaluations finales réussies (≥ 75 %) à des jours différents.
 */
export function chapterMastery(chapterId: string, questions: Question[], states: Map<string, QuestionState>, sessions: SessionRecord[]): ChapterMastery {
  const qs = questions.filter((q) => q.chapter === chapterId && isPlayable(q));
  const total = qs.length || 1;
  let worked = 0;
  let mastered = 0;
  let notedLast = 0;
  let correctLast = 0;
  for (const q of qs) {
    const s = states.get(q.id);
    if (!s || s.attempts === 0) continue;
    worked += 1;
    if (isMastered(s)) mastered += 1;
    if (s.lastCorrect !== null) {
      notedLast += 1;
      if (s.lastCorrect) correctLast += 1;
    }
  }
  const evalDays = new Set(
    sessions
      .filter((x) => x.mode === 'final-eval' && x.chapterId === chapterId && x.finishedAt && (x.score ?? 0) >= 0.75)
      .map((x) => (x.finishedAt as string).slice(0, 10)),
  );
  const workedRatio = worked / total;
  const masteredRatio = mastered / total;
  const successRate = notedLast ? correctLast / notedLast : null;
  let level: MasteryLevel = 'not-started';
  if (worked > 0) level = 'discovering';
  if (workedRatio >= 0.3 && (successRate ?? 0) >= 0.5) level = 'progressing';
  if (workedRatio >= 0.7 && (successRate ?? 0) >= 0.7 && evalDays.size >= 1) level = 'solid';
  if (masteredRatio >= 0.8 && evalDays.size >= 2) level = 'mastered';
  return { level, workedRatio, masteredRatio, successRate, finalEvalsPassed: evalDays.size };
}
