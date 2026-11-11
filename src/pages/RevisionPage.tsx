import { Link } from 'react-router-dom';
import { chapters, questions } from '@/data/content';
import { useProgress } from '@/state/ProgressContext';
import { reviewSets, upcomingReviews } from '@/features/revision/notebook';

export function RevisionPage() {
  const { attempts, states } = useProgress();
  const now = new Date();
  const titles = Object.fromEntries(chapters.map((c) => [c.id, c.title]));
  const sets = reviewSets(questions, attempts, states, now, titles);
  const upcoming = upcomingReviews(states, now);
  return (
    <section>
      <h1>Mes révisions</h1>
      <p className="lead">Révision espacée : une question échouée revient dès le lendemain, une question réussie revient de plus en plus tard (3, 7, 14 puis 30 jours).</p>
      <ul className="cards">
        {sets.map((s) => (
          <li key={s.kind} className="card">
            <span className="card-title">{s.title}</span>
            <span className="card-sub">{s.description}</span>
            <span className="card-foot">{s.ids.length} question(s)</span>
            {s.ids.length > 0 ? (
              <Link className="btn" to={`/quiz?mode=free&ids=${s.ids.slice(0, 20).join(',')}`}>Réviser ({Math.min(20, s.ids.length)})</Link>
            ) : (
              <span className="muted">Rien à réviser ici pour l’instant.</span>
            )}
          </li>
        ))}
      </ul>
      <h2>Prochaines révisions</h2>
      {upcoming.length ? (
        <ul>{upcoming.map((u) => <li key={u.date}>{new Date(u.date).toLocaleDateString('fr-BE', { weekday: 'long', day: 'numeric', month: 'long' })} : {u.count} question(s)</li>)}</ul>
      ) : (
        <p className="muted">Aucune révision programmée dans les 7 prochains jours.</p>
      )}
    </section>
  );
}
