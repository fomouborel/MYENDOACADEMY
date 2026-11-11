import { Link, useNavigate, useParams } from 'react-router-dom';
import { SESSION_LABEL, questionById, questions } from '@/data/content';
import { isPlayable } from '@/services/scoring/score';
import { QuestionCard } from '@/features/quizzes/QuestionCard';
import { ReadOnlyQuestion } from '@/features/exams/ReadOnlyQuestion';

export function ArchiveQuestionPage() {
  const { questionId = '' } = useParams();
  const nav = useNavigate();
  const q = questionById.get(questionId);
  if (!q || q.kind !== 'archive') return <p>Question introuvable. <Link to="/examens">Retour aux anciens examens</Link></p>;
  const twins = q.duplicateGroup
    ? questions.filter((x) => x.kind === 'archive' && x.id !== q.id && x.duplicateGroup === q.duplicateGroup)
    : [];
  return (
    <section>
      <p className="crumbs"><button className="linklike" onClick={() => nav(-1)}>← Retour à la liste</button></p>
      <h1>Ancien examen — {SESSION_LABEL[q.provenance.session]}</h1>
      <p className="muted">Identifiant : {q.id} · source : {q.provenance.sourceFile}, page {q.provenance.page}</p>
      {isPlayable(q) ? <QuestionCard question={q} mode="archive-bank" hintsEnabled /> : <ReadOnlyQuestion q={q} />}
      {twins.length > 0 && (
        <>
          <h2>Même thème dans d’autres sessions ({twins.length})</h2>
          <ul>
            {twins.map((t) => t.kind === 'archive' && (
              <li key={t.id}><Link to={`/examens/${t.id}`}>{SESSION_LABEL[t.provenance.session]} — {t.stem.slice(0, 90)}{t.stem.length > 90 ? '…' : ''}</Link></li>
            ))}
          </ul>
        </>
      )}
    </section>
  );
}
