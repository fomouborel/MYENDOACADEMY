import { Link } from 'react-router-dom';
import { integratedDomainsLabel, lessons as allLessons, openChapters, questions } from '@/data/content';
import { ChapterCard } from '@/components/ChapterCard';
import { BackupReminder } from '@/components/BackupReminder';
import { CoverageStats } from '@/components/Stats';
import { useProgress } from '@/state/ProgressContext';
import { chapterMastery, MASTERY_LABEL } from '@/services/progress/chapterMastery';
import { errorNotebook, recentActivity, reviewSets, upcomingReviews } from '@/features/revision/notebook';

/** Tableau de bord (prompt § 13) : uniquement des chiffres calculés à partir des réponses réelles. */
export function HomePage() {
  const { lessons, states, sessions, attempts } = useProgress();
  const now = new Date();
  const nextLesson = allLessons.find((l) => !lessons.get(l.id)?.completedAt);
  const levels = openChapters.map((c) => ({ c, m: chapterMastery(c.id, questions, states, sessions) }));
  const mastered = levels.filter((x) => x.m.level === 'mastered');
  const toStrengthen = levels.filter((x) => x.m.level !== 'not-started' && x.m.level !== 'mastered' && (x.m.successRate ?? 1) < 0.7);
  const errors = errorNotebook(questions, attempts, states, now).filter((e) => !e.resolved).slice(0, 5);
  const due = reviewSets(questions, attempts, states, now, {}).find((s) => s.kind === 'due')!;
  const upcoming = upcomingReviews(states, now);
  const activity = recentActivity(attempts, now);
  const maxAct = Math.max(1, ...activity.map((a) => a.count));
  const started = attempts.length > 0;

  return (
    <section>
      <h1>Bienvenue</h1>
      <p className="lead">Comprendre tes cours, travailler les anciens examens d’endocrinologie et suivre ta progression.</p>
      {nextLesson && (
        <div className="notice"><strong>Pour continuer :</strong> <Link to={`/cours/${nextLesson.chapterId}/lecon/${nextLesson.id}`}>{nextLesson.title}</Link></div>
      )}
      <BackupReminder />
      {due.ids.length > 0 && (
        <div className="notice"><strong>🔁 {due.ids.length} question(s) à réviser aujourd’hui.</strong> <Link to={`/quiz?mode=free&ids=${due.ids.slice(0, 20).join(',')}`}>Réviser maintenant</Link></div>
      )}

      <h2>Tes cours ({integratedDomainsLabel})</h2>
      <ul className="cards">{openChapters.map((c) => <ChapterCard key={c.id} c={c} />)}</ul>

      <h2>Ta progression</h2>
      <CoverageStats />

      {started ? (
        <div className="dash">
          <div className="panel">
            <h3>Niveau par cours</h3>
            <ul className="plain">{levels.map(({ c, m }) => <li key={c.id}>{c.icon} {c.title} : <strong>{MASTERY_LABEL[m.level]}</strong></li>)}</ul>
            <p className="muted">Maîtrisés : {mastered.length ? mastered.map((x) => x.c.title).join(', ') : 'aucun pour l’instant'} · À renforcer : {toStrengthen.length ? toStrengthen.map((x) => x.c.title).join(', ') : '—'}</p>
          </div>
          <div className="panel">
            <h3>Dernières erreurs</h3>
            {errors.length ? <ul className="plain">{errors.map((e) => <li key={e.question.id}>{e.question.stem.slice(0, 80)}{e.question.stem.length > 80 ? '…' : ''}</li>)}</ul> : <p className="muted">Aucune erreur en cours.</p>}
            <Link to="/erreurs">Voir le carnet d’erreurs</Link>
          </div>
          <div className="panel">
            <h3>Prochaines révisions</h3>
            {upcoming.length ? <ul className="plain">{upcoming.slice(0, 4).map((u) => <li key={u.date}>{new Date(u.date).toLocaleDateString('fr-BE', { weekday: 'short', day: 'numeric', month: 'short' })} : {u.count}</li>)}</ul> : <p className="muted">Rien de programmé cette semaine.</p>}
            <Link to="/revisions">Mes révisions</Link>
          </div>
          <div className="panel">
            <h3>Activité des 7 derniers jours</h3>
            <div className="bars" aria-label="Réponses validées par jour">
              {activity.map((a) => (
                <div key={a.date} className="bar-col" title={`${a.count} réponse(s)`}>
                  <span className="bar" style={{ height: `${(a.count / maxAct) * 60}px` }} />
                  <span className="bar-label">{new Date(a.date).toLocaleDateString('fr-BE', { weekday: 'narrow' })}</span>
                  <span className="bar-v">{a.count}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      ) : (
        <p className="muted">Ton tableau de bord se remplira dès tes premières réponses.</p>
      )}
      <p className="muted">
        Banque actuelle : {questions.filter((q) => q.kind === 'archive').length} questions d’anciens examens ({integratedDomainsLabel}, 2016-2026), {questions.filter((q) => q.kind === 'exercise').length} exercices et cas cliniques.{' '}
        <Link to="/examens">Parcourir les anciens examens</Link>
      </p>
    </section>
  );
}
