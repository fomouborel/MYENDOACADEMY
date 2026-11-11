import { useMemo } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import { DISCIPLINE_LABEL, SESSION_LABEL, chapterById, examSessions, openChapters, questions } from '@/data/content';
import { useProgress } from '@/state/ProgressContext';
import { archiveQuestions, filterArchives, sortArchives, type ArchiveFilter } from '@/features/exams/archiveFilters';
import { isPlayable } from '@/services/scoring/score';
import { STATUS_LABEL, statusOf } from '@/services/progress/questionState';

const RELIABILITY: Record<string, string> = {
  official: 'Correction officielle',
  proposed: 'Réponse proposée',
  disputed: 'Réponse discutée',
  deduced: 'Réponse déduite',
  absent: 'Sans réponse',
  incomplete: 'Incomplète',
};
const INSTRUCTIONS: Record<string, string> = {
  'one-correct': 'Une bonne réponse',
  'two-correct': 'Deux bonnes réponses',
  'one-false': 'Une fausse / « sauf »',
  'two-false': 'Deux fausses',
  'one-true': 'Une seule vraie',
};
const KEYS: (keyof ArchiveFilter)[] = ['session', 'discipline', 'teacher', 'chapter', 'subchapter', 'instruction', 'difficulty', 'status', 'reliability', 'audience', 'playable', 'text'];

export function ArchivesPage() {
  const [params, setParams] = useSearchParams();
  const { states } = useProgress();
  const f = Object.fromEntries(KEYS.map((k) => [k, params.get(k) ?? ''])) as ArchiveFilter;
  const all = archiveQuestions(questions);
  const now = new Date();
  const list = useMemo(() => sortArchives(filterArchives(questions, f, states, now)), [params.toString(), states]); // eslint-disable-line react-hooks/exhaustive-deps
  const teachers = [...new Set(all.map((q) => q.provenance.teacher ?? 'non attribué'))].sort();
  const set = (k: keyof ArchiveFilter, v: string) => {
    const p = new URLSearchParams(params);
    if (v) p.set(k, v); else p.delete(k);
    if (k === 'chapter') p.delete('subchapter');
    setParams(p, { replace: true });
  };
  const session = f.session ? examSessions.find((s) => s.id === f.session) : undefined;
  const chapter = f.chapter ? chapterById.get(f.chapter) : undefined;
  const playable = list.filter(isPlayable).length;
  const practiceIds = list.filter(isPlayable).map((q) => q.id);

  return (
    <section>
      <h1>Anciens examens</h1>
      <p className="lead">Toutes les questions de thyroïde retrouvées dans les retranscriptions (2016 à 2026), avec leur provenance et la fiabilité de leur correction. Les autres domaines seront ajoutés ensuite.</p>

      <div className="filters grid">
        <label>Année / session
          <select value={f.session} onChange={(e) => set('session', e.target.value)}>
            <option value="">Toutes</option>
            {examSessions.map((s) => <option key={s.id} value={s.id}>{s.label}</option>)}
          </select>
        </label>
        <label>Discipline
          <select value={f.discipline} onChange={(e) => set('discipline', e.target.value)}>
            <option value="">Toutes</option>
            {Object.entries(DISCIPLINE_LABEL).map(([k, v]) => <option key={k} value={k}>{v}</option>)}
          </select>
        </label>
        <label>Professeur
          <select value={f.teacher} onChange={(e) => set('teacher', e.target.value)}>
            <option value="">Tous</option>
            {teachers.map((t) => <option key={t} value={t}>{t === 'Beauloye' ? 'Beauloye (ancien titulaire)' : t}</option>)}
          </select>
        </label>
        <label>Chapitre
          <select value={f.chapter} onChange={(e) => set('chapter', e.target.value)}>
            <option value="">Tous</option>
            {openChapters.map((c) => <option key={c.id} value={c.id}>{c.title}</option>)}
          </select>
        </label>
        <label>Sous-chapitre
          <select value={f.subchapter} onChange={(e) => set('subchapter', e.target.value)} disabled={!chapter}>
            <option value="">{chapter ? 'Tous' : 'Choisir un chapitre'}</option>
            {chapter?.subchapters.map((s) => <option key={s.id} value={s.id}>{s.title}</option>)}
          </select>
        </label>
        <label>Type de question
          <select value={f.instruction} onChange={(e) => set('instruction', e.target.value)}>
            <option value="">Tous</option>
            {Object.entries(INSTRUCTIONS).map(([k, v]) => <option key={k} value={k}>{v}</option>)}
          </select>
        </label>
        <label>Difficulté
          <select value={f.difficulty} onChange={(e) => set('difficulty', e.target.value)}>
            <option value="">Toutes</option><option value="2">Standard</option><option value="3">Cas clinique / avancée</option>
          </select>
        </label>
        <label>Mon statut
          <select value={f.status} onChange={(e) => set('status', e.target.value)}>
            <option value="">Tous</option>
            {Object.entries(STATUS_LABEL).map(([k, v]) => <option key={k} value={k}>{v}</option>)}
          </select>
        </label>
        <label>Fiabilité de la correction
          <select value={f.reliability} onChange={(e) => set('reliability', e.target.value)}>
            <option value="">Toutes</option>
            {Object.entries(RELIABILITY).map(([k, v]) => <option key={k} value={k}>{v}</option>)}
          </select>
        </label>
        <label>Public
          <select value={f.audience} onChange={(e) => set('audience', e.target.value)}>
            <option value="">Adulte et pédiatrie</option><option value="adulte">Adulte</option><option value="pediatrie">Pédiatrie</option>
          </select>
        </label>
        <label>Recherche
          <input type="search" value={f.text} placeholder="ex. Quervain, amiodarone…" onChange={(e) => set('text', e.target.value)} />
        </label>
      </div>

      {session && (
        <div className="notice">
          <strong>{session.label}</strong>
          {session.durationMinutes ? ` · durée ${Math.round(session.durationMinutes / 60)} h` : ''}
          {session.announcedComposition ? (
            <> · composition annoncée : {session.announcedComposition.map((p) => `${p.part} ${p.count}`).join(', ')} (total {session.announcedTotal}).</>
          ) : (
            <> · composition non indiquée dans la source.</>
          )}
          {session.notTranscribedCount > 0 && <> {session.notTranscribedCount} question(s) de cette session n’ont pas été retranscrites.</>}
          <br /><small>Seules les questions de thyroïde sont intégrées pour l’instant : la session n’est pas complète.</small>
        </div>
      )}

      <p>
        <strong>{list.length}</strong> question(s) · {playable} notée(s) · {list.length - playable} consultable(s) seulement
        {params.toString() && <> · <button className="linklike" onClick={() => setParams({}, { replace: true })}>effacer les filtres</button></>}
      </p>
      {practiceIds.length > 0 && (
        <Link className="btn" to={`/quiz?mode=free&ids=${practiceIds.slice(0, 50).join(',')}`}>🎯 Travailler ces questions ({Math.min(50, practiceIds.length)})</Link>
      )}

      <ul className="archive-list">
        {list.map((q) => {
          const st = statusOf(states.get(q.id), now);
          return (
            <li key={q.id}>
              <Link to={`/examens/${q.id}`} className="archive-item">
                <span className="archive-meta">
                  {SESSION_LABEL[q.provenance.session]} · {DISCIPLINE_LABEL[q.provenance.discipline]}
                  {q.provenance.teacher ? ` · ${q.provenance.teacher}` : ''} · p. {q.provenance.page}
                  {q.provenance.originalNumber ? ` · Q${q.provenance.originalNumber}` : ''}
                </span>
                <span className="archive-stem">{q.stem}</span>
                <span className="archive-badges">
                  <span className={`badge status-${q.answerStatus}`}>{RELIABILITY[q.answerStatus]}</span>
                  {!isPlayable(q) && <span className="badge">Consultable seulement</span>}
                  {st !== 'not-started' && <span className="badge">{STATUS_LABEL[st]}</span>}
                  <span className="badge">{chapterById.get(q.chapter)?.title}</span>
                  {q.provenance.discipline === 'PEDIA' && <span className="badge">👶 Pédiatrie</span>}
                </span>
              </Link>
            </li>
          );
        })}
      </ul>
    </section>
  );
}
