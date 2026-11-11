/**
 * Moteur commun aux examens blancs et à l'évaluation finale : réponses sans correction, sauvegarde
 * continue (brouillon repris après interruption), chronomètre optionnel, correction détaillée à la fin.
 */
import { useEffect, useMemo, useRef, useState } from 'react';
import { Link } from 'react-router-dom';
import type { Question } from '@/schemas/content';
import type { SessionRecord } from '@/schemas/progress';
import { questionById, lessonById, SESSION_LABEL } from '@/data/content';
import { expectedSelectionCount, grade, instructionLabel, reliabilityMessage } from '@/services/scoring/score';
import { newId } from '@/services/storage/db';
import { useProgress } from '@/state/ProgressContext';
import { formatClock, remainingMs } from './mockExam';

export function ExamRunner({ session, title, backTo }: { session: SessionRecord; title: string; backTo: { to: string; label: string } }) {
  const { saveSession, record, setDraft } = useProgress();
  const qs = useMemo(() => session.questionIds.map((id) => questionById.get(id)).filter((q): q is Question => Boolean(q)), [session.questionIds]);
  const [answers, setAnswers] = useState<Record<string, string[]>>(session.answers);
  const [index, setIndex] = useState(0);
  const [now, setNow] = useState(Date.now());
  const [saved, setSaved] = useState(true);
  const finishing = useRef(false);
  const left = remainingMs(session.startedAt, session.timeLimitMinutes, now);

  useEffect(() => {
    if (!session.timeLimitMinutes || session.finishedAt) return;
    const t = setInterval(() => setNow(Date.now()), 1000);
    return () => clearInterval(t);
  }, [session.timeLimitMinutes, session.finishedAt]);

  useEffect(() => {
    if (left === 0 && !session.finishedAt) void finish(); // temps écoulé : remise automatique
  }, [left]); // eslint-disable-line react-hooks/exhaustive-deps

  async function choose(q: Question, id: string) {
    const max = q.format === 'true-false' ? 1 : expectedSelectionCount(q.instruction);
    const prev = answers[q.id] ?? [];
    let next: string[];
    if (prev.includes(id)) next = prev.filter((x) => x !== id);
    else if (max === 1) next = [id];
    else if (max !== null && prev.length >= max) next = prev;
    else next = [...prev, id];
    const all = { ...answers, [q.id]: next };
    setAnswers(all);
    setSaved(false);
    await saveSession({ ...session, answers: all }); // sauvegarde continue du brouillon
    setSaved(true);
  }

  async function finish() {
    if (finishing.current || session.finishedAt) return;
    finishing.current = true;
    let ok = 0;
    const at = new Date().toISOString();
    for (const q of qs) {
      const sel = answers[q.id] ?? [];
      const g = grade(q, sel);
      if (g.correct) ok += 1;
      // Une question laissée sans réponse ne compte pas comme travaillée.
      if (sel.length > 0) await record({ id: newId(), questionId: q.id, at, mode: session.mode, selected: sel, correct: g.correct, hintsUsed: 0, durationMs: 0, sessionId: session.id });
    }
    await setDraft(qs.map((q) => q.id), false);
    await saveSession({ ...session, answers, finishedAt: at, score: qs.length ? ok / qs.length : 0 });
  }

  if (session.finishedAt) return <ExamResults session={session} questions={qs} backTo={backTo} title={title} />;
  const q = qs[index];
  const answered = qs.filter((x) => (answers[x.id] ?? []).length > 0).length;
  const choices = q.format === 'true-false' ? [{ id: 'VRAI', text: 'Vrai' }, { id: 'FAUX', text: 'Faux' }] : q.options;
  return (
    <section>
      <div className="exam-bar">
        <span>{title}</span>
        <span>Question {index + 1}/{qs.length} · {answered} répondue(s)</span>
        <span className="saved" role="status">{saved ? '✓ réponses enregistrées' : 'enregistrement…'}</span>
        {left !== null && <span className={left < 5 * 60_000 ? 'clock warn' : 'clock'} role="timer">⏱️ {formatClock(left)}</span>}
      </div>
      <article className="qcard">
        {q.kind === 'archive' && <p className="muted">📜 {SESSION_LABEL[q.provenance.session]} · page {q.provenance.page}</p>}
        <p className="stem">{q.stem}</p>
        <p className="instruction">{q.format === 'true-false' ? 'Vrai ou faux ?' : instructionLabel(q.instruction)}</p>
        <ul className={q.format === 'true-false' ? 'choices tf' : 'choices'} role="list">
          {choices.map((o) => (
            <li key={o.id}>
              <button type="button" className={`choice ${(answers[q.id] ?? []).includes(o.id) ? 'selected' : ''}`} aria-pressed={(answers[q.id] ?? []).includes(o.id)} onClick={() => choose(q, o.id)}>
                {q.format === 'mcq' && <span className="letter">{o.id}</span>}
                <span className="choice-text">{o.text}</span>
              </button>
            </li>
          ))}
        </ul>
      </article>
      <div className="qactions">
        <button className="btn ghost" disabled={index === 0} onClick={() => setIndex((i) => i - 1)}>← Précédente</button>
        {index + 1 < qs.length ? (
          <button className="btn" onClick={() => setIndex((i) => i + 1)}>Suivante →</button>
        ) : (
          <button className="btn" onClick={() => { if (answered === qs.length || window.confirm(`${qs.length - answered} question(s) sans réponse. Terminer quand même ?`)) void finish(); }}>Terminer et voir la correction</button>
        )}
      </div>
      <nav className="exam-grid" aria-label="Aller à la question">
        {qs.map((x, i) => (
          <button key={x.id} className={`dot ${(answers[x.id] ?? []).length ? 'done' : ''} ${i === index ? 'current' : ''}`} onClick={() => setIndex(i)} aria-label={`Question ${i + 1}`}>{i + 1}</button>
        ))}
      </nav>
      <p className="muted">Tes réponses sont enregistrées à chaque clic : tu peux fermer la page et reprendre plus tard{session.timeLimitMinutes ? ' (le chronomètre continue de tourner)' : ''}. Les corrections s’affichent à la fin.</p>
      <button className="btn secondary" onClick={() => void finish()}>Terminer maintenant</button>
    </section>
  );
}

function ExamResults({ session, questions, backTo, title }: { session: SessionRecord; questions: Question[]; backTo: { to: string; label: string }; title: string }) {
  const good = questions.filter((q) => grade(q, session.answers[q.id] ?? []).correct).length;
  return (
    <section>
      <h2>Correction — {title}</h2>
      <p className="score">{good} / {questions.length} ({Math.round((good / Math.max(1, questions.length)) * 100)} %)</p>
      {session.mode === 'final-eval' && (
        <p className="muted">Une évaluation réussie (≥ 75 %) compte pour la maîtrise du cours ; il en faut deux, à des jours différents, avec des questions maîtrisées dans la durée.</p>
      )}
      <ol className="results">
        {questions.map((q) => {
          const sel = session.answers[q.id] ?? [];
          const g = grade(q, sel);
          const label = (ids: string[]) => ids.map((e) => (e === 'VRAI' ? 'Vrai' : e === 'FAUX' ? 'Faux' : e)).join(' et ') || '—';
          return (
            <li key={q.id} className={g.correct ? 'ok' : 'ko'}>
              <p className="stem">{g.correct ? '✅' : sel.length ? '❌' : '⬜'} {q.stem}</p>
              <p>Ta réponse : <strong>{label(sel)}</strong> · Réponse attendue : <strong>{label(q.expected)}</strong></p>
              {q.format === 'mcq' && (
                <ul className="mini-options">
                  {q.options.map((o) => <li key={o.id} className={q.expected.includes(o.id) ? 'exp' : ''}><strong>{o.id}.</strong> {o.text}{'explanation' in o && o.explanation ? <small> — {o.explanation}</small> : null}</li>)}
                </ul>
              )}
              <p className="reliability">{reliabilityMessage(q)}</p>
              {q.explanation && <p className="block block-complement"><span className="block-label">🟨 Explication — à valider</span><br />{q.explanation.text}</p>}
              {q.lessonLinks.slice(0, 1).map((l) => {
                const lesson = lessonById.get(l);
                return lesson ? <Link key={l} to={`/cours/${lesson.chapterId}/lecon/${l}`}>📖 Revoir : {lesson.title}</Link> : null;
              })}
            </li>
          );
        })}
      </ol>
      <Link className="btn" to={backTo.to}>{backTo.label}</Link>
    </section>
  );
}
