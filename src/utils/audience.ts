import type { Question } from '@/schemas/content';

export type Audience = 'adulte' | 'pediatrie';

/**
 * Public d'une question (méthode § 6) : Pédiatrie si discipline pédiatrique, si le sous-chapitre est
 * pédiatrique (ex. hypothyroïdie congénitale, décision phase 1) ou si elle porte l'étiquette « pédiatrie ».
 */
export const PEDIATRIC_SUBCHAPTERS = new Set(['hypo/congenitale']);

export function audienceOf(q: Question): Audience {
  if (q.kind === 'archive' && q.provenance.discipline === 'PEDIA') return 'pediatrie';
  if (PEDIATRIC_SUBCHAPTERS.has(`${q.chapter}/${q.subchapter}`)) return 'pediatrie';
  if (q.tags.includes('pédiatrie')) return 'pediatrie';
  return 'adulte';
}
