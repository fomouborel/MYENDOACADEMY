import { Link } from 'react-router-dom';
import type { Chapter } from '@/schemas/content';
import { isOpen, questions } from '@/data/content';
import { useProgress } from '@/state/ProgressContext';
import { chapterMastery, MASTERY_LABEL } from '@/services/progress/chapterMastery';

export function ChapterCard({ c }: { c: Chapter }) {
  const { states, sessions, lessons } = useProgress();
  if (!isOpen(c)) {
    return (
      <li className="card disabled" aria-disabled="true">
        <span className="card-icon" aria-hidden>{c.icon}</span>
        <span className="card-title">{c.title}</span>
        <span className="card-sub">{c.short}</span>
        <span className="badge">Intégration en cours</span>
      </li>
    );
  }
  const m = chapterMastery(c.id, questions, states, sessions);
  const read = c.lessons.filter((l) => lessons.get(l.id)?.completedAt).length;
  return (
    <li className="card">
      <Link to={`/cours/${c.id}`} className="card-link">
        <span className="card-icon" aria-hidden>{c.icon}</span>
        <span className="card-title">{c.title}</span>
        <span className="card-sub">{c.short}</span>
        <span className="meter" aria-label={`${read} leçon(s) lue(s) sur ${c.lessons.length}`}>
          <span style={{ width: `${(read / c.lessons.length) * 100}%` }} />
        </span>
        <span className="card-foot">{read}/{c.lessons.length} leçons · {MASTERY_LABEL[m.level]}</span>
      </Link>
    </li>
  );
}
