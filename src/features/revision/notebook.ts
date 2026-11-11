/** Carnet d'erreurs et sessions de révision, calculés à partir de l'historique réel des tentatives. */
import type { Question } from '@/schemas/content';
import type { Attempt, QuestionState } from '@/schemas/progress';
import { isPlayable } from '@/services/scoring/score';
import { isMastered, statusOf } from '@/services/progress/questionState';
import { isDue } from '@/services/progress/srs';

export interface ErrorEntry {
  question: Question;
  lastWrong: Attempt;
  failures: number;
  attempts: number;
  lastAttemptAt: string;
  resolved: boolean; // la dernière tentative est juste
  status: ReturnType<typeof statusOf>;
}

export function errorNotebook(questions: Question[], attempts: Attempt[], states: Map<string, QuestionState>, now: Date): ErrorEntry[] {
  const byId = new Map(questions.map((q) => [q.id, q]));
  const grouped = new Map<string, Attempt[]>();
  for (const a of attempts) {
    if (!grouped.has(a.questionId)) grouped.set(a.questionId, []);
    grouped.get(a.questionId)!.push(a);
  }
  const out: ErrorEntry[] = [];
  for (const [id, list] of grouped) {
    const q = byId.get(id);
    const wrong = list.filter((a) => a.correct === false).sort((x, y) => y.at.localeCompare(x.at));
    if (!q || wrong.length === 0) continue;
    const sorted = [...list].sort((x, y) => y.at.localeCompare(x.at));
    out.push({
      question: q,
      lastWrong: wrong[0],
      failures: wrong.length,
      attempts: list.length,
      lastAttemptAt: sorted[0].at,
      resolved: sorted[0].correct === true,
      status: statusOf(states.get(id), now),
    });
  }
  return out.sort((a, b) => b.lastWrong.at.localeCompare(a.lastWrong.at));
}

export type ReviewKind = 'due' | 'recent-errors' | 'recurrent-errors' | 'not-mastered' | 'weak-chapter';

export interface ReviewSet {
  kind: ReviewKind;
  title: string;
  description: string;
  ids: string[];
  chapterId?: string;
}

const DAY = 86_400_000;

/** Ordre de priorité : les questions échouées passent avant les questions réussies. */
function prioritize(ids: string[], states: Map<string, QuestionState>): string[] {
  return [...ids].sort((a, b) => (states.get(a)?.box ?? 0) - (states.get(b)?.box ?? 0) || (states.get(a)?.dueAt ?? '').localeCompare(states.get(b)?.dueAt ?? ''));
}

export function reviewSets(questions: Question[], attempts: Attempt[], states: Map<string, QuestionState>, now: Date, chapterTitles: Record<string, string>): ReviewSet[] {
  const playable = new Map(questions.filter(isPlayable).map((q) => [q.id, q]));
  const notebook = errorNotebook([...playable.values()], attempts, states, now);
  const due = [...states.values()].filter((s) => playable.has(s.questionId) && s.attempts > 0 && (s.flagged || isDue(s.dueAt, now))).map((s) => s.questionId);
  const recent = notebook.filter((e) => !e.resolved && now.getTime() - new Date(e.lastWrong.at).getTime() <= 7 * DAY).map((e) => e.question.id);
  const recurrent = notebook.filter((e) => e.failures >= 2).map((e) => e.question.id);
  const notMastered = [...states.values()].filter((s) => playable.has(s.questionId) && s.attempts > 0 && !isMastered(s)).map((s) => s.questionId);

  // Chapitre le plus faible : plus bas taux de réussite (dernière réponse), au moins 3 questions travaillées.
  const perChapter = new Map<string, { ok: number; n: number }>();
  for (const s of states.values()) {
    const q = playable.get(s.questionId);
    if (!q || s.lastCorrect === null) continue;
    const c = perChapter.get(q.chapter) ?? { ok: 0, n: 0 };
    c.n += 1;
    if (s.lastCorrect) c.ok += 1;
    perChapter.set(q.chapter, c);
  }
  const weakest = [...perChapter.entries()].filter(([, v]) => v.n >= 3).sort((a, b) => a[1].ok / a[1].n - b[1].ok / b[1].n)[0];
  const sets: ReviewSet[] = [
    { kind: 'due', title: 'À revoir aujourd’hui', description: 'Questions arrivées à échéance de révision ou marquées « à revoir ».', ids: prioritize(due, states) },
    { kind: 'recent-errors', title: 'Erreurs récentes', description: 'Erreurs des 7 derniers jours, pas encore corrigées.', ids: recent },
    { kind: 'recurrent-errors', title: 'Erreurs récurrentes', description: 'Questions échouées au moins deux fois.', ids: prioritize(recurrent, states) },
    { kind: 'not-mastered', title: 'Questions non maîtrisées', description: 'Déjà travaillées mais pas encore stables dans le temps.', ids: prioritize(notMastered, states) },
  ];
  if (weakest) {
    const ids = [...playable.values()].filter((q) => q.chapter === weakest[0]).map((q) => q.id);
    sets.push({ kind: 'weak-chapter', title: `Chapitre à renforcer : ${chapterTitles[weakest[0]] ?? weakest[0]}`, description: `Taux de réussite actuel : ${Math.round((weakest[1].ok / weakest[1].n) * 100)} %.`, ids: prioritize(ids, states), chapterId: weakest[0] });
  }
  return sets;
}

/** Prochaines échéances de révision (pour le tableau de bord). */
export function upcomingReviews(states: Map<string, QuestionState>, now: Date, days = 7): { date: string; count: number }[] {
  const counts = new Map<string, number>();
  for (const s of states.values()) {
    if (!s.dueAt) continue;
    const t = new Date(s.dueAt).getTime();
    if (t > now.getTime() && t <= now.getTime() + days * DAY) counts.set(s.dueAt.slice(0, 10), (counts.get(s.dueAt.slice(0, 10)) ?? 0) + 1);
  }
  return [...counts.entries()].sort().map(([date, count]) => ({ date, count }));
}

/** Activité des derniers jours (nombre de réponses validées par jour). */
export function recentActivity(attempts: Attempt[], now: Date, days = 7): { date: string; count: number }[] {
  const out: { date: string; count: number }[] = [];
  for (let i = days - 1; i >= 0; i--) {
    const d = new Date(now.getTime() - i * DAY).toISOString().slice(0, 10);
    out.push({ date: d, count: attempts.filter((a) => a.at.slice(0, 10) === d).length });
  }
  return out;
}
