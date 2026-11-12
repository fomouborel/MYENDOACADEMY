# ENDOCRINO ACADEMY

Environnement d'apprentissage de l'endocrinologie (UCL) : cours, entraînement, anciens examens, examens blancs et suivi de progression.
Application **statique** et gratuite : aucun serveur ni compte, la progression reste dans le navigateur (avec export / import JSON).

- **Application : https://fomouborel.github.io/MYENDOACADEMY/** (publiée automatiquement à chaque modification validée sur `main`)
- Mode d'emploi pour l'étudiante : dans l'application, lien « ❔ Mode d'emploi » en bas du menu
- Documentation : [audit](docs/AUDIT-PHASE-1.md) · [architecture](docs/ARCHITECTURE-PHASE-2.md) · [conception pédagogique](docs/PHASE-3-CONCEPTION.md) · [prototype](docs/PHASE-4-PROTOTYPE.md) · [banque](docs/PHASE-5-BANQUE.md) · [fonctionnalités](docs/PHASE-6-FONCTIONNALITES.md) · [tests et déploiement](docs/PHASE-7-DEPLOIEMENT.md) · [domaine hypophyse](docs/DOMAINE-HYPOPHYSE.md) · [domaine surrénales](docs/DOMAINE-SURRENALES.md) · [pharmacologie](docs/DOMAINE-PHARMACOLOGIE.md) · [obésité](docs/DOMAINE-OBESITE.md) · [diabète](docs/DOMAINE-DIABETE.md) · [décisions validées](docs/DECISIONS.md)

## Commandes (développement)

| Commande | Rôle |
|---|---|
| `npm ci` | installer les dépendances |
| `npm run dev` | lancer l'application en local |
| `npm run validate:content` | vérifier les cours et les questions (`content/`) |
| `npm test` | tests unitaires |
| `npm run e2e` | tests de bout en bout (ordinateur + smartphone) |
| `npm run check` | TypeScript + contenu + tests + build |

Le contenu pédagogique se trouve dans `content/` et se modifie sans toucher au code.
