import type { Instruction, Question } from '@/schemas/content';

/** Nombre de propositions à cocher annoncé par la consigne (null = libre). */
export function expectedSelectionCount(instruction: Instruction | undefined): number | null {
  switch (instruction) {
    case 'one-correct':
    case 'one-false':
    case 'one-true':
      return 1;
    case 'two-correct':
    case 'two-false':
      return 2;
    default:
      return null;
  }
}

/** Libellé affiché au-dessus des propositions : l'interface s'adapte à la formulation de l'examen. */
export function instructionLabel(instruction: Instruction | undefined): string {
  switch (instruction) {
    case 'one-correct':
      return 'Cochez la bonne réponse.';
    case 'two-correct':
      return 'Cochez les deux bonnes réponses.';
    case 'one-false':
      return 'Cochez la proposition FAUSSE.';
    case 'two-false':
      return 'Cochez les deux propositions FAUSSES.';
    case 'one-true':
      return 'Cochez la seule proposition VRAIE.';
    case 'all-that-apply':
      return 'Cochez toutes les propositions qui conviennent.';
    default:
      return 'Choisissez votre réponse.';
  }
}

/**
 * Une question est « jouable » (notée automatiquement) seulement si elle est complète et
 * possède une réponse attendue. Les autres restent consultables dans la banque d'archives.
 */
export function isPlayable(q: Question): boolean {
  if (q.answerStatus === 'absent' || q.answerStatus === 'incomplete') return false;
  if (q.format === 'qroc') return Boolean(q.qroc);
  if (q.expected.length === 0) return false;
  if (q.format === 'mcq') {
    if (q.options.length < 3) return false;
    const ids = new Set(q.options.map((o) => o.id));
    if (!q.expected.every((e) => ids.has(e))) return false;
    const n = expectedSelectionCount(q.instruction);
    if (n !== null && q.expected.length !== n) return false;
  }
  return true;
}

export type OptionVerdict = 'expected-selected' | 'expected-missed' | 'wrongly-selected' | 'correctly-ignored';

export interface Grade {
  /** null : réponse non notée (QROC ou question non jouable). */
  correct: boolean | null;
  perOption: Record<string, OptionVerdict>;
}

/** Correction : la réponse est juste si la sélection est EXACTEMENT l'ensemble attendu. */
export function grade(q: Question, selected: string[]): Grade {
  const sel = new Set(selected);
  const exp = new Set(q.expected);
  const perOption: Record<string, OptionVerdict> = {};
  const ids = q.format === 'true-false' ? ['VRAI', 'FAUX'] : q.options.map((o) => o.id);
  for (const id of ids) {
    if (exp.has(id)) perOption[id] = sel.has(id) ? 'expected-selected' : 'expected-missed';
    else perOption[id] = sel.has(id) ? 'wrongly-selected' : 'correctly-ignored';
  }
  if (!isPlayable(q) || q.format === 'qroc') return { correct: null, perOption };
  const correct = sel.size === exp.size && [...exp].every((e) => sel.has(e));
  return { correct, perOption };
}

/** Message de fiabilité affiché avec chaque correction. */
export function reliabilityMessage(q: Question): string {
  switch (q.answerStatus) {
    case 'official':
      return 'Correction officielle identifiée.';
    case 'proposed':
      return 'Réponse proposée dans la compilation d’étudiants — non officielle.';
    case 'disputed':
      return 'Réponse discutée ou contestée dans la compilation — à considérer avec prudence.';
    case 'deduced':
      return 'Réponse déduite, à vérifier.';
    case 'absent':
      return 'Aucune réponse disponible dans la compilation.';
    case 'incomplete':
      return 'Question incomplète dans la compilation (propositions manquantes).';
    case 'authored':
      return 'Exercice créé pour l’entraînement (hors archives) — correction rédigée, à valider.';
  }
}
