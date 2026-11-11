import { useMemo } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import { chapterById, lessonById, questions } from '@/data/content';
import { useProgress } from '@/state/ProgressContext';
import { hintsAllowed, selectQuestions, type QuizFilters, type QuizMode } from '@/features/quizzes/select';
import { QuizSession } from '@/features/quizzes/QuizSession';
import type { Mode } from '@/schemas/progress';

const TITLES: Record<QuizMode, string> = {
  check: 'Vérifier ma compréhension',
  training: 'M’entraîner',
  'exam-level': 'Niveau examen',
  lesson: 'S’exercer sur la leçon',
  free: 'Entraînement',
};
const STORE_MODE: Record<QuizMode, Mode> = { check: 'check', training: 'training', 'exam-level': 'exam-level', lesson: 'training', free: 'training' };

export function QuizPage() {
  const [p] = useSearchParams();
  const { states, ready } = useProgress();
  const mode = (p.get('mode') ?? 'free') as QuizMode;
  const filters: QuizFilters = {
    mode,
    chapters: p.get('chapter')?.split(',').filter(Boolean),
    lesson: p.get('lesson') ?? undefined,
    ids: p.get('ids')?.split(',').filter(Boolean),
    audience: (p.get('audience') as QuizFilters['audience']) ?? 'all',
    status: (p.get('status') as QuizFilters['status']) ?? 'all',
    kind: (p.get('kind') as QuizFilters['kind']) ?? 'all',
    limit: p.get('n') ? Number(p.get('n')) : undefined,
    seed: p.get('seed') ? Number(p.get('seed')) : 1,
  };
  // La liste est figée au démarrage : répondre ne doit pas faire disparaître la question en cours.
  // eslint-disable-next-line react-hooks/exhaustive-deps
  const list = useMemo(() => (ready ? selectQuestions(questions, filters, states, new Date()) : []), [ready, p.toString()]);

  const chapter = filters.chapters?.length === 1 ? chapterById.get(filters.chapters[0]) : undefined;
  const lesson = filters.lesson ? lessonById.get(filters.lesson) : undefined;
  const backTo = lesson
    ? { to: `/cours/${lesson.chapterId}/lecon/${lesson.id}`, label: 'Retour à la leçon' }
    : chapter
      ? { to: `/cours/${chapter.id}`, label: `Retour au cours « ${chapter.title} »` }
      : filters.ids
        ? { to: '/examens', label: 'Retour aux anciens examens' }
        : { to: '/entrainement', label: 'Retour à l’entraînement' };

  if (!ready) return <p>Chargement de ta progression…</p>;
  return (
    <section>
      <p className="crumbs"><Link to={backTo.to}>{backTo.label}</Link></p>
      <h1>{TITLES[mode]}{chapter ? ` — ${chapter.title}` : ''}{lesson ? ` — ${lesson.title}` : ''}</h1>
      <QuizSession questions={list} mode={STORE_MODE[mode]} hintsEnabled={hintsAllowed(mode)} backTo={backTo} />
    </section>
  );
}
