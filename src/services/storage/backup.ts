/**
 * Exportation / importation de la progression (fichier JSON).
 * Import « replace » : remplace tout. Import « merge » : ajoute les tentatives absentes,
 * puis recalcule les états à partir de l'historique fusionné (aucune tentative perdue).
 */
import { Backup, PROGRESS_SCHEMA_VERSION, type Backup as BackupT } from '@/schemas/progress';
import { rebuildState } from '@/services/progress/questionState';
import { getDb, setMeta } from './db';

export async function exportBackup(now = new Date()): Promise<BackupT> {
  const db = await getDb();
  return {
    app: 'endocrino-academy',
    schemaVersion: PROGRESS_SCHEMA_VERSION,
    exportedAt: now.toISOString(),
    data: {
      attempts: await db.getAll('attempts'),
      questionStates: await db.getAll('questionStates'),
      lessons: await db.getAll('lessons'),
      sessions: await db.getAll('sessions'),
    },
  };
}

/** À appeler après un téléchargement réussi : sert au rappel de sauvegarde. */
export async function markExported(now = new Date()): Promise<void> {
  await setMeta('lastExportAt', now.toISOString());
}

export function backupFileName(now = new Date()): string {
  return `endocrino-academy-sauvegarde-${now.toISOString().slice(0, 10)}.json`;
}

export class BackupError extends Error {}

/** Vérifie un fichier de sauvegarde ; message en français, sans jargon. */
export function parseBackup(text: string): BackupT {
  let raw: unknown;
  try {
    raw = JSON.parse(text);
  } catch {
    throw new BackupError('Ce fichier n’est pas une sauvegarde lisible (format JSON attendu).');
  }
  const r = Backup.safeParse(raw);
  if (!r.success) throw new BackupError('Ce fichier ne ressemble pas à une sauvegarde ENDOCRINO ACADEMY.');
  if (r.data.schemaVersion > PROGRESS_SCHEMA_VERSION) {
    throw new BackupError('Cette sauvegarde vient d’une version plus récente de l’application. Rechargez la page puis réessayez.');
  }
  return r.data;
}

export interface ImportReport {
  attemptsAdded: number;
  questionsUpdated: number;
}

export async function importBackup(b: BackupT, mode: 'replace' | 'merge'): Promise<ImportReport> {
  const db = await getDb();
  const tx = db.transaction(['attempts', 'questionStates', 'lessons', 'sessions'], 'readwrite');
  const attempts = tx.objectStore('attempts');
  const states = tx.objectStore('questionStates');
  if (mode === 'replace') {
    await Promise.all([attempts.clear(), states.clear(), tx.objectStore('lessons').clear(), tx.objectStore('sessions').clear()]);
  }
  let added = 0;
  for (const a of b.data.attempts) {
    if (mode === 'merge' && (await attempts.get(a.id))) continue;
    await attempts.put(a);
    added += 1;
  }
  for (const l of b.data.lessons) {
    const prev = mode === 'merge' ? await tx.objectStore('lessons').get(l.lessonId) : undefined;
    await tx.objectStore('lessons').put(prev?.completedAt && !l.completedAt ? prev : l);
  }
  for (const s of b.data.sessions) await tx.objectStore('sessions').put(s);

  // États recalculés depuis l'historique : cohérence garantie.
  const allAttempts = await attempts.getAll();
  const flags = new Map<string, boolean>();
  for (const s of [...(mode === 'merge' ? await states.getAll() : []), ...b.data.questionStates]) {
    flags.set(s.questionId, (flags.get(s.questionId) ?? false) || s.flagged);
  }
  const ids = new Set([...allAttempts.map((a) => a.questionId), ...flags.keys()]);
  for (const id of ids) await states.put(rebuildState(id, allAttempts, flags.get(id) ?? false));
  await tx.done;
  return { attemptsAdded: added, questionsUpdated: ids.size };
}
