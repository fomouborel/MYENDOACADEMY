/** npx tsx scripts/content/coverage.ts — couverture de la banque thyroïde par rapport à l'audit. */
import { readFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import { QuestionFile } from '../../src/schemas/content';
import { isPlayable } from '../../src/services/scoring/score';

const dir = join(import.meta.dirname, '..', '..', 'content', 'questions');
const qs = readdirSync(dir).flatMap((f) => QuestionFile.parse(JSON.parse(readFileSync(join(dir, f), 'utf8'))).questions);
const audit = JSON.parse(readFileSync(join(import.meta.dirname, '..', 'audit', 'data', 'thyroide-audit.json'), 'utf8')) as { ref: string; placeholder: boolean }[];
const arch = qs.filter((q) => q.kind === 'archive');
const refs = new Set(arch.map((q) => (q.kind === 'archive' ? q.provenance.auditRef : '')));
const missing = audit.filter((a) => !a.placeholder && !refs.has(a.ref));
const count = <K extends string>(f: (q: (typeof arch)[number]) => K) => arch.reduce<Record<string, number>>((m, q) => ((m[f(q)] = (m[f(q)] ?? 0) + 1), m), {});
console.log(JSON.stringify({
  auditThyroide: audit.length, nonRetranscrites: audit.filter((a) => a.placeholder).length,
  integrees: arch.length, manquantes: missing.map((m) => m.ref), exercices: qs.length - arch.length,
  jouables: arch.filter(isPlayable).length, consultables: arch.filter((q) => !isPlayable(q)).length,
  avecExplication: arch.filter((q) => q.explanation).length,
  parStatut: count((q) => q.answerStatus), parSession: count((q) => (q.kind === 'archive' ? q.provenance.session : '')),
  parChapitre: count((q) => q.chapter), parDiscipline: count((q) => (q.kind === 'archive' ? q.provenance.discipline : '')),
  jouablesParChapitre: arch.filter(isPlayable).reduce<Record<string, number>>((m, q) => ((m[q.chapter] = (m[q.chapter] ?? 0) + 1), m), {}),
}, null, 1));
