import { Link, useParams } from 'react-router-dom';
import { chapterById, lessonMarkdown, questions } from '@/data/content';
import { LessonContent } from '@/features/learning/LessonContent';
import { useProgress } from '@/state/ProgressContext';
import { isPlayable } from '@/services/scoring/score';

export function LessonPage() {
  const { chapterId = '', lessonId = '' } = useParams();
  const c = chapterById.get(chapterId);
  const { lessons, lessonDone } = useProgress();
  const idx = c?.lessons.findIndex((l) => l.id === lessonId) ?? -1;
  if (!c || idx < 0) return <p>Leçon introuvable. <Link to="/cours">Retour à Mes cours</Link></p>;
  const l = c.lessons[idx];
  const prev = c.lessons[idx - 1];
  const next = c.lessons[idx + 1];
  const done = Boolean(lessons.get(l.id)?.completedAt);
  const linked = questions.filter((q) => q.lessonLinks.includes(l.id) && isPlayable(q)).length;

  return (
    <article>
      <p className="crumbs"><Link to="/cours">Mes cours</Link> › <Link to={`/cours/${c.id}`}>{c.title}</Link> › Leçon {idx + 1}</p>
      <p className="muted">⏱️ {l.minutes} min de lecture</p>
      <LessonContent markdown={lessonMarkdown(l.file)} />
      <div className="lesson-end">
        <button className={done ? 'btn ghost' : 'btn'} onClick={() => lessonDone(l.id, !done)}>
          {done ? '✓ Leçon terminée (cliquer pour annuler)' : 'J’ai terminé cette leçon'}
        </button>
        {linked > 0 && <Link className="btn secondary" to={`/quiz?mode=lesson&lesson=${l.id}`}>🎯 S’exercer sur cette leçon ({linked} questions)</Link>}
      </div>
      <nav className="pager" aria-label="Leçons">
        {prev ? <Link to={`/cours/${c.id}/lecon/${prev.id}`}>← {prev.title}</Link> : <span />}
        {next ? <Link to={`/cours/${c.id}/lecon/${next.id}`}>{next.title} →</Link> : <Link to={`/cours/${c.id}`}>Retour au cours →</Link>}
      </nav>
    </article>
  );
}
