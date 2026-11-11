/** Une question : consigne adaptée, indices progressifs, validation, correction détaillée et fiable. */
import { useEffect, useRef, useState } from 'react';
import { Link } from 'react-router-dom';
import type { Question } from '@/schemas/content';
import { DISCIPLINE_LABEL, SESSION_LABEL, lessonById } from '@/data/content';
import { expectedSelectionCount, grade, instructionLabel, reliabilityMessage, type Grade } from '@/services/scoring/score';
import { audienceOf } from '@/utils/audience';
import { newId } from '@/services/storage/db';
import { useProgress } from '@/state/ProgressContext';
import type { Mode } from '@/schemas/progress';

const VERDICT_LABEL = {
  'expected-selected': '✔ attendue, cochée',
  'expected-missed': '✘ attendue, non cochée',
  'wrongly-selected': '✘ cochée à tort',
  'correctly-ignored': '',
} as const;

const STATUS_BADGE: Record<string, string> = {
  official: 'Correction officielle',
  proposed: 'Réponse proposée (compilation)',
  disputed: 'Réponse discutée',
  deduced: 'Réponse déduite',
  absent: 'Réponse absente',
  incomplete: 'Question incomplète',
  authored: 'Exercice créé — à valider',
};

interface Props {
  question: Question;
  mode: Mode;
  hintsEnabled: boolean;
  sessionId?: string;
  onAnswered?: (correct: boolean | null) => void;
}

export function QuestionCard({ question: q, mode, hintsEnabled, sessionId, onAnswered }: Props) {
  const { record, flag, states } = useProgress();
  const [selected, setSelected] = useState<string[]>([]);
  const [hints, setHints] = useState(0);
  const [result, setResult] = useState<Grade | null>(null);
  const [saving, setSaving] = useState(false);
  const started = useRef(Date.now());
  const max = q.format === 'true-false' ? 1 : expectedSelectionCount(q.instruction);
  const flagged = states.get(q.id)?.flagged ?? false;

  useEffect(() => {
    setSelected([]);
    setHints(0);
    setResult(null);
    setSaving(false);
    started.current = Date.now();
  }, [q.id]);

  function toggle(id: string) {
    if (result) return;
    setSelected((prev) => {
      if (prev.includes(id)) return prev.filter((x) => x !== id);
      if (max === 1) return [id];
      if (max !== null && prev.length >= max) return prev;
      return [...prev, id];
    });
  }

  async function validate() {
    if (saving) return;
    setSaving(true);
    const g = grade(q, selected);
    // Enregistrer AVANT d'afficher la correction : une réponse affichée comme corrigée est toujours sauvegardée.
    await record({
      id: newId(),
      questionId: q.id,
      at: new Date().toISOString(),
      mode,
      selected,
      correct: g.correct,
      hintsUsed: hints,
      durationMs: Date.now() - started.current,
      sessionId,
    });
    setResult(g);
    setSaving(false);
    onAnswered?.(g.correct);
  }

  const choices = q.format === 'true-false' ? [{ id: 'VRAI', text: 'Vrai' }, { id: 'FAUX', text: 'Faux' }] : q.options;
  const needed = max ?? 1;
  const canValidate = !result && !saving && selected.length > 0 && (max === null || selected.length === needed);

  return (
    <article className="qcard" aria-labelledby={`stem-${q.id}`}>
      <header className="qmeta">
        {q.kind === 'archive' ? (
          <span className="tag tag-archive">
            📜 Ancien examen · {SESSION_LABEL[q.provenance.session] ?? q.provenance.session} · {DISCIPLINE_LABEL[q.provenance.discipline]}
            {q.provenance.teacher ? ` · ${q.provenance.teacher}${q.provenance.formerTeacher ? ' (ancien titulaire)' : ''}` : ''}
          </span>
        ) : (
          <span className="tag tag-exercise">✏️ Exercice d’entraînement (hors archives)</span>
        )}
        {audienceOf(q) === 'pediatrie' && <span className="tag">👶 Pédiatrie</span>}
        {q.clinical && <span className="tag">🩺 Cas clinique</span>}
      </header>

      <p id={`stem-${q.id}`} className="stem">{q.stem}</p>

      {q.labs.length > 0 && (
        <div className="table-wrap">
          <table className="labs">
            <thead><tr><th>Analyse</th><th>Résultat</th><th>Norme</th></tr></thead>
            <tbody>
              {q.labs.map((l) => (
                <tr key={l.analyte}>
                  <td>{l.analyte}</td>
                  <td>{l.value} {l.unit}</td>
                  <td>{l.reference ?? '—'}{l.referenceOrigin ? <small> ({l.referenceOrigin})</small> : null}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      <p className="instruction">{q.format === 'true-false' ? 'Cette affirmation est-elle vraie ou fausse ?' : instructionLabel(q.instruction)}</p>

      <ul className={q.format === 'true-false' ? 'choices tf' : 'choices'} role="list">
        {choices.map((o) => {
          const v = result?.perOption[o.id];
          const cls = ['choice', selected.includes(o.id) ? 'selected' : '', v ? `v-${v}` : ''].join(' ');
          return (
            <li key={o.id}>
              <button type="button" className={cls} aria-pressed={selected.includes(o.id)} onClick={() => toggle(o.id)} disabled={Boolean(result)}>
                {q.format === 'mcq' && <span className="letter">{o.id}</span>}
                <span className="choice-text">{o.text}</span>
              </button>
              {result && (
                <div className="choice-feedback">
                  {v && VERDICT_LABEL[v] && <strong>{VERDICT_LABEL[v]}</strong>}
                  {'explanation' in o && o.explanation ? <span> {o.explanation}</span> : null}
                </div>
              )}
            </li>
          );
        })}
      </ul>

      {!result && (
        <div className="qactions">
          {hintsEnabled && q.hints && hints < 3 && (
            <button type="button" className="btn ghost" onClick={() => setHints((h) => h + 1)}>
              💡 {hints === 0 ? 'Afficher un indice' : 'Indice suivant'} ({hints}/3)
            </button>
          )}
          <button type="button" className="btn" onClick={validate} disabled={!canValidate}>
            Valider ma réponse
          </button>
        </div>
      )}
      {max !== null && max > 1 && !result && <p className="muted">Sélectionne {max} propositions.</p>}

      {hints > 0 && q.hints && (
        <ol className="hints">
          {q.hints.slice(0, hints).map((h, i) => (
            <li key={i}><strong>Indice {i + 1} :</strong> {h}</li>
          ))}
        </ol>
      )}

      {result && (
        <section className={`feedback ${result.correct ? 'ok' : result.correct === false ? 'ko' : ''}`} aria-live="polite">
          <p className="verdict">{result.correct ? '✅ Bonne réponse' : result.correct === false ? '❌ Ce n’est pas la réponse attendue' : 'Réponse enregistrée'}</p>
          <p className="expected">
            Réponse attendue : <strong>{q.expected.map((e) => (e === 'VRAI' ? 'Vrai' : e === 'FAUX' ? 'Faux' : e)).join(' et ')}</strong>
            <span className={`badge status-${q.answerStatus}`}>{STATUS_BADGE[q.answerStatus]}</span>
          </p>
          <p className="reliability">{reliabilityMessage(q)}</p>
          {q.answerNote && <p className="reliability">⚠️ {q.answerNote}</p>}
          {q.explanation && (
            <div className={`block block-${q.explanation.status === 'validated' ? 'validated' : 'complement'}`}>
              <p className="block-label">{q.explanation.status === 'validated' ? '🟩 Explication — validée' : '🟨 Explication — à valider'}</p>
              <p>{q.explanation.text}</p>
            </div>
          )}
          {q.pitfall && <p className="pitfall">🪤 <strong>Piège à éviter :</strong> {q.pitfall}</p>}
          {q.sourceComments.length > 0 && <p className="muted">Note de la compilation : {q.sourceComments.join(' · ')}</p>}
          {q.kind === 'archive' && <p className="muted">Source : {q.provenance.sourceFile}, page {q.provenance.page}.</p>}
          <div className="qactions">
            {q.lessonLinks.map((l) => {
              const lesson = lessonById.get(l);
              return lesson ? (
                <Link key={l} className="btn ghost" to={`/cours/${lesson.chapterId}/lecon/${l}`}>📖 Revoir : {lesson.title}</Link>
              ) : null;
            })}
            <button type="button" className="btn ghost" onClick={() => flag(q.id, !flagged)}>
              {flagged ? '★ Retirer de « à revoir »' : '☆ Marquer « à revoir »'}
            </button>
          </div>
        </section>
      )}
    </article>
  );
}
