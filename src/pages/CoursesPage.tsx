import { chapters, isOpen } from '@/data/content';
import { ChapterCard } from '@/components/ChapterCard';

export function CoursesPage() {
  // Un cours est rangé selon qu'il est ouvert (statut « available » et leçons présentes), jamais selon son domaine.
  const open = chapters.filter(isOpen);
  const soon = chapters.filter((c) => !isOpen(c));
  return (
    <section>
      <h1>Mes cours</h1>
      <p className="lead">Chaque cours suit le même parcours : apprendre, vérifier, s’entraîner, puis travailler les vraies questions d’examen.</p>
      <ul className="cards" aria-label="Cours disponibles">
        {open.map((c) => <ChapterCard key={c.id} c={c} />)}
      </ul>
      {soon.length > 0 && (
        <>
          <h2>Bientôt</h2>
          <ul className="cards" aria-label="Cours bientôt disponibles">
            {soon.map((c) => <ChapterCard key={c.id} c={c} />)}
          </ul>
        </>
      )}
    </section>
  );
}
