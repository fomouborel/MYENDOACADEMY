import type { Attempt, QuestionState, QuestionStatus } from '@/schemas/progress';
import { dueDate, isDue, nextBox } from './srs';

export function emptyState(questionId: string): QuestionState {
  return {
    questionId,
    attempts: 0,
    successes: 0,
    failures: 0,
    lastAttemptAt: null,
    lastCorrect: null,
    box: 0,
    dueAt: null,
    successDays: [],
    flagged: false,
    draft: false,
  };
}

const day = (iso: string) => iso.slice(0, 10);

/** Applique une tentative validée. Les tentatives non notées (correct = null) comptent comme travaillées. */
export function applyAttempt(state: QuestionState, a: Attempt): QuestionState {
  const s: QuestionState = { ...state, attempts: state.attempts + 1, lastAttemptAt: a.at, lastCorrect: a.correct, draft: false };
  if (a.correct === true) {
    s.successes += 1;
    if (!s.successDays.includes(day(a.at))) s.successDays = [...s.successDays, day(a.at)];
  } else if (a.correct === false) {
    s.failures += 1;
  }
  if (a.correct !== null) {
    s.box = nextBox({ box: state.box, correct: a.correct, hintsUsed: a.hintsUsed });
    s.dueAt = dueDate(s.box, new Date(a.at)).toISOString();
  }
  return s;
}

/** Recalcule l'état à partir de l'historique complet (utile après import ou migration). */
export function rebuildState(questionId: string, attempts: Attempt[], flagged = false): QuestionState {
  return [...attempts]
    .filter((a) => a.questionId === questionId)
    .sort((x, y) => x.at.localeCompare(y.at))
    .reduce(applyAttempt, { ...emptyState(questionId), flagged });
}

/**
 * Maîtrise : jamais après une seule bonne réponse.
 * Il faut au moins 3 réussites, sur au moins 2 jours différents, la dernière réponse juste
 * et la question arrivée en boîte 4 ou plus (réussites sans indice espacées dans le temps).
 */
export function isMastered(s: QuestionState): boolean {
  return s.successes >= 3 && s.successDays.length >= 2 && s.lastCorrect === true && s.box >= 4;
}

/** Statut affiché (prompt § 9). Priorité : en cours > à revoir > maîtrisée > réussie / échouée. */
export function statusOf(s: QuestionState | undefined, now: Date): QuestionStatus {
  if (!s) return 'not-started';
  if (s.draft) return 'in-progress';
  if (s.attempts === 0) return 'not-started';
  if (s.flagged) return 'to-review';
  if (s.lastCorrect === false) return 'failed';
  if (isMastered(s)) return isDue(s.dueAt, now) ? 'to-review' : 'mastered';
  if (s.lastCorrect === true) return isDue(s.dueAt, now) ? 'to-review' : 'success';
  return 'success'; // tentative non notée (QROC auto-évaluée) : travaillée
}

export const STATUS_LABEL: Record<QuestionStatus, string> = {
  'not-started': 'Non commencée',
  'in-progress': 'En cours',
  success: 'Réussie',
  failed: 'Échouée',
  'to-review': 'À revoir',
  mastered: 'Maîtrisée',
};
