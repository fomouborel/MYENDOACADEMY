/**
 * Règles de cohérence du contenu (méthode § 9, étape 6). Pure : utilisable dans les tests et la CI.
 * Une seule erreur bloque le déploiement.
 */
import { ChaptersFile, ExamsFile, QuestionFile, type Question } from '@/schemas/content';
import { expectedSelectionCount } from '@/services/scoring/score';

export interface RawContent {
  chapters: unknown;
  exams: unknown;
  questionFiles: Record<string, unknown>;
  /** Contenu des leçons, indexé par chemin relatif à content/lessons/. */
  lessons: Record<string, string>;
}

const norm = (s: string) => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]+/g, ' ').trim();

export function validateContent(raw: RawContent): string[] {
  const errors: string[] = [];
  const err = (where: string, msg: string) => errors.push(`${where} : ${msg}`);

  const ch = ChaptersFile.safeParse(raw.chapters);
  if (!ch.success) {
    err('chapters.json', ch.error.issues.map((i) => `${i.path.join('.')} ${i.message}`).join(' ; '));
    return errors;
  }
  const ex = ExamsFile.safeParse(raw.exams);
  if (!ex.success) {
    err('exams.json', ex.error.issues.map((i) => `${i.path.join('.')} ${i.message}`).join(' ; '));
    return errors;
  }
  const chapters = new Map(ch.data.chapters.map((c) => [c.id, c]));
  const sessions = new Set(ex.data.sessions.map((s) => s.id));
  const lessonIds = new Set<string>();

  for (const c of ch.data.chapters) {
    if (new Set(c.subchapters.map((s) => s.id)).size !== c.subchapters.length) err(`chapitre ${c.id}`, 'sous-chapitres en double');
    if (c.status === 'available' && c.lessons.length === 0) err(`chapitre ${c.id}`, 'un chapitre disponible doit avoir au moins une leçon');
    for (const l of c.lessons) {
      if (lessonIds.has(l.id)) err(`leçon ${l.id}`, 'identifiant en double');
      lessonIds.add(l.id);
      for (const s of l.subchapters) if (!c.subchapters.some((x) => x.id === s)) err(`leçon ${l.id}`, `sous-chapitre inconnu « ${s} »`);
      const md = raw.lessons[l.file];
      if (md === undefined) err(`leçon ${l.id}`, `fichier manquant content/lessons/${l.file}`);
      else {
        if (!md.includes(':::archives')) err(`leçon ${l.id}`, 'encadré « :::archives » obligatoire (ce que les archives interrogent)');
        if (!/À retenir/.test(md)) err(`leçon ${l.id}`, 'rubrique « À retenir » obligatoire');
        md.split('\n').forEach((line, i) => {
          // « :mot » est interprété comme une directive Markdown et disparaîtrait à l'affichage.
          if (!line.startsWith(':::') && /(?<![:\\]):[A-Za-z0-9]/.test(line)) {
            err(`leçon ${l.id}`, `ligne ${i + 1} : deux-points collé à un mot ou un chiffre (écrire « \\: » ou ajouter une espace)`);
          }
        });
      }
    }
  }

  const ids = new Set<string>();
  const cases = new Map<string, number[]>();
  for (const [file, content] of Object.entries(raw.questionFiles)) {
    const parsed = QuestionFile.safeParse(content);
    if (!parsed.success) {
      for (const i of parsed.error.issues.slice(0, 20)) err(file, `${i.path.join('.')} ${i.message}`);
      continue;
    }
    for (const q of parsed.data.questions) checkQuestion(q, file);
  }

  function checkQuestion(q: Question, file: string) {
    const w = `${file} › ${q.id}`;
    if (ids.has(q.id)) err(w, 'identifiant en double (jamais réutiliser un identifiant)');
    ids.add(q.id);

    const c = chapters.get(q.chapter);
    if (!c) err(w, `chapitre inconnu « ${q.chapter} »`);
    else if (!c.subchapters.some((s) => s.id === q.subchapter)) err(w, `sous-chapitre inconnu « ${q.subchapter} »`);
    for (const l of q.lessonLinks) if (!lessonIds.has(l)) err(w, `leçon liée inexistante « ${l} »`);

    if (q.kind === 'archive') {
      if (!sessions.has(q.provenance.session)) err(w, `session inconnue « ${q.provenance.session} » (exams.json)`);
      if (!q.id.startsWith(`ENDO-${q.provenance.session}-${q.provenance.discipline}-`)) err(w, 'l’identifiant ne correspond pas à la session/discipline');
      if (q.answerStatus === 'authored') err(w, 'une question d’archives ne peut pas avoir le statut « authored »');
      // Règle pédiatrie (décision phase 1) : thyroïde de l'enfant → hypo/congenitale ; sinon chapitre pédiatrie.
      if (q.provenance.discipline === 'PEDIA') {
        const ok = (q.chapter === 'hypo' && q.subchapter === 'congenitale') || q.chapter === 'pediatrie';
        if (!ok) err(w, 'question pédiatrique hors de « hypo › congenitale » ou du chapitre « pediatrie »');
      }
    } else {
      if (!q.id.startsWith(`ENDO-EX-`)) err(w, 'un exercice créé doit avoir un identifiant ENDO-EX-…');
      if (q.answerStatus !== 'authored') err(w, 'un exercice créé doit avoir le statut « authored »');
      if (!q.explanation) err(w, 'un exercice créé doit avoir une explication');
    }

    const needsNote = ['disputed', 'deduced', 'absent', 'incomplete'].includes(q.answerStatus);
    if (needsNote && !q.answerNote) err(w, `answerNote obligatoire pour le statut « ${q.answerStatus} »`);
    if (q.answerStatus === 'absent' && q.expected.length > 0) err(w, 'statut « absent » mais une réponse attendue est renseignée');
    if (['official', 'proposed', 'disputed', 'deduced', 'authored'].includes(q.answerStatus) && q.format !== 'qroc' && q.expected.length === 0) {
      err(w, `statut « ${q.answerStatus} » sans réponse attendue`);
    }

    if (q.format === 'mcq') {
      if (!q.instruction) err(w, 'consigne (instruction) obligatoire pour un QCM');
      const optIds = q.options.map((o) => o.id);
      if (new Set(optIds).size !== optIds.length) err(w, 'propositions en double');
      for (const e of q.expected) if (!optIds.includes(e)) err(w, `réponse attendue « ${e} » absente des propositions`);
      const n = expectedSelectionCount(q.instruction);
      if (n !== null && q.answerStatus !== 'incomplete' && q.expected.length > 0 && q.expected.length !== n) {
        err(w, `la consigne demande ${n} réponse(s), ${q.expected.length} attendue(s)`);
      }
      if (q.options.length < 3 && q.answerStatus !== 'incomplete') err(w, 'moins de 3 propositions : statut « incomplete » requis');
    }
    if (q.format === 'true-false' && q.expected.some((e) => e !== 'VRAI' && e !== 'FAUX')) err(w, 'vrai/faux : réponse VRAI ou FAUX');
    if (q.format === 'qroc' && !q.qroc) err(w, 'QROC sans grille (mots-clés, réponse modèle)');

    // Les indices ne doivent pas révéler la réponse.
    if (q.hints && q.format === 'mcq') {
      for (const e of q.expected) {
        const t = norm(q.options.find((o) => o.id === e)?.text ?? '');
        if (t.length >= 8 && q.hints.some((h) => norm(h).includes(t))) err(w, `un indice recopie la proposition attendue ${e}`);
      }
      if (q.hints.some((h) => /\b(reponse|proposition) [a-e]\b/.test(norm(h)))) err(w, 'un indice cite une lettre de réponse');
    }
    if (q.explanation?.status === 'validated' && q.explanation.text.trim().length < 20) err(w, 'explication validée trop courte');

    if (q.caseId) {
      if (!q.caseStep) err(w, 'caseId sans caseStep');
      else cases.set(q.caseId, [...(cases.get(q.caseId) ?? []), q.caseStep]);
    }
  }

  for (const [id, steps] of cases) {
    const sorted = [...steps].sort((a, b) => a - b);
    if (sorted.some((s, i) => s !== i + 1)) err(`cas ${id}`, `étapes non continues (${sorted.join(', ')})`);
  }
  return errors;
}
