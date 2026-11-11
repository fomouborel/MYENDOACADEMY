import { Link, useParams } from 'react-router-dom';
import { chapterById, questions } from '@/data/content';
import { useProgress } from '@/state/ProgressContext';
import { selectQuestions } from '@/features/quizzes/select';
import { chapterMastery, MASTERY_LABEL } from '@/services/progress/chapterMastery';
import { isPlayable } from '@/services/scoring/score';

export function ChapterPage() {
  const { chapterId = '' } = useParams();
  const c = chapterById.get(chapterId);
  const { states, lessons, sessions } = useProgress();
  if (!c || c.lessons.length === 0) return <p>Ce cours n’est pas encore disponible. <Link to="/cours">Retour à Mes cours</Link></p>;

  const now = new Date();
  const count = (mode: 'check' | 'training' | 'exam-level') => selectQuestions(questions, { mode, chapters: [c.id] }, states, now).length;
  const m = chapterMastery(c.id, questions, states, sessions);
  const chapterQs = questions.filter((q) => q.chapter === c.id && isPlayable(q));

  const bySub = c.subchapters.map((s) => {
    const qs = chapterQs.filter((q) => q.subchapter === s.id);
    const tried = qs.filter((q) => (states.get(q.id)?.attempts ?? 0) > 0);
    const ok = tried.filter((q) => states.get(q.id)?.lastCorrect === true);
    return { ...s, total: qs.length, tried: tried.length, ok: ok.length };
  });

  return (
    <section>
      <p className="crumbs"><Link to="/cours">Mes cours</Link> › {c.title}</p>
      <h1>{c.icon} {c.title}</h1>
      <p className="lead">{c.short}</p>
      <p className="badge-line"><span className="badge">Niveau : {MASTERY_LABEL[m.level]}</span></p>

      <ol className="steps">
        <li className="step">
          <h2>1. Apprendre</h2>
          <ul className="lesson-list">
            {c.lessons.map((l, i) => {
              const done = Boolean(lessons.get(l.id)?.completedAt);
              return (
                <li key={l.id}>
                  <Link to={`/cours/${c.id}/lecon/${l.id}`} className={done ? 'lesson-item done' : 'lesson-item'}>
                    <span className="lesson-num">{done ? '✓' : i + 1}</span>
                    <span>{l.title}</span>
                    <span className="muted">{l.minutes} min</span>
                  </Link>
                </li>
              );
            })}
          </ul>
        </li>
        <li className="step">
          <h2>2. Vérifier ma compréhension</h2>
          <p className="muted">Questions simples (vrai ou faux) pour vérifier les notions de base.</p>
          <Link className="btn" to={`/quiz?mode=check&chapter=${c.id}`}>Commencer ({count('check')} questions)</Link>
        </li>
        <li className="step">
          <h2>3. M’entraîner</h2>
          <p className="muted">Difficulté progressive, avec indices.</p>
          <Link className="btn" to={`/quiz?mode=training&chapter=${c.id}`}>Commencer ({count('training')} questions)</Link>
        </li>
        <li className="step">
          <h2>4. Niveau examen</h2>
          <p className="muted">Les vraies questions des anciens examens rattachées à ce cours, sans indice.</p>
          <Link className="btn" to={`/quiz?mode=exam-level&chapter=${c.id}`}>Commencer ({count('exam-level')} questions)</Link>
        </li>
        <li className="step">
          <h2>Bilan</h2>
          <div className="table-wrap">
            <table>
              <thead><tr><th>Sous-chapitre</th><th>Travaillées</th><th>Réussies</th></tr></thead>
              <tbody>
                {bySub.map((s) => (
                  <tr key={s.id}><td>{s.title}</td><td>{s.tried} / {s.total}</td><td>{s.tried ? `${Math.round((s.ok / s.tried) * 100)} %` : '—'}</td></tr>
                ))}
              </tbody>
            </table>
          </div>
          <p className="muted">L’évaluation finale et le bilan détaillé (erreurs, notions à revoir) arrivent avec les rubriques « Mes erreurs » et « Mes révisions ».</p>
        </li>
      </ol>
    </section>
  );
}
