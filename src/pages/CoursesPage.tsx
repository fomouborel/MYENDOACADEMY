import { chapters } from '@/data/content';
import { ChapterCard } from '@/components/ChapterCard';

export function CoursesPage() {
  return (
    <section>
      <h1>Mes cours</h1>
      <p className="lead">Chaque cours suit le même parcours : apprendre, vérifier, s’entraîner, puis travailler les vraies questions d’examen.</p>
      <ul className="cards">
        {chapters.filter((c) => c.domain === 'thyroide').map((c) => <ChapterCard key={c.id} c={c} />)}
      </ul>
      <h2>Bientôt</h2>
      <ul className="cards">
        {chapters.filter((c) => c.domain !== 'thyroide').map((c) => <ChapterCard key={c.id} c={c} />)}
      </ul>
    </section>
  );
}
