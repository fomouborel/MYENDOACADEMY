import { Link } from 'react-router-dom';

/** Mode d'emploi en langage simple, sans jargon informatique. */
export function HelpPage() {
  return (
    <section className="help">
      <h1>Mode d’emploi</h1>
      <h2>Par où commencer ?</h2>
      <ol>
        <li>Ouvre <Link to="/cours">Mes cours</Link> et choisis un cours.</li>
        <li>Lis les leçons dans l’ordre, puis clique sur « J’ai terminé cette leçon ».</li>
        <li>Fais ensuite les étapes du cours : vérifier, s’entraîner, niveau examen, évaluation finale.</li>
        <li>Reviens chaque jour dans <Link to="/revisions">Mes révisions</Link> : l’application te propose les questions à revoir au bon moment.</li>
      </ol>
      <h2>Comment lire les couleurs ?</h2>
      <ul>
        <li>🟦 <strong>Archives UCL</strong> : ce qui vient des anciens examens (retranscrits par des étudiants).</li>
        <li>🟨 <strong>À valider</strong> : explication rédigée pour t’aider, pas encore relue par un enseignant.</li>
        <li>🟩 <strong>Validée</strong> : explication relue.</li>
        <li>Une « réponse proposée (compilation) » n’est <strong>pas</strong> une correction officielle ; une « réponse discutée » est à prendre avec prudence.</li>
      </ul>
      <h2>Ma progression est-elle sauvegardée ?</h2>
      <p>Oui, automatiquement, sur l’appareil que tu utilises. Mais elle n’est pas partagée entre ton téléphone et ton ordinateur.</p>
      <ul>
        <li>Pour changer d’appareil ou par sécurité : <Link to="/progression">Ma progression</Link> → « Télécharger ma sauvegarde », puis, sur l’autre appareil, « Choisir un fichier de sauvegarde ».</li>
        <li>Si tu effaces les données de navigation de ton navigateur, la progression est effacée : garde une sauvegarde récente.</li>
      </ul>
      <h2>Installer l’application sur mon téléphone</h2>
      <ul>
        <li><strong>iPhone (Safari)</strong> : bouton Partager → « Sur l’écran d’accueil ». C’est recommandé sur iPhone, pour que tes données soient mieux conservées.</li>
        <li><strong>Android (Chrome)</strong> : menu ⋮ → « Installer l’application » ou « Ajouter à l’écran d’accueil ».</li>
        <li>Une fois ouverte une première fois, l’application fonctionne aussi sans connexion internet.</li>
      </ul>
      <h2>Une question semble fausse ?</h2>
      <p>Les archives sont des souvenirs d’examen : certaines corrections sont incertaines (elles sont signalées). Note l’identifiant de la question (ex. ENDO-2024-01-ADULTE-QCM-031), visible sur sa page dans « Anciens examens », et signale-le pour qu’elle soit corrigée.</p>
    </section>
  );
}
