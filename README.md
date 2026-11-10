# ENDOCRINO ACADEMY

Environnement d'apprentissage de l'endocrinologie (UCL) : cours, entraînement, anciens examens, examens blancs et suivi de progression.
Application **statique** et gratuite : aucun serveur ni compte, la progression reste dans le navigateur (avec export / import JSON).

- Adresse prévue : https://fomouborel.github.io/MYENDOACADEMY/ (après activation de GitHub Pages et publication sur `main`)
- Documentation : [`docs/AUDIT-PHASE-1.md`](docs/AUDIT-PHASE-1.md) · [`docs/ARCHITECTURE-PHASE-2.md`](docs/ARCHITECTURE-PHASE-2.md)

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
