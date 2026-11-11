import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { openChapters, questions } from '@/data/content';
import { useProgress } from '@/state/ProgressContext';
import { selectQuestions, type QuizFilters } from '@/features/quizzes/select';

export function TrainingPage() {
  const nav = useNavigate();
  const { states } = useProgress();
  const [chs, setChs] = useState<string[]>(openChapters.map((c) => c.id));
  const [audience, setAudience] = useState<QuizFilters['audience']>('all');
  const [status, setStatus] = useState<QuizFilters['status']>('all');
  const [kind, setKind] = useState<QuizFilters['kind']>('all');
  const [n, setN] = useState(10);
  const available = selectQuestions(questions, { mode: 'free', chapters: chs, audience, status, kind }, states, new Date()).length;

  function start() {
    const q = new URLSearchParams({ mode: 'free', chapter: chs.join(','), audience: audience!, status: status!, kind: kind!, n: String(n), seed: String(Date.now() % 100000) });
    nav(`/quiz?${q}`);
  }

  return (
    <section>
      <h1>Entraînement</h1>
      <p className="lead">Compose ta série de questions. Les questions déjà réussies ne disparaissent jamais : tu peux les refaire autant que tu veux.</p>
      <fieldset className="filters">
        <legend>Cours</legend>
        {openChapters.map((c) => (
          <label key={c.id} className="check">
            <input type="checkbox" checked={chs.includes(c.id)} onChange={(e) => setChs((x) => (e.target.checked ? [...x, c.id] : x.filter((y) => y !== c.id)))} /> {c.icon} {c.title}
          </label>
        ))}
      </fieldset>
      <div className="filters grid">
        <label>Public
          <select value={audience} onChange={(e) => setAudience(e.target.value as QuizFilters['audience'])}>
            <option value="all">Adulte et pédiatrie</option><option value="adulte">Adulte</option><option value="pediatrie">Pédiatrie</option>
          </select>
        </label>
        <label>Questions
          <select value={status} onChange={(e) => setStatus(e.target.value as QuizFilters['status'])}>
            <option value="all">Toutes</option><option value="not-started">Jamais faites</option><option value="failed">Échouées</option><option value="to-review">À revoir</option>
          </select>
        </label>
        <label>Type
          <select value={kind} onChange={(e) => setKind(e.target.value as QuizFilters['kind'])}>
            <option value="all">Archives et exercices</option><option value="archive">Anciens examens uniquement</option><option value="exercise">Exercices uniquement</option>
          </select>
        </label>
        <label>Nombre
          <select value={n} onChange={(e) => setN(Number(e.target.value))}>
            {[5, 10, 20, 50].map((x) => <option key={x} value={x}>{x}</option>)}
          </select>
        </label>
      </div>
      <p>{available} question(s) disponible(s) avec ces critères.</p>
      <button className="btn" disabled={available === 0 || chs.length === 0} onClick={start}>Commencer la série</button>
    </section>
  );
}
