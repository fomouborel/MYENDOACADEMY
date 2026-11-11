/**
 * Stockage local (IndexedDB) — sauvegarde automatique : chaque action est écrite immédiatement.
 * Aucune donnée ne quitte l'appareil. Les données ne sont PAS synchronisées entre appareils :
 * l'export / import JSON sert à les transférer ou à les sauvegarder.
 */
import { openDB, type DBSchema, type IDBPDatabase } from 'idb';
import type { Attempt, LessonProgress, QuestionState, SessionRecord } from '@/schemas/progress';
import { PROGRESS_SCHEMA_VERSION } from '@/schemas/progress';
import { applyAttempt, emptyState } from '@/services/progress/questionState';

export const DB_NAME = 'endocrino-academy';

interface EndoDB extends DBSchema {
  attempts: { key: string; value: Attempt; indexes: { byQuestion: string; byDate: string } };
  questionStates: { key: string; value: QuestionState };
  lessons: { key: string; value: LessonProgress };
  sessions: { key: string; value: SessionRecord };
  meta: { key: string; value: { key: string; value: unknown } };
}

let dbPromise: Promise<IDBPDatabase<EndoDB>> | null = null;

export function getDb(): Promise<IDBPDatabase<EndoDB>> {
  dbPromise ??= openDB<EndoDB>(DB_NAME, PROGRESS_SCHEMA_VERSION, {
    upgrade(db, oldVersion) {
      // Migrations successives : ne jamais supprimer de données de progression.
      if (oldVersion < 1) {
        const attempts = db.createObjectStore('attempts', { keyPath: 'id' });
        attempts.createIndex('byQuestion', 'questionId');
        attempts.createIndex('byDate', 'at');
        db.createObjectStore('questionStates', { keyPath: 'questionId' });
        db.createObjectStore('lessons', { keyPath: 'lessonId' });
        db.createObjectStore('sessions', { keyPath: 'id' });
        db.createObjectStore('meta', { keyPath: 'key' });
      }
    },
  });
  return dbPromise;
}

/** Pour les tests : ferme et oublie la connexion. */
export async function resetDbConnection(): Promise<void> {
  if (dbPromise) (await dbPromise).close();
  dbPromise = null;
}

/** Demande au navigateur de ne pas effacer les données en cas de manque d'espace. */
export async function requestPersistentStorage(): Promise<boolean> {
  if (typeof navigator !== 'undefined' && navigator.storage?.persist) {
    return navigator.storage.persist();
  }
  return false;
}

export function newId(): string {
  return typeof crypto !== 'undefined' && 'randomUUID' in crypto
    ? crypto.randomUUID()
    : `${Date.now()}-${Math.random().toString(36).slice(2)}`;
}

/** Enregistre une tentative validée et met à jour l'état de la question dans la même transaction. */
export async function recordAttempt(attempt: Attempt): Promise<QuestionState> {
  const db = await getDb();
  const tx = db.transaction(['attempts', 'questionStates'], 'readwrite');
  await tx.objectStore('attempts').put(attempt);
  const store = tx.objectStore('questionStates');
  const prev = (await store.get(attempt.questionId)) ?? emptyState(attempt.questionId);
  const next = applyAttempt(prev, attempt);
  await store.put(next);
  await tx.done;
  return next;
}

export async function setFlag(questionId: string, flagged: boolean): Promise<void> {
  const db = await getDb();
  const prev = (await db.get('questionStates', questionId)) ?? emptyState(questionId);
  await db.put('questionStates', { ...prev, flagged });
}

export async function setDraft(questionIds: string[], draft: boolean): Promise<void> {
  const db = await getDb();
  const tx = db.transaction('questionStates', 'readwrite');
  for (const id of questionIds) {
    const prev = (await tx.store.get(id)) ?? emptyState(id);
    await tx.store.put({ ...prev, draft });
  }
  await tx.done;
}

export async function getStates(): Promise<Map<string, QuestionState>> {
  const db = await getDb();
  const all = await db.getAll('questionStates');
  return new Map(all.map((s) => [s.questionId, s]));
}

export async function getAttempts(questionId?: string): Promise<Attempt[]> {
  const db = await getDb();
  return questionId ? db.getAllFromIndex('attempts', 'byQuestion', questionId) : db.getAll('attempts');
}

export async function saveSession(s: SessionRecord): Promise<void> {
  const db = await getDb();
  await db.put('sessions', s);
}

export async function getSessions(): Promise<SessionRecord[]> {
  const db = await getDb();
  return db.getAll('sessions');
}

export async function markLesson(lessonId: string, completed: boolean): Promise<void> {
  const db = await getDb();
  const now = new Date().toISOString();
  const prev = await db.get('lessons', lessonId);
  await db.put('lessons', { lessonId, openedAt: prev?.openedAt ?? now, completedAt: completed ? now : (prev?.completedAt ?? null) });
}

export async function getLessons(): Promise<LessonProgress[]> {
  const db = await getDb();
  return db.getAll('lessons');
}

export async function getMeta<T = unknown>(key: string): Promise<T | undefined> {
  const db = await getDb();
  return (await db.get('meta', key))?.value as T | undefined;
}

export async function setMeta(key: string, value: unknown): Promise<void> {
  const db = await getDb();
  await db.put('meta', { key, value });
}
