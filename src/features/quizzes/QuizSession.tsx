import { useMemo, useState } from 'react';
import { Link } from 'react-router-dom';
import type { Question } from '@/schemas/content';
import type { Mode } from '@/schemas/progress';
import { newId } from '@/services/storage/db';
import { QuestionCard } from './QuestionCard';

/** Enchaîne les questions d'une session puis affiche un bilan. */
export function QuizSession({ questions, mode, hintsEnabled, backTo }: { questions: Question[]; mode: Mode; hintsEnabled: boolean; backTo: { to: string; label: string } }) {
  const sessionId = useMemo(() => newId(), []);
  const [index, setIndex] = useState(0);
  const [answers, setAnswers] = useState<Record<string, boolean | null>>({});
  const done = index >= questions.length;

  if (questions.length === 0) {
    return (
      <div className="notice">
        Aucune question ne correspond pour l’instant. <Link to={backTo.to}>{backTo.label}</Link>
      </div>
    );
  }

  if (done) {
    const noted = Object.values(answers).filter((v) => v !== null);
    const good = noted.filter(Boolean).length;
    const wrong = questions.filter((q) => answers[q.id] === false);
    return (
      <section className="summary">
        <h2>Bilan de la série</h2>
        <p className="score">{good} / {noted.length} bonne{good > 1 ? 's' : ''} réponse{good > 1 ? 's' : ''}</p>
        {wrong.length > 0 ? (
          <>
            <h3>À retravailler</h3>
            <ul>{wrong.map((q) => <li key={q.id}>{q.stem}</li>)}</ul>
            <p className="muted">Ces questions reviendront dans tes révisions.</p>
          </>
        ) : (
          <p>Bravo, aucune erreur dans cette série. Une seule réussite ne suffit pas à maîtriser : ces questions reviendront plus tard pour vérifier que c’est acquis.</p>
        )}
        <div className="qactions">
          <button className="btn" onClick={() => { setIndex(0); setAnswers({}); }}>Refaire la série</button>
          <Link className="btn ghost" to={backTo.to}>{backTo.label}</Link>
        </div>
      </section>
    );
  }

  const q = questions[index];
  const answered = q.id in answers;
  return (
    <div>
      <div className="progressbar" role="progressbar" aria-valuemin={0} aria-valuemax={questions.length} aria-valuenow={index + 1}>
        <span style={{ width: `${((index + (answered ? 1 : 0)) / questions.length) * 100}%` }} />
      </div>
      <p className="muted">Question {index + 1} sur {questions.length}{hintsEnabled ? '' : ' · sans indice (niveau examen)'}</p>
      <QuestionCard key={q.id} question={q} mode={mode} hintsEnabled={hintsEnabled} sessionId={sessionId} onAnswered={(c) => setAnswers((a) => ({ ...a, [q.id]: c }))} />
      {answered && (
        <div className="qactions sticky-next">
          <button className="btn" onClick={() => setIndex((i) => i + 1)}>{index + 1 < questions.length ? 'Question suivante →' : 'Voir le bilan'}</button>
        </div>
      )}
    </div>
  );
}
