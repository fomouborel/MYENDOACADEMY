import { useMemo, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import { QuestionCard } from '@/features/quizzes/QuestionCard';
import { newId } from '@/services/storage/db';
import { caseList } from './ClinicalCasesPage';

/** Cas clinique progressif : l'étape suivante n'apparaît qu'après la réponse à l'étape en cours. */
export function CasePage() {
  const { caseId = '' } = useParams();
  const c = caseList().find((x) => x.id === caseId);
  const sessionId = useMemo(() => newId(), []);
  const [reached, setReached] = useState(0); // nombre d'étapes répondues
  if (!c) return <p>Cas introuvable. <Link to="/cas-cliniques">Retour aux cas cliniques</Link></p>;
  const visible = c.steps.slice(0, Math.min(reached + 1, c.steps.length));
  return (
    <section>
      <p className="crumbs"><Link to="/cas-cliniques">Cas cliniques</Link></p>
      <h1>Cas clinique</h1>
      {visible.map((q, i) => (
        <div key={q.id} className="case-step">
          <h2>Étape {i + 1} / {c.steps.length}</h2>
          <QuestionCard question={q} mode="clinical-case" hintsEnabled sessionId={sessionId} onAnswered={() => setReached((r) => Math.max(r, i + 1))} />
        </div>
      ))}
      {reached >= c.steps.length && (
        <div className="notice">
          <strong>Cas terminé.</strong> Tu peux le refaire plus tard pour vérifier que le raisonnement est acquis. <Link to="/cas-cliniques">Autres cas</Link>
        </div>
      )}
    </section>
  );
}
