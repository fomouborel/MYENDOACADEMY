/**
 * Révision espacée simple (boîtes de Leitner, 5 boîtes).
 * - Bonne réponse sans indice : boîte + 1.
 * - Bonne réponse avec indice(s) : la boîte ne monte pas (la notion n'est pas encore autonome).
 * - Mauvaise réponse : retour en boîte 1 (la question revient dès le lendemain).
 * Les questions échouées reviennent donc plus souvent que les questions maîtrisées.
 */
export const BOX_INTERVAL_DAYS: Record<number, number> = { 1: 1, 2: 3, 3: 7, 4: 14, 5: 30 };

export interface SrsInput {
  box: number;
  correct: boolean;
  hintsUsed: number;
  at: Date;
}

export function nextBox({ box, correct, hintsUsed }: Omit<SrsInput, 'at'>): number {
  if (!correct) return 1;
  if (hintsUsed > 0) return Math.max(1, box);
  return Math.min(5, Math.max(1, box) + 1);
}

export function dueDate(box: number, from: Date): Date {
  const d = new Date(from);
  d.setUTCDate(d.getUTCDate() + (BOX_INTERVAL_DAYS[box] ?? 1));
  return d;
}

export function isDue(dueAt: string | null, now: Date): boolean {
  return dueAt !== null && new Date(dueAt).getTime() <= now.getTime();
}
