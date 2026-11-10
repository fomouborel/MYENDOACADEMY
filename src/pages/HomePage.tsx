import { chapters, thyroidChapters } from '@/data/content';

export function HomePage() {
  return (
    <section>
      <h1>Bienvenue</h1>
      <p className="lead">
        ENDOCRINO ACADEMY t’accompagne pour comprendre tes cours, travailler les anciens examens d’endocrinologie et suivre ta progression.
      </p>
      <div className="notice">
        <strong>Application en préparation.</strong> Les cours et les questions sont en cours d’intégration. Les rubriques apparaîtront ici dès qu’elles seront prêtes et vérifiées.
      </div>
      <h2>Premiers cours prévus</h2>
      <ul className="cards">
        {thyroidChapters.map((c) => (
          <li key={c.id} className="card disabled" aria-disabled="true">
            <span className="card-icon" aria-hidden>{c.icon}</span>
            <span className="card-title">{c.title}</span>
            <span className="card-sub">{c.short}</span>
            <span className="badge">Intégration en cours</span>
          </li>
        ))}
      </ul>
      <p className="muted">Ensuite : {chapters.filter((c) => c.domain !== 'thyroide').map((c) => c.title).join(' · ')}.</p>
    </section>
  );
}
