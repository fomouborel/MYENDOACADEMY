/**
 * Chargement du contenu (séparé du code) : content/chapters.json, exams.json, questions/*.json, lessons/**.md.
 * Le contenu est vérifié en CI par `npm run validate:content` ; ici on le parse pour obtenir des types sûrs.
 */
import chaptersRaw from '../../content/chapters.json';
import examsRaw from '../../content/exams.json';
import { ChaptersFile, ExamsFile, QuestionFile, type Chapter, type Question } from '@/schemas/content';

const questionModules = import.meta.glob('../../content/questions/*.json', { eager: true, import: 'default' });
const lessonModules = import.meta.glob('../../content/lessons/**/*.md', { eager: true, query: '?raw', import: 'default' });

export const chapters = ChaptersFile.parse(chaptersRaw).chapters.sort((a, b) => a.order - b.order);
export const examSessions = ExamsFile.parse(examsRaw).sessions;
export const questions: Question[] = Object.values(questionModules).flatMap((m) => QuestionFile.parse(m).questions);
export const questionById = new Map(questions.map((q) => [q.id, q]));

export type LessonRef = Chapter['lessons'][number] & { chapterId: string; index: number };
export const lessons: LessonRef[] = chapters.flatMap((c) => c.lessons.map((l, index) => ({ ...l, chapterId: c.id, index })));
export const lessonById = new Map(lessons.map((l) => [l.id, l]));

export function lessonMarkdown(file: string): string {
  const key = Object.keys(lessonModules).find((k) => k.endsWith(`/lessons/${file}`));
  return key ? (lessonModules[key] as string) : '';
}

/** Un chapitre est ouvert à l'étudiante s'il est « available » (le validateur impose alors des leçons). */
export function isOpen(c: Chapter): boolean {
  return c.status === 'available' && c.lessons.length > 0;
}
export const openChapters = chapters.filter(isOpen);
export const chapterById = new Map(chapters.map((c) => [c.id, c]));
export const thyroidChapters = chapters.filter((c) => c.domain === 'thyroide');

const DOMAIN_LABEL: Record<string, string> = { thyroide: 'thyroïde', hypophyse: 'hypophyse', surrenales: 'surrénales', pharmaco: 'pharmacologie', obesite: 'obésité', diabete: 'diabète' };
/** Domaines réellement intégrés (au moins un cours ouvert), en toutes lettres : « thyroïde et hypophyse ». */
export const integratedDomainsLabel = (() => {
  const names = [...new Set(openChapters.map((c) => c.domain))].map((d) => DOMAIN_LABEL[d] ?? d);
  return names.length <= 1 ? (names[0] ?? '') : `${names.slice(0, -1).join(', ')} et ${names[names.length - 1]}`;
})();

export const SESSION_LABEL: Record<string, string> = Object.fromEntries(examSessions.map((s) => [s.id, s.label]));
export const DISCIPLINE_LABEL: Record<string, string> = {
  ADULTE: 'Endocrinologie adulte',
  PEDIA: 'Pédiatrie',
  RADIO: 'Radiologie',
  ANAPATH: 'Anatomie pathologique',
  PHARMA: 'Pharmacologie',
};
