import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { SESSION_LABEL, chapterById, examSessions, integratedDomainsLabel, openChapters, questions } from '@/data/content';
import { useProgress } from '@/state/ProgressContext';
import { buildMockExam, type MockConfig } from '@/features/exams/mockExam';
import { archiveQuestions } from '@/features/exams/archiveFilters';
import { newId } from '@/services/storage/db';

export function MockExamsPage() {
  const nav = useNavigate();
  const { sessions, saveSession, setDraft } = useProgress();
  const [source, setSource] = useState<MockConfig['source']>('mix');
  const [session, setSession] = useState(examSessions[0]?.id ?? '');
  const teachers = [...new Set(archiveQuestions(questions).map((q) => q.provenance.teacher ?? 'non attribué'))].sort();
  const [teacher, setTeacher] = useState(teachers[0]);
  const [chs, setChs] = useState(openChapters.map((c) => c.id));
  const [count, setCount] = useState(20);
  const [minutes, setMinutes] = useState(30);
  const config: MockConfig = { source, session, teacher, chapters: chs, count, minutes, seed: 1 };
  const preview = buildMockExam(questions, config);
  const info = examSessions.find((s) => s.id === session);

  async function start() {
    const qs = buildMockExam(questions, { ...config, seed: Date.now() % 100000 });
    const rec = { id: newId(), mode: 'mock-exam' as const, examSessionId: source === 'session' ? session : undefined, questionIds: qs.map((q) => q.id), answers: {}, startedAt: new Date().toISOString(), finishedAt: null, timeLimitMinutes: minutes || null, score: null };
    await saveSession(rec);
    await setDraft(rec.questionIds, true);
    nav(`/session/${rec.id}`);
  }

  const mine = sessions.filter((s) => s.mode === 'mock-exam' || s.mode === 'final-eval').sort((a, b) => b.startedAt.localeCompare(a.startedAt));
  return (
    <section>
      <h1>Examens blancs</h1>
      <p className="lead">Compose un examen à partir des vraies questions des anciens examens ({integratedDomainsLabel} pour l’instant). Pas de correction pendant l’examen : tout s’affiche à la fin.</p>
      <div className="filters grid">
        <label>Composer à partir de
          <select value={source} onChange={(e) => setSource(e.target.value as MockConfig['source'])}>
            <option value="mix">Mélange des cours disponibles</option>
            <option value="session">Une année / session</option>
            <option value="teacher">Un professeur</option>
          </select>
        </label>
        {source === 'session' && (
          <label>Session
            <select value={session} onChange={(e) => setSession(e.target.value)}>{examSessions.map((s) => <option key={s.id} value={s.id}>{s.label}</option>)}</select>
          </label>
        )}
        {source === 'teacher' && (
          <label>Professeur
            <select value={teacher} onChange={(e) => setTeacher(e.target.value)}>{teachers.map((t) => <option key={t} value={t}>{t}</option>)}</select>
          </label>
        )}
        <label>Nombre de questions
          <select value={count} onChange={(e) => setCount(Number(e.target.value))}>{[10, 20, 30, 50, 80].map((n) => <option key={n} value={n}>{n}</option>)}</select>
        </label>
        <label>Durée
          <select value={minutes} onChange={(e) => setMinutes(Number(e.target.value))}>
            <option value={0}>Sans chronomètre</option>{[15, 30, 45, 60, 90, 120].map((m) => <option key={m} value={m}>{m} min</option>)}
          </select>
        </label>
      </div>
      {source === 'mix' && (
        <fieldset className="filters">
          <legend>Cours inclus</legend>
          {openChapters.map((c) => (
            <label key={c.id} className="check"><input type="checkbox" checked={chs.includes(c.id)} onChange={(e) => setChs((x) => (e.target.checked ? [...x, c.id] : x.filter((y) => y !== c.id)))} /> {c.icon} {c.title}</label>
          ))}
        </fieldset>
      )}
      {source === 'session' && info && (
        <div className="notice warn">
          <strong>{info.label}</strong> : {info.announcedComposition ? `composition annoncée ${info.announcedTotal} questions (${info.announcedComposition.map((p) => `${p.part} ${p.count}`).join(', ')})` : 'composition non indiquée dans la source'}.
          {' '}Cet examen blanc ne contient que les questions disponibles de cette session ({integratedDomainsLabel}), dans leur ordre d’origine : ce n’est <strong>pas</strong> la reproduction complète de l’examen officiel.
        </div>
      )}
      <p>{preview.length} question(s) seront proposées{preview.length < count ? ` (toutes celles disponibles avec ces critères)` : ''}.</p>
      <button className="btn" disabled={preview.length === 0} onClick={start}>Commencer l’examen blanc</button>

      {mine.length > 0 && (
        <>
          <h2>Mes examens et évaluations</h2>
          <ul className="archive-list">
            {mine.map((s) => (
              <li key={s.id}>
                <Link className="archive-item" to={`/session/${s.id}`}>
                  <span className="archive-meta">{new Date(s.startedAt).toLocaleString('fr-BE')} · {s.mode === 'final-eval' ? `Évaluation finale — ${chapterById.get(s.chapterId ?? '')?.title ?? ''}` : s.examSessionId ? `Examen blanc — ${SESSION_LABEL[s.examSessionId]}` : 'Examen blanc'}</span>
                  <span className="archive-stem">{s.finishedAt ? `Score : ${Math.round((s.score ?? 0) * 100)} % · ${s.questionIds.length} questions` : `En cours — ${Object.values(s.answers).filter((a) => a.length).length}/${s.questionIds.length} répondues · reprendre`}</span>
                </Link>
              </li>
            ))}
          </ul>
        </>
      )}
    </section>
  );
}
