/** npm run validate:content — vérifie tout le dossier content/ (bloquant en CI). */
import { readFileSync, readdirSync, existsSync, statSync } from 'node:fs';
import { join, relative } from 'node:path';
import { validateContent } from '../src/services/content/validate';

const root = join(import.meta.dirname, '..', 'content');
const readJson = (p: string) => JSON.parse(readFileSync(p, 'utf8'));
const walk = (dir: string): string[] =>
  existsSync(dir) ? readdirSync(dir).flatMap((f) => (statSync(join(dir, f)).isDirectory() ? walk(join(dir, f)) : [join(dir, f)])) : [];

const questionFiles: Record<string, unknown> = {};
for (const f of walk(join(root, 'questions')).filter((f) => f.endsWith('.json'))) questionFiles[relative(root, f)] = readJson(f);
const lessons: Record<string, string> = {};
for (const f of walk(join(root, 'lessons')).filter((f) => f.endsWith('.md'))) lessons[relative(join(root, 'lessons'), f)] = readFileSync(f, 'utf8');

const errors = validateContent({ chapters: readJson(join(root, 'chapters.json')), exams: readJson(join(root, 'exams.json')), questionFiles, lessons });
const nQ = Object.values(questionFiles).reduce<number>((n, f) => n + (((f as { questions?: unknown[] }).questions)?.length ?? 0), 0);
if (errors.length) {
  console.error(`✗ ${errors.length} erreur(s) dans le contenu :\n` + errors.map((e) => `  - ${e}`).join('\n'));
  process.exit(1);
}
console.log(`✓ Contenu valide : ${Object.keys(questionFiles).length} fichier(s) de questions, ${nQ} question(s), ${Object.keys(lessons).length} leçon(s).`);
