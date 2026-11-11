import { Link } from 'react-router-dom';
import { SESSION_LABEL, chapterById, questions } from '@/data/content';
import { useProgress } from '@/state/ProgressContext';
import { isPlayable } from '@/services/scoring/score';

export function caseList() {
  const byCase = new Map<string, typeof questions>();
  for (const q of questions) if (q.caseId) byCase.set(q.caseId, [...(byCase.get(q.caseId) ?? []), q]);
  return [...byCase.entries()].map(([id, steps]) => ({ id, steps: steps.sort((a, b) => (a.caseStep ?? 0) - (b.caseStep ?? 0)) }));
}

export function ClinicalCasesPage() {
  const { states } = useProgress();
  const cases = caseList();
  const examCases = questions.filter((q) => q.kind === 'archive' && q.clinical && isPlayable(q));
  return (
    <section>
      <h1>Cas cliniques</h1>
      <p className="lead">Raisonne étape par étape : chaque étape se débloque après ta réponse, sans révéler le diagnostic à l’avance.</p>
      <h2>Cas progressifs</h2>
      <p className="muted">Cas créés pour l’entraînement à partir des notions des anciens examens (hors archives). Les normes biologiques sont reprises d’un énoncé d’examen.</p>
      <ul className="cards">
        {cases.map((c) => {
          const first = c.steps[0];
          const done = c.steps.filter((s) => (states.get(s.id)?.attempts ?? 0) > 0).length;
          return (
            <li key={c.id} className="card">
              <Link to={`/cas-cliniques/${c.id}`} className="card-link">
                <span className="card-icon" aria-hidden>{chapterById.get(first.chapter)?.icon}</span>
                <span className="card-title">{chapterById.get(first.chapter)?.title} — {c.steps.length} étapes</span>
                <span className="card-sub">{first.stem.slice(0, 120)}…</span>
                <span className="card-foot">{done}/{c.steps.length} étapes déjà faites</span>
              </Link>
            </li>
          );
        })}
      </ul>
      <h2>Cas cliniques des anciens examens ({examCases.length})</h2>
      <ul className="archive-list">
        {examCases.map((q) => q.kind === 'archive' && (
          <li key={q.id}>
            <Link className="archive-item" to={`/examens/${q.id}`}>
              <span className="archive-meta">{SESSION_LABEL[q.provenance.session]} · {chapterById.get(q.chapter)?.title}</span>
              <span className="archive-stem">{q.stem}</span>
            </Link>
          </li>
        ))}
      </ul>
    </section>
  );
}
