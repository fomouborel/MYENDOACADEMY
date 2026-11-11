import { Link } from 'react-router-dom';
import { chapters, lessons as allLessons } from '@/data/content';
import { ChapterCard } from '@/components/ChapterCard';
import { CoverageStats } from '@/components/Stats';
import { useProgress } from '@/state/ProgressContext';

export function HomePage() {
  const { lessons } = useProgress();
  const nextLesson = allLessons.find((l) => !lessons.get(l.id)?.completedAt);
  return (
    <section>
      <h1>Bienvenue</h1>
      <p className="lead">Comprendre tes cours, travailler les anciens examens d’endocrinologie et suivre ta progression.</p>
      {nextLesson && (
        <div className="notice">
          <strong>Pour continuer :</strong>{' '}
          <Link to={`/cours/${nextLesson.chapterId}/lecon/${nextLesson.id}`}>{nextLesson.title}</Link>
        </div>
      )}
      <h2>Thyroïde : tes trois premiers cours</h2>
      <ul className="cards">{chapters.filter((c) => c.domain === 'thyroide').map((c) => <ChapterCard key={c.id} c={c} />)}</ul>
      <h2>Ta progression</h2>
      <CoverageStats />
      <p className="muted">Version prototype : 30 questions d’anciens examens et 15 exercices sont déjà intégrés ; la banque complète de thyroïde arrive à la prochaine étape.</p>
    </section>
  );
}
