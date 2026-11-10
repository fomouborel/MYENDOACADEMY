/**
 * Schémas des DONNÉES PERSONNELLES (progression), stockées en IndexedDB et exportées en JSON.
 * Version de schéma incrémentée à chaque changement incompatible (voir services/storage/migrations).
 */
import { z } from 'zod';

export const PROGRESS_SCHEMA_VERSION = 1;

export const Mode = z.enum(['check', 'training', 'exam-level', 'final-eval', 'mock-exam', 'review', 'archive-bank', 'clinical-case']);
export type Mode = z.infer<typeof Mode>;

/** Une tentative = une réponse VALIDÉE. Afficher une question ne crée aucune tentative. */
export const Attempt = z.object({
  id: z.string(),
  questionId: z.string(),
  at: z.string().datetime(),
  mode: Mode,
  selected: z.array(z.string()),
  /** Texte libre (QROC). */
  freeText: z.string().optional(),
  /** null = non notée (QROC auto-évaluée, réponse d'archive absente…). */
  correct: z.boolean().nullable(),
  hintsUsed: z.number().int().min(0).max(3),
  durationMs: z.number().int().min(0),
  sessionId: z.string().optional(),
});
export type Attempt = z.infer<typeof Attempt>;

export const QuestionStatus = z.enum(['not-started', 'in-progress', 'success', 'failed', 'to-review', 'mastered']);
export type QuestionStatus = z.infer<typeof QuestionStatus>;

/** État calculé et mis en cache par question (recalculable à partir des tentatives). */
export const QuestionState = z.object({
  questionId: z.string(),
  attempts: z.number().int().min(0),
  successes: z.number().int().min(0),
  failures: z.number().int().min(0),
  lastAttemptAt: z.string().datetime().nullable(),
  lastCorrect: z.boolean().nullable(),
  /** Boîte de Leitner 1..5 et prochaine échéance de révision. */
  box: z.number().int().min(0).max(5),
  dueAt: z.string().datetime().nullable(),
  /** Jours distincts où la question a été réussie (maîtrise = stabilité dans le temps). */
  successDays: z.array(z.string()).default([]),
  /** Marquée « à revoir » par l'étudiante. */
  flagged: z.boolean().default(false),
  /** Brouillon dans une session non terminée (examen blanc interrompu, cas clinique). */
  draft: z.boolean().default(false),
});
export type QuestionState = z.infer<typeof QuestionState>;

export const LessonProgress = z.object({
  lessonId: z.string(),
  openedAt: z.string().datetime(),
  completedAt: z.string().datetime().nullable(),
});
export type LessonProgress = z.infer<typeof LessonProgress>;

export const SessionRecord = z.object({
  id: z.string(),
  mode: Mode,
  chapterId: z.string().optional(),
  examSessionId: z.string().optional(),
  questionIds: z.array(z.string()),
  answers: z.record(z.string(), z.array(z.string())),
  startedAt: z.string().datetime(),
  finishedAt: z.string().datetime().nullable(),
  timeLimitMinutes: z.number().int().positive().nullable(),
  score: z.number().min(0).max(1).nullable(),
});
export type SessionRecord = z.infer<typeof SessionRecord>;

export const Backup = z.object({
  app: z.literal('endocrino-academy'),
  schemaVersion: z.number().int().positive(),
  exportedAt: z.string().datetime(),
  data: z.object({
    attempts: z.array(Attempt),
    questionStates: z.array(QuestionState),
    lessons: z.array(LessonProgress),
    sessions: z.array(SessionRecord),
  }),
});
export type Backup = z.infer<typeof Backup>;
