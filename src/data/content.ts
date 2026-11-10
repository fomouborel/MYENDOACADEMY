/**
 * Chargement du contenu (séparé du code) : content/chapters.json, exams.json, questions/*.json.
 * Le contenu est vérifié en CI par `npm run validate:content` ; ici on le parse pour obtenir des types sûrs.
 */
import chaptersRaw from '../../content/chapters.json';
import examsRaw from '../../content/exams.json';
import { ChaptersFile, ExamsFile, QuestionFile, type Question } from '@/schemas/content';

const questionModules = import.meta.glob('../../content/questions/*.json', { eager: true, import: 'default' });

export const chapters = ChaptersFile.parse(chaptersRaw).chapters.sort((a, b) => a.order - b.order);
export const examSessions = ExamsFile.parse(examsRaw).sessions;
export const questions: Question[] = Object.values(questionModules).flatMap((m) => QuestionFile.parse(m).questions);
export const thyroidChapters = chapters.filter((c) => c.domain === 'thyroide');
