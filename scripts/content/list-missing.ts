// Liste les questions d'archives jouables sans explication rédigée (aide à la rédaction).
import { readFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import { QuestionFile } from '../../src/schemas/content';
import { isPlayable } from '../../src/services/scoring/score';

const dir = join(import.meta.dirname, '../../content/questions');
const full = process.argv.includes('--full');
const missing = readdirSync(dir).filter((f) => f.endsWith('.json'))
  .flatMap((f) => QuestionFile.parse(JSON.parse(readFileSync(join(dir, f), 'utf8'))).questions)
  .filter((q) => q.kind === 'archive' && isPlayable(q) && !q.explanation);
missing.sort((a, b) => (a.chapter + a.subchapter).localeCompare(b.chapter + b.subchapter));
for (const q of missing) {
  if (!full) { console.log(`${q.chapter}/${q.subchapter}\t${q.id}`); continue; }
  console.log(`\n### ${q.id} [${q.chapter}/${q.subchapter}] ${q.instruction} ${q.answerStatus} attendu=${q.expected.join(',')} réf=${q.provenance?.auditRef} dup=${q.duplicateGroup ?? ''}`);
  console.log(q.stem);
  for (const o of q.options) console.log(`  ${o.id}. ${o.text}`);
  if (q.answerNote) console.log(`  NOTE: ${q.answerNote}`);
  for (const c of q.sourceComments) console.log(`  COMMENTAIRE: ${c}`);
}
console.log(`\n${missing.length} question(s) sans explication.`);
