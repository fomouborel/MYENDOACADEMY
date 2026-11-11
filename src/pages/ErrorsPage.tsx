import { useState } from 'react';
import { Link } from 'react-router-dom';
import { chapterById, lessonById, openChapters, questions } from '@/data/content';
import { useProgress } from '@/state/ProgressContext';
import { errorNotebook } from '@/features/revision/notebook';
import { STATUS_LABEL } from '@/services/progress/questionState';
import { reliabilityMessage } from '@/services/scoring/score';

const lab = (ids: string[]) => ids.map((e) => (e === 'VRAI' ? 'Vrai' : e === 'FAUX' ? 'Faux' : e)).join(' et ') || '—';

export function ErrorsPage() {
  const { attempts, states } = useProgress();
  const [chapter, setChapter] = useState('');
  const [view, setView] = useState<'open' | 'all' | 'recurrent'>('open');
  const now = new Date();
  let list = errorNotebook(questions, attempts, states, now);
  if (chapter) list = list.filter((e) => e.question.chapter === chapter);
  if (view === 'open') list = list.filter((e) => !e.resolved);
  if (view === 'recurrent') list = list.filter((e) => e.failures >= 2);
  const ids = list.map((e) => e.question.id).slice(0, 50).join(',');
  return (
    <section>
      <h1>Mes erreurs</h1>
      <p className="lead">Toutes tes erreurs sont conservées, même quand tu as ensuite réussi la question.</p>
      <div className="filters grid">
        <label>Afficher
          <select value={view} onChange={(e) => setView(e.target.value as typeof view)}>
            <option value="open">Erreurs non corrigées</option><option value="recurrent">Erreurs récurrentes (≥ 2)</option><option value="all">Toutes les erreurs</option>
          </select>
        </label>
        <label>Cours
          <select value={chapter} onChange={(e) => setChapter(e.target.value)}>
            <option value="">Tous</option>{openChapters.map((c) => <option key={c.id} value={c.id}>{c.title}</option>)}
          </select>
        </label>
      </div>
      {list.length === 0 ? (
        <div className="notice">Aucune erreur dans cette sélection. Les erreurs apparaîtront ici dès que tu répondras à des questions.</div>
      ) : (
        <>
          <Link className="btn" to={`/quiz?mode=free&ids=${ids}`}>🔁 Retravailler ces erreurs ({Math.min(50, list.length)})</Link>
          <ul className="error-list">
            {list.map((e) => {
              const lesson = lessonById.get(e.question.lessonLinks[0] ?? '');
              return (
                <li key={e.question.id} className="error-item">
                  <p className="archive-meta">{chapterById.get(e.question.chapter)?.title} · dernière erreur le {new Date(e.lastWrong.at).toLocaleDateString('fr-BE')} · {e.failures} échec(s) sur {e.attempts} tentative(s) · statut : {STATUS_LABEL[e.status]}{e.resolved ? ' (corrigée depuis)' : ''}</p>
                  <p className="stem">{e.question.stem}</p>
                  <p>Ta réponse : <strong>{lab(e.lastWrong.selected)}</strong> · Réponse attendue : <strong>{lab(e.question.expected)}</strong></p>
                  <p className="reliability">{reliabilityMessage(e.question)}</p>
                  {e.question.explanation && <p className="muted">🟨 {e.question.explanation.text}</p>}
                  <div className="qactions">
                    <Link className="btn ghost" to={e.question.kind === 'archive' ? `/examens/${e.question.id}` : `/quiz?mode=free&ids=${e.question.id}`}>Refaire la question</Link>
                    {lesson && <Link className="btn ghost" to={`/cours/${lesson.chapterId}/lecon/${lesson.id}`}>📖 {lesson.title}</Link>}
                  </div>
                </li>
              );
            })}
          </ul>
        </>
      )}
    </section>
  );
}
