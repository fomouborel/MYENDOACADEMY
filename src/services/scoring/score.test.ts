import { describe, expect, it } from 'vitest';
import { mcq } from '@/test/fixtures';
import { grade, instructionLabel, isPlayable, reliabilityMessage } from './score';

describe('correction', () => {
  it('juste seulement si la sélection correspond exactement', () => {
    const q = mcq();
    expect(grade(q, ['D']).correct).toBe(true);
    expect(grade(q, ['A']).correct).toBe(false);
    expect(grade(q, ['D', 'A']).correct).toBe(false);
    expect(grade(q, []).correct).toBe(false);
  });
  it('détaille chaque proposition', () => {
    const g = grade(mcq(), ['A']);
    expect(g.perOption).toMatchObject({ A: 'wrongly-selected', D: 'expected-missed', B: 'correctly-ignored' });
  });
  it('deux fausses : les deux doivent être cochées', () => {
    const q = mcq({ instruction: 'two-false', expected: ['B', 'E'] });
    expect(grade(q, ['E', 'B']).correct).toBe(true);
    expect(grade(q, ['B']).correct).toBe(false);
  });
  it('vrai / faux', () => {
    const q = mcq({ format: 'true-false', options: [], instruction: undefined, expected: ['FAUX'] });
    expect(grade(q, ['FAUX']).correct).toBe(true);
    expect(grade(q, ['VRAI']).correct).toBe(false);
  });
});

describe('questions jouables', () => {
  it('exclut réponses absentes et questions incomplètes', () => {
    expect(isPlayable(mcq())).toBe(true);
    expect(isPlayable(mcq({ answerStatus: 'absent', expected: [] }))).toBe(false);
    expect(isPlayable(mcq({ answerStatus: 'incomplete' }))).toBe(false);
    expect(isPlayable(mcq({ options: mcq().options.slice(0, 2) }))).toBe(false);
  });
  it('incohérence consigne / réponses → non jouable', () => {
    expect(isPlayable(mcq({ expected: ['A', 'B'] }))).toBe(false);
  });
  it('une question non jouable n’est jamais notée', () => {
    expect(grade(mcq({ answerStatus: 'absent', expected: [] }), ['A']).correct).toBeNull();
  });
});

describe('messages', () => {
  it('adapte la consigne et affiche la fiabilité', () => {
    expect(instructionLabel('one-false')).toContain('FAUSSE');
    expect(instructionLabel('two-correct')).toContain('deux bonnes');
    expect(reliabilityMessage(mcq())).toContain('non officielle');
    expect(reliabilityMessage(mcq({ answerStatus: 'disputed' }))).toContain('prudence');
  });
});
