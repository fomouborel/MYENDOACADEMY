/** Question consultable mais non notée (incomplète, sans réponse, ou réponse discutée incohérente avec la consigne). */
import { Link } from 'react-router-dom';
import type { Question } from '@/schemas/content';
import { lessonById } from '@/data/content';
import { instructionLabel, reliabilityMessage } from '@/services/scoring/score';

export function ReadOnlyQuestion({ q }: { q: Question }) {
  return (
    <article className="qcard">
      <div className="notice warn">
        <strong>Question consultable, non notée.</strong> {reliabilityMessage(q)}
        {q.answerNote && <> {q.answerNote}</>}
      </div>
      <p className="stem">{q.stem}</p>
      {q.instruction && <p className="instruction">{instructionLabel(q.instruction)}</p>}
      {q.options.length > 0 ? (
        <ul className="choices" role="list">
          {q.options.map((o) => (
            <li key={o.id}>
              <div className={`choice static ${q.expected.includes(o.id) ? 'marked' : ''}`}>
                <span className="letter">{o.id}</span>
                <span className="choice-text">{o.text}</span>
              </div>
              {q.expected.includes(o.id) && <div className="choice-feedback"><strong>Marquée en rouge dans la compilation</strong> (non officielle, à considérer avec prudence)</div>}
            </li>
          ))}
        </ul>
      ) : (
        <p className="muted">Les propositions n’ont pas été retranscrites.</p>
      )}
      {q.sourceComments.length > 0 && <p className="muted">Commentaires de la compilation : {q.sourceComments.join(' · ')}</p>}
      <div className="qactions">
        {q.lessonLinks.map((l) => {
          const lesson = lessonById.get(l);
          return lesson ? <Link key={l} className="btn ghost" to={`/cours/${lesson.chapterId}/lecon/${l}`}>📖 Revoir : {lesson.title}</Link> : null;
        })}
      </div>
    </article>
  );
}
