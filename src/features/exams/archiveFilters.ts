/** Filtres de la banque d'anciens examens (prompt § 9). Logique pure. */
import type { Question } from '@/schemas/content';
import type { QuestionState, QuestionStatus } from '@/schemas/progress';
import { statusOf } from '@/services/progress/questionState';
import { isPlayable } from '@/services/scoring/score';
import { audienceOf } from '@/utils/audience';

export interface ArchiveFilter {
  session?: string;
  discipline?: string;
  teacher?: string;
  chapter?: string;
  subchapter?: string;
  instruction?: string;
  difficulty?: string;
  status?: QuestionStatus | '';
  reliability?: string;
  audience?: string;
  playable?: 'all' | 'yes' | 'no';
  text?: string;
}

const norm = (s: string) => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');

export function archiveQuestions(all: Question[]) {
  return all.filter((q): q is Extract<Question, { kind: 'archive' }> => q.kind === 'archive');
}

export function filterArchives(all: Question[], f: ArchiveFilter, states: Map<string, QuestionState>, now: Date) {
  return archiveQuestions(all).filter((q) => {
    const p = q.provenance;
    if (f.session && p.session !== f.session) return false;
    if (f.discipline && p.discipline !== f.discipline) return false;
    if (f.teacher && (p.teacher ?? 'non attribué') !== f.teacher) return false;
    if (f.chapter && q.chapter !== f.chapter) return false;
    if (f.subchapter && q.subchapter !== f.subchapter) return false;
    if (f.instruction && q.instruction !== f.instruction) return false;
    if (f.difficulty && String(q.difficulty) !== f.difficulty) return false;
    if (f.status && statusOf(states.get(q.id), now) !== f.status) return false;
    if (f.reliability && q.answerStatus !== f.reliability) return false;
    if (f.audience && audienceOf(q) !== f.audience) return false;
    if (f.playable === 'yes' && !isPlayable(q)) return false;
    if (f.playable === 'no' && isPlayable(q)) return false;
    if (f.text && !norm(q.stem + ' ' + q.options.map((o) => o.text).join(' ')).includes(norm(f.text))) return false;
    return true;
  });
}

/** Ordre de présentation : session la plus récente d'abord, puis numéro d'origine. */
const SESSION_ORDER = ['2026-01', '2025-01', '2024-01', '2023-05', '2022-05', 'ND'];
export function sortArchives<T extends { provenance: { session: string; originalNumber: number | null; page: number } }>(qs: T[]): T[] {
  return [...qs].sort(
    (a, b) =>
      SESSION_ORDER.indexOf(a.provenance.session) - SESSION_ORDER.indexOf(b.provenance.session) ||
      a.provenance.page - b.provenance.page ||
      (a.provenance.originalNumber ?? 999) - (b.provenance.originalNumber ?? 999),
  );
}
