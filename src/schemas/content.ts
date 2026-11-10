/**
 * Schémas du CONTENU (chapitres, sessions d'examen, questions).
 * Source unique de vérité : utilisés par l'application (types) ET par le validateur
 * `npm run validate:content`. Toute modification ici doit être documentée dans
 * docs/ARCHITECTURE-PHASE-2.md.
 */
import { z } from 'zod';

/* ------------------------------------------------------------------ */
/* Identifiants                                                        */
/* ------------------------------------------------------------------ */

/** Sessions : AAAA-MM (examen daté), ND (compilation 2016-2021 non datée), AP<année> (série spéciale). */
export const SessionId = z.string().regex(/^(\d{4}-\d{2}|ND|AP\d{4})$/, 'session : AAAA-MM, ND ou AP<année>');

export const Discipline = z.enum(['ADULTE', 'PEDIA', 'RADIO', 'ANAPATH', 'PHARMA']);
export type Discipline = z.infer<typeof Discipline>;

/** Type de format dans l'identifiant (méthode § 8). */
export const IdType = z.enum(['QCM', 'QCMM', 'VF', 'QROC', 'CAS', 'EX']);

/**
 * ENDO-<SESSION>-<DISCIPLINE>-<TYPE>-<NNN> pour les questions d'archives,
 * ENDO-EX-<CHAPITRE>-<TYPE>-<NNN> pour les exercices créés (hors archives).
 * NNN n'est JAMAIS réutilisé ni renuméroté (la progression en dépend).
 */
export const QuestionId = z
  .string()
  .regex(
    /^ENDO-((\d{4}-\d{2}|ND|AP\d{4})-(ADULTE|PEDIA|RADIO|ANAPATH|PHARMA)|EX-[a-z]+)-(QCM|QCMM|VF|QROC|CAS|EX)-\d{3}$/,
    'identifiant de question invalide',
  );

/* ------------------------------------------------------------------ */
/* Fiabilité et provenance                                             */
/* ------------------------------------------------------------------ */

/** Statut de correction (prompt § 4.3). Jamais transformé automatiquement en « official ». */
export const AnswerStatus = z.enum([
  'official', //       correction officielle identifiée (aucune à ce jour)
  'proposed', //       réponse proposée dans la compilation (en rouge)
  'disputed', //       réponse discutée ou contestée
  'deduced', //        réponse déduite, à vérifier
  'absent', //         réponse absente
  'incomplete', //     question incomplète (propositions/énoncé manquants)
  'authored', //       exercice créé (hors archives) : correction rédigée, à valider
]);
export type AnswerStatus = z.infer<typeof AnswerStatus>;

/** Statut d'une explication rédigée (provenance visible, méthode § 5.3). */
export const ExplanationStatus = z.enum(['complement', 'validated']);

/** Référence externe : n'est acceptée que si elle a été vérifiée. */
export const SourceRef = z.object({
  label: z.string().min(3),
  url: z.string().url().optional(),
  verifiedOn: z.string().regex(/^\d{4}-\d{2}-\d{2}$/, 'date de vérification AAAA-MM-JJ'),
});

export const Provenance = z.object({
  session: SessionId,
  discipline: Discipline,
  /** Enseignant tel qu'indiqué dans la source ; null si non attribué (jamais deviné). */
  teacher: z.string().nullable(),
  formerTeacher: z.boolean().default(false),
  /** Fichier source et page du PDF. */
  sourceFile: z.string(),
  page: z.number().int().positive(),
  /** Numéro dans la retranscription, si présent. */
  originalNumber: z.number().int().positive().nullable(),
  /** Référence de l'audit phase 1 (docs/audit/*.csv). */
  auditRef: z.string(),
});

/* ------------------------------------------------------------------ */
/* Questions                                                           */
/* ------------------------------------------------------------------ */

/**
 * Consigne de réponse telle que formulée dans l'examen. L'interface adapte le mode de
 * sélection : on demande TOUJOURS à l'étudiante de cocher les propositions qui répondent
 * à la consigne (ex. pour « une fausse », cocher la proposition fausse).
 */
export const Instruction = z.enum([
  'one-correct', //  une seule bonne réponse
  'two-correct', //  deux bonnes réponses
  'one-false', //    une fausse / « sauf une »
  'two-false', //    deux fausses / « sauf deux »
  'one-true', //     une seule vraie
  'all-that-apply', // plusieurs possibles, nombre non annoncé
]);
export type Instruction = z.infer<typeof Instruction>;

export const Option = z.object({
  id: z.string().regex(/^[A-J]$/),
  /** Formulation ORIGINALE conservée. */
  text: z.string().min(1),
  /** Explication propre à la proposition (complément rédigé). */
  explanation: z.string().optional(),
});

export const Explanation = z.object({
  text: z.string().min(1),
  status: ExplanationStatus,
  sources: z.array(SourceRef).default([]),
});

export const QrocKey = z.object({
  keywords: z.array(z.string()).min(1),
  essentials: z.array(z.string()).min(1),
  modelAnswer: z.string(),
  majorErrors: z.array(z.string()).default([]),
  acceptableEquivalents: z.array(z.string()).default([]),
});

/** Valeur biologique affichée avec sa norme ET l'origine de la norme (jamais inventée). */
export const LabValue = z.object({
  analyte: z.string(),
  value: z.string(),
  unit: z.string(),
  reference: z.string().optional(),
  /** « énoncé de l'examen », « laboratoire X », référence vérifiée… */
  referenceOrigin: z.string().optional(),
});

const QuestionBase = z.object({
  id: QuestionId,
  /** archive = question réelle d'un ancien examen ; exercise = exercice créé (affiché comme tel). */
  kind: z.enum(['archive', 'exercise']),
  format: z.enum(['mcq', 'true-false', 'qroc']),
  instruction: Instruction.optional(),
  stem: z.string().min(1),
  /** Tableau de résultats biologiques éventuel. */
  labs: z.array(LabValue).default([]),
  options: z.array(Option).default([]),
  /** Identifiants des propositions à cocher (selon la consigne). Vide si réponse absente. */
  expected: z.array(z.string().regex(/^[A-J]$|^(VRAI|FAUX)$/)).default([]),
  answerStatus: AnswerStatus,
  /** Pourquoi la réponse est discutée / déduite / absente. Obligatoire sauf si « proposed »/« official ». */
  answerNote: z.string().optional(),
  /** Commentaires d'étudiants conservés tels quels (contexte). */
  sourceComments: z.array(z.string()).default([]),

  chapter: z.string(),
  subchapter: z.string(),
  lessonLinks: z.array(z.string()).max(3).default([]),
  tags: z.array(z.string()).default([]),
  difficulty: z.union([z.literal(1), z.literal(2), z.literal(3)]),
  clinical: z.boolean().default(false),
  caseId: z.string().optional(),
  caseStep: z.number().int().positive().optional(),
  duplicateGroup: z.string().optional(),

  hints: z.array(z.string()).length(3).optional(),
  explanation: Explanation.optional(),
  pitfall: z.string().optional(),
  qroc: QrocKey.optional(),
});

export const ArchiveQuestion = QuestionBase.extend({
  kind: z.literal('archive'),
  provenance: Provenance,
});

export const ExerciseQuestion = QuestionBase.extend({
  kind: z.literal('exercise'),
  /** Un exercice créé n'est jamais présenté comme une question d'archives. */
  provenance: z.undefined().optional(),
});

export const Question = z.discriminatedUnion('kind', [ArchiveQuestion, ExerciseQuestion]);
export type Question = z.infer<typeof Question>;
export type ArchiveQuestion = z.infer<typeof ArchiveQuestion>;

export const QuestionFile = z.object({
  source: z.string(),
  questions: z.array(Question),
});

/* ------------------------------------------------------------------ */
/* Chapitres, leçons, sessions                                         */
/* ------------------------------------------------------------------ */

export const Lesson = z.object({
  id: z.string().regex(/^[a-z]+-[a-z0-9-]+$/),
  title: z.string(),
  /** Chemin relatif à content/lessons/. */
  file: z.string().regex(/^[a-z]+\/\d{2}-[a-z0-9-]+\.md$/),
  subchapters: z.array(z.string()).min(1),
  minutes: z.number().int().min(3).max(30),
});

export const Chapter = z.object({
  id: z.string().regex(/^[a-z]+$/),
  order: z.number().int().positive(),
  domain: z.string(),
  title: z.string(),
  short: z.string(),
  icon: z.string(),
  status: z.enum(['available', 'pending']),
  subchapters: z.array(z.object({ id: z.string().regex(/^[a-z-]+$/), title: z.string() })).min(1),
  lessons: z.array(Lesson).default([]),
});
export type Chapter = z.infer<typeof Chapter>;

export const ChaptersFile = z.object({ chapters: z.array(Chapter) });

export const ExamSession = z.object({
  id: SessionId,
  label: z.string(),
  sourceFile: z.string(),
  durationMinutes: z.number().int().positive().nullable(),
  /** Composition ANNONCÉE dans la source, null si inconnue (jamais inventée). */
  announcedComposition: z
    .array(z.object({ part: z.string(), teachers: z.array(z.string()), count: z.number().int().positive() }))
    .nullable(),
  announcedTotal: z.number().int().positive().nullable(),
  notTranscribedCount: z.number().int().min(0),
  notes: z.array(z.string()).default([]),
});
export const ExamsFile = z.object({ sessions: z.array(ExamSession) });
export type ExamSession = z.infer<typeof ExamSession>;
