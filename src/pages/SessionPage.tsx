import { Link, useParams } from 'react-router-dom';
import { chapterById } from '@/data/content';
import { useProgress } from '@/state/ProgressContext';
import { ExamRunner } from '@/features/exams/ExamRunner';

export function SessionPage() {
  const { sessionId = '' } = useParams();
  const { sessions, ready } = useProgress();
  if (!ready) return <p>Chargement…</p>;
  const s = sessions.find((x) => x.id === sessionId);
  if (!s) return <p>Session introuvable. <Link to="/examens-blancs">Retour aux examens blancs</Link></p>;
  const isEval = s.mode === 'final-eval';
  const chapter = s.chapterId ? chapterById.get(s.chapterId) : undefined;
  const title = isEval ? `Évaluation finale — ${chapter?.title ?? ''}` : 'Examen blanc';
  const backTo = isEval && chapter ? { to: `/cours/${chapter.id}`, label: `Retour au cours « ${chapter.title} »` } : { to: '/examens-blancs', label: 'Retour aux examens blancs' };
  return (
    <section>
      <h1>{title}</h1>
      <ExamRunner key={s.id} session={s} title={title} backTo={backTo} />
    </section>
  );
}
