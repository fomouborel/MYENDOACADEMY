import { describe, expect, it } from 'vitest';
import { questions } from '@/data/content';
import { filterArchives, sortArchives } from './archiveFilters';

const now = new Date();
describe('banque d’anciens examens', () => {
  it('contient toute la thyroïde intégrée, archives uniquement', () => {
    const all = filterArchives(questions, {}, new Map(), now);
    expect(all.length).toBeGreaterThanOrEqual(130);
    expect(all.every((q) => q.kind === 'archive')).toBe(true);
  });
  it('filtre par session, enseignant, fiabilité et jouabilité', () => {
    expect(filterArchives(questions, { session: '2026-01' }, new Map(), now).every((q) => q.provenance.session === '2026-01')).toBe(true);
    expect(filterArchives(questions, { teacher: 'Beauloye' }, new Map(), now).every((q) => q.provenance.formerTeacher)).toBe(true);
    const consult = filterArchives(questions, { playable: 'no' }, new Map(), now);
    expect(consult.length).toBeGreaterThan(0);
    expect(consult.every((q) => ['absent', 'incomplete', 'disputed'].includes(q.answerStatus))).toBe(true);
  });
  it('recherche plein texte insensible aux accents', () => {
    expect(filterArchives(questions, { text: 'quervain' }, new Map(), now).length).toBeGreaterThanOrEqual(5);
  });
  it('trie de la session la plus récente à la plus ancienne', () => {
    const s = sortArchives(filterArchives(questions, {}, new Map(), now));
    expect(s[0].provenance.session).toBe('2026-01');
    expect(s[s.length - 1].provenance.session).toBe('ND');
  });
});
