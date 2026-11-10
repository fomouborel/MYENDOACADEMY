import { describe, expect, it } from 'vitest';
import chapters from '../../../content/chapters.json';
import exams from '../../../content/exams.json';
import { mcq } from '@/test/fixtures';
import { validateContent } from './validate';

const run = (questions: unknown[], lessons: Record<string, string> = {}, ch: unknown = chapters) =>
  validateContent({ chapters: ch, exams, questionFiles: { 'questions/test.json': { source: 'test', questions } }, lessons });

describe('validateur de contenu', () => {
  it('le contenu réel du dépôt est valide', () => {
    expect(validateContent({ chapters, exams, questionFiles: {}, lessons: {} })).toEqual([]);
  });
  it('accepte une question cohérente', () => {
    expect(run([mcq()])).toEqual([]);
  });
  it('refuse identifiants en double et sous-chapitres inconnus', () => {
    const e = run([mcq(), mcq({ subchapter: 'inconnu' })]);
    expect(e.join('\n')).toMatch(/en double/);
    expect(e.join('\n')).toMatch(/sous-chapitre inconnu/);
  });
  it('exige une note pour une réponse discutée et la cohérence du nombre de réponses', () => {
    expect(run([mcq({ answerStatus: 'disputed' })]).join()).toMatch(/answerNote/);
    expect(run([mcq({ expected: ['A', 'B'] })]).join()).toMatch(/demande 1/);
  });
  it('refuse un indice qui révèle la réponse', () => {
    expect(run([mcq({ hints: ['Orientation', 'Rappel', 'Pensez à : Proposition delta'] })]).join()).toMatch(/indice recopie/);
  });
  it('règle pédiatrie : thyroïde de l’enfant dans hypo › congenitale', () => {
    const p = mcq({ id: 'ENDO-2024-01-PEDIA-QCM-001', provenance: { ...(mcq() as { provenance: object }).provenance, discipline: 'PEDIA' } as never });
    expect(run([p]).join()).toMatch(/pédiatrique/);
    expect(run([{ ...p, chapter: 'hypo', subchapter: 'congenitale' }])).toEqual([]);
  });
  it('un exercice créé ne peut pas se faire passer pour une question d’archives', () => {
    const ex = { ...mcq(), kind: 'exercise', provenance: undefined, id: 'ENDO-EX-thyroide-QCM-001', answerStatus: 'proposed' };
    expect(run([ex]).join()).toMatch(/authored/);
  });
  it('leçon : encadré archives et « À retenir » obligatoires', () => {
    const ch = structuredClone(chapters);
    ch.chapters[0].lessons = [{ id: 'thyr-explo', title: 'T', file: 'thyroide/01-explo.md', subchapters: ['explo'], minutes: 10 }] as never;
    expect(run([], { 'thyroide/01-explo.md': '# Sans encadré' }, ch).join()).toMatch(/archives/);
    expect(run([], { 'thyroide/01-explo.md': ':::archives\nx\n:::\n## À retenir' }, ch)).toEqual([]);
  });
});
