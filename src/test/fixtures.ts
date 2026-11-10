import type { Question } from '@/schemas/content';

/** Question FICTIVE de test (pas un contenu pédagogique). */
export function mcq(over: Partial<Question> = {}): Question {
  return {
    id: 'ENDO-2024-01-ADULTE-QCM-001',
    kind: 'archive',
    format: 'mcq',
    instruction: 'one-false',
    stem: 'Question de test',
    labs: [],
    options: [
      { id: 'A', text: 'Proposition alpha' },
      { id: 'B', text: 'Proposition beta' },
      { id: 'C', text: 'Proposition gamma' },
      { id: 'D', text: 'Proposition delta' },
      { id: 'E', text: 'Proposition epsilon' },
    ],
    expected: ['D'],
    answerStatus: 'proposed',
    sourceComments: [],
    chapter: 'thyroide',
    subchapter: 'explo',
    lessonLinks: [],
    tags: [],
    difficulty: 2,
    clinical: false,
    provenance: {
      session: '2024-01',
      discipline: 'ADULTE',
      teacher: null,
      formerTeacher: false,
      sourceFile: 'test.pdf',
      page: 1,
      originalNumber: 1,
      auditRef: '2024-01-Q1',
    },
    ...over,
  } as Question;
}
