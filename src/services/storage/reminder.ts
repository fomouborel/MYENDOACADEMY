/** Rappel d'exporter la sauvegarde : la progression n'existe que dans ce navigateur. */
export const REMINDER_DAYS = 14;
export const REMINDER_MIN_ATTEMPTS = 20;

export function needsBackupReminder(attemptCount: number, lastExportAt: string | undefined, now: Date): boolean {
  if (attemptCount < REMINDER_MIN_ATTEMPTS) return false;
  if (!lastExportAt) return true;
  return now.getTime() - new Date(lastExportAt).getTime() > REMINDER_DAYS * 86_400_000;
}
