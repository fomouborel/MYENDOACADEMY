import { Link, useNavigate, useParams } from 'react-router-dom';
import { chapterById, questions } from '@/data/content';
import { useProgress } from '@/state/ProgressContext';
import { selectQuestions } from '@/features/quizzes/select';
import { chapterMastery, MASTERY_LABEL } from '@/services/progress/chapterMastery';
import { isPlayable } from '@/services/scoring/score';
import { buildFinalEval } from '@/features/exams/mockExam';
import { errorNotebook } from '@/features/revision/notebook';
import { isMastered } from '@/services/progress/questionState';
import { lessonById } from '@/data/content';
import { newId } from '@/services/storage/db';

export function ChapterPage() {
  const { chapterId = '' } = useParams();
  const c = chapterById.get(chapterId);
  const { states, lessons, sessions, attempts, saveSession, setDraft } = useProgress();
  const nav = useNavigate();
  if (!c || c.lessons.length === 0) return <p>Ce cours n’est pas encore disponible. <Link to="/cours">Retour à Mes cours</Link></p>;

  const now = new Date();
  const count = (mode: 'check' | 'training' | 'exam-level') => selectQuestions(questions, { mode, chapters: [c.id] }, states, now).length;
  const m = chapterMastery(c.id, questions, states, sessions);
  const chapterQs = questions.filter((q) => q.chapter === c.id && isPlayable(q));

  async function startEval() {
    const qs = buildFinalEval(questions, c!.id, Date.now() % 100000);
    const rec = { id: newId(), mode: 'final-eval' as const, chapterId: c!.id, questionIds: qs.map((q) => q.id), answers: {}, startedAt: new Date().toISOString(), finishedAt: null, timeLimitMinutes: null, score: null };
    await saveSession(rec);
    await setDraft(rec.questionIds, true);
    nav(`/session/${rec.id}`);
  }
  const evals = sessions.filter((s) => s.mode === 'final-eval' && s.chapterId === c.id && s.finishedAt).sort((a, b) => (b.finishedAt ?? '').localeCompare(a.finishedAt ?? ''));
  const errors = errorNotebook(chapterQs, attempts, states, now).filter((e) => !e.resolved);
  const examNotMastered = chapterQs.filter((q) => q.kind === 'archive' && (states.get(q.id)?.attempts ?? 0) > 0 && !isMastered(states.get(q.id)!));
  const lessonsToReview = [...new Set(errors.flatMap((e) => e.question.lessonLinks.slice(0, 1)))].map((l) => lessonById.get(l)).filter(Boolean);

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
          <StartButton n={count('check')} to={`/quiz?mode=check&chapter=${c.id}`} />
        </li>
        <li className="step">
          <h2>3. M’entraîner</h2>
          <p className="muted">Difficulté progressive, avec indices.</p>
          <StartButton n={count('training')} to={`/quiz?mode=training&chapter=${c.id}`} />
        </li>
        <li className="step">
          <h2>4. Niveau examen</h2>
          <p className="muted">Les vraies questions des anciens examens rattachées à ce cours, sans indice.</p>
          <StartButton n={count('exam-level')} to={`/quiz?mode=exam-level&chapter=${c.id}`} />
        </li>
        <li className="step">
          <h2>5. Évaluation finale</h2>
          <p className="muted">15 questions mélangées (anciens examens et exercices), sans indice, corrigées à la fin.</p>
          <button className="btn" onClick={startEval}>Commencer l’évaluation</button>
          {evals.length > 0 && <p className="muted">Dernières évaluations : {evals.slice(0, 3).map((e) => `${Math.round((e.score ?? 0) * 100)} % le ${new Date(e.finishedAt!).toLocaleDateString('fr-BE')}`).join(' · ')}</p>}
        </li>
        <li className="step">
          <h2>6. Bilan</h2>
          <p><strong>Niveau de maîtrise :</strong> {MASTERY_LABEL[m.level]} · {Math.round(m.workedRatio * 100)} % des questions travaillées · réussite {m.successRate === null ? '—' : `${Math.round(m.successRate * 100)} %`} · {m.finalEvalsPassed} évaluation(s) réussie(s) à des jours différents</p>
          <div className="table-wrap" tabIndex={0} role="region" aria-label="Tableau">
            <table>
              <thead><tr><th>Sous-chapitre</th><th>Travaillées</th><th>Réussite</th><th>Appréciation</th></tr></thead>
              <tbody>
                {bySub.map((s) => {
                  const rate = s.tried ? s.ok / s.tried : null;
                  return <tr key={s.id}><td>{s.title}</td><td>{s.tried} / {s.total}</td><td>{rate === null ? '—' : `${Math.round(rate * 100)} %`}</td><td>{rate === null ? 'à commencer' : rate >= 0.75 ? '💪 point fort' : rate < 0.5 ? '⚠️ lacune' : 'en progrès'}</td></tr>;
                })}
              </tbody>
            </table>
          </div>
          {lessonsToReview.length > 0 && <p><strong>Notions à revoir :</strong> {lessonsToReview.map((l) => <Link key={l!.id} to={`/cours/${c.id}/lecon/${l!.id}`}>{l!.title}</Link>).reduce<React.ReactNode[]>((a, x, i) => (i ? [...a, ' · ', x] : [x]), [])}</p>}
          <p><strong>Erreurs en cours :</strong> {errors.length} · <strong>Questions d’examen non encore maîtrisées :</strong> {examNotMastered.length}</p>
          <div className="qactions">
            {errors.length > 0 && <Link className="btn ghost" to={`/quiz?mode=free&ids=${errors.map((e) => e.question.id).slice(0, 50).join(',')}`}>Retravailler mes erreurs</Link>}
            {examNotMastered.length > 0 && <Link className="btn ghost" to={`/quiz?mode=free&ids=${examNotMastered.map((q) => q.id).slice(0, 50).join(',')}`}>Questions d’examen non maîtrisées</Link>}
          </div>
          <p className="muted">Un cours n’est « maîtrisé » qu’avec 80 % de questions maîtrisées dans la durée et deux évaluations finales réussies à des jours différents.</p>
        </li>
      </ol>
    </section>
  );
}

/** Pas de bouton vers une liste vide : on dit simplement qu'il n'y a encore rien. */
function StartButton({ n, to }: { n: number; to: string }) {
  if (n === 0) return <p className="muted">Pas encore de questions de ce type pour ce cours.</p>;
  return <Link className="btn" to={to}>Commencer ({n} question{n > 1 ? 's' : ''})</Link>;
}
