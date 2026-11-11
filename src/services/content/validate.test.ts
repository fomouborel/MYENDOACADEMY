import { describe, expect, it } from 'vitest';
import chapters from '../../../content/chapters.json';
import exams from '../../../content/exams.json';
import { mcq } from '@/test/fixtures';
import { readdirSync, readFileSync } from 'node:fs';
import { QuestionFile } from '@/schemas/content';
import { isPlayable } from '@/services/scoring/score';
import { validateContent } from './validate';

// Leçons réelles du dépôt (content/lessons/…).
const realLessons = Object.fromEntries(
  chapters.chapters.flatMap((c) => c.lessons.map((l) => [l.file, readFileSync(`content/lessons/${l.file}`, 'utf8')])),
);
// Pour tester les règles des questions isolément : chapitres sans leçons.
const bare = { chapters: chapters.chapters.map((c) => ({ ...c, status: 'pending', lessons: [] })) };

const run = (questions: unknown[], lessons: Record<string, string> = {}, ch: unknown = bare) =>
  validateContent({ chapters: ch, exams, questionFiles: { 'questions/test.json': { source: 'test', questions } }, lessons });

describe('validateur de contenu', () => {
  it('le contenu réel du dépôt est valide', () => {
    expect(validateContent({ chapters, exams, questionFiles: {}, lessons: realLessons })).toEqual([]);
  });
  it('chaque question d’archives jouable a ses 3 indices et son explication', () => {
    const missing = readdirSync('content/questions')
      .filter((f) => f.endsWith('.json'))
      .flatMap((f) => QuestionFile.parse(JSON.parse(readFileSync(`content/questions/${f}`, 'utf8'))).questions)
      .filter((q) => q.kind === 'archive' && isPlayable(q) && (!q.explanation || !q.hints))
      .map((q) => q.id);
    expect(missing).toEqual([]);
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
    const ch = structuredClone(bare);
    ch.chapters[0].lessons = [{ id: 'thyr-explo', title: 'T', file: 'thyroide/01-explo.md', subchapters: ['explo'], minutes: 10 }] as never;
    expect(run([], { 'thyroide/01-explo.md': '# Sans encadré' }, ch).join()).toMatch(/archives/);
    expect(run([], { 'thyroide/01-explo.md': ':::archives\nx\n:::\n## À retenir' }, ch)).toEqual([]);
    expect(run([], { 'thyroide/01-explo.md': ':::archives\nThyroid 2016;26:1-133\n:::\n## À retenir' }, ch).join()).toMatch(/deux-points/);
    expect(run([], { 'thyroide/01-explo.md': ':::archives\nThyroid 2016;26\\:1-133, voir : ici\n:::\n## À retenir' }, ch)).toEqual([]);
  });
});
