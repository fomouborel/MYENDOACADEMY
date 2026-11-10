# ENDOCRINO ACADEMY — Architecture et modélisation (phase 2)

> Date : 10 novembre 2026 · Branche : `claude/nice-mendel-6foiq0`
> Prérequis : `docs/AUDIT-PHASE-1.md` (recommandations validées le 10/11/2026).
>
> **Statut** : le socle technique est en place et testé. Il comprend :
> - le modèle de données ;
> - les règles de validation ;
> - la logique de correction, de progression et de révision ;
> - la sauvegarde locale ;
> - les workflows de déploiement.
>
> **Aucun contenu pédagogique n'est encore intégré.** Ce document présente les choix structurants à valider avant la phase 3.

---

## 1. Ce qu'il faut retenir

| Sujet | Choix |
|---|---|
| Application | **Site statique** React 19 + TypeScript + Vite. Aucun serveur, aucune base distante, aucune IA pendant l'utilisation. |
| Contenu | Fichiers JSON et Markdown dans `content/`, **séparés du code**. Ils sont vérifiés par un validateur qui bloque le déploiement en cas d'erreur. |
| Fiabilité | Chaque question porte un **statut de correction**. Une réponse d'étudiant n'est jamais affichée comme officielle. |
| Progression | **IndexedDB**, sauvegarde automatique à chaque réponse, export et import JSON. Pas de synchronisation entre appareils. |
| Révision | **Boîtes de Leitner** (5 niveaux). Les erreurs reviennent le lendemain, les questions maîtrisées après 2 à 4 semaines. |
| Maîtrise | Jamais après une seule bonne réponse : il faut au moins 3 réussites sur au moins 2 jours, et une stabilité dans le temps. |
| Déploiement | GitHub Actions, puis GitHub Pages. Une étape qui échoue empêche toute publication. |
| Confidentialité | Le dépôt est **public**. Cloudflare Access ne respecte probablement pas la contrainte « sans carte bancaire » (§ 10). **Recommandation : rester sur GitHub Pages public en V1.** |
| Ce qui est testé | 31 tests unitaires et 8 tests de bout en bout (ordinateur et smartphone), au vert en local. |

---

## 2. Les trois couches

```
┌───────────────────────────── COUCHE 1 — DÉVELOPPEMENT ─────────────────────────────┐
│ Claude Code + dépôt GitHub (source de vérité)                                      │
│  content/  ← cours, questions, sessions (JSON / Markdown)                          │
│  src/      ← application React                                                     │
│  docs/     ← audit, architecture, décisions                                        │
└──────────────────────────────────────┬─────────────────────────────────────────────┘
                                       │ push sur main
┌──────────────────────────── COUCHE 2 — GITHUB ACTIONS ─────────────────────────────┐
│ npm ci → TypeScript → validation du contenu → tests unitaires → build              │
│        → tests de bout en bout (ordinateur + smartphone) → publication Pages       │
│ (le moindre échec arrête tout : la version en ligne reste la précédente)            │
└──────────────────────────────────────┬─────────────────────────────────────────────┘
                                       │
┌──────────────────────────── COUCHE 3 — GITHUB PAGES ───────────────────────────────┐
│ https://fomouborel.github.io/MYENDOACADEMY/  (HTTPS, gratuit)                      │
│ Navigateur de l'étudiante : application + IndexedDB (progression locale)           │
│ PWA : installable sur l'écran d'accueil, fonctionne hors connexion                  │
└────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Choix techniques et justification

| Brique | Choix | Pourquoi |
|---|---|---|
| Interface | React 19, TypeScript strict | composants réutilisables, erreurs détectées avant publication |
| Construction | Vite 8 | build rapide, chemin de base configurable (`BASE_PATH`) |
| Navigation | `HashRouter` (adresses en `#/…`) | fonctionne sur GitHub Pages sans configuration serveur, y compris après un rechargement ou depuis un favori (testé) |
| Validation des données | zod 4 | **un seul schéma** sert à la fois aux types de l'application, au validateur et à la vérification des sauvegardes importées |
| Stockage | IndexedDB, via la bibliothèque `idb` | grande capacité, transactions (une tentative et l'état de sa question sont toujours écrits ensemble) |
| Cours | Markdown, rendu par `react-markdown` + `remark-gfm` + `remark-directive` | blocs `:::archives`, `:::complement` et `:::validated` de la méthode, tableaux comparatifs |
| Hors connexion | `vite-plugin-pwa` (Workbox) | installation sur l'écran d'accueil et usage hors réseau |
| Tests | Vitest + fake-indexeddb, Playwright (Chromium ordinateur et Pixel 7) | tests de la logique et du parcours réel dans un navigateur |
| Style | CSS maison avec variables (bleu marine, turquoise, gris clair, blanc) | interface légère, aucune bibliothèque lourde |

**Note** : `npm audit` signale 6 alertes modérées ou faibles dans des outils de construction (`workbox-build` → `glob`/`minimatch`). Ces outils ne sont **pas livrés** dans l'application, donc les alertes sont sans effet pour l'étudiante. Je les surveillerai lors des mises à jour.

---

## 4. Organisation du dépôt

```
content/                        ← CONTENU (modifiable sans toucher au code)
  chapters.json                 chapitres → sous-chapitres → leçons
  exams.json                    sessions d'examen (composition annoncée ou null)
  questions/<source>.json       questions groupées par source (2026-01.json, nd-maiter.json…)
  lessons/<chapitre>/NN-<thème>.md
src/
  schemas/      content.ts, progress.ts   ← modèles de données (zod)
  data/         content.ts                ← chargement typé du contenu
  services/
    scoring/    score.ts                  ← correction selon la consigne, fiabilité
    progress/   questionState.ts, srs.ts, chapterMastery.ts, coverage.ts
    storage/    db.ts (IndexedDB), backup.ts (export / import)
    content/    validate.ts               ← règles du validateur
  features/     learning, quizzes, clinical-cases, exams, progress, revision   (phases 4 à 6)
  pages/ components/ hooks/ utils/ styles/
scripts/        validate-content.ts, audit/ (phase 1)
e2e/            tests de bout en bout
.github/workflows/  ci.yml (branches), deploy.yml (main → Pages)
docs/           audit, architecture, décisions
```

**Écart assumé avec l'exemple du prompt.** Le prompt range le contenu dans `src/data/`. Je le place dans `content/`, à la racine, comme dans la méthode Digest. On peut ainsi corriger une question ou un cours sans toucher au code. `src/data/` ne contient que le chargeur.

---

## 5. Modèle du contenu

### 5.1 Question (archive ou exercice)

Exemple de **format** : la question de janvier 2024 telle qu'inventoriée. Les indices et l'explication seront rédigés en phase 5.

```json
{
  "id": "ENDO-2024-01-ADULTE-QCM-031",
  "kind": "archive",
  "format": "mcq",
  "instruction": "one-false",
  "stem": "Une TSH abaissée peut être observée dans toutes ces situations, sauf une :",
  "options": [
    { "id": "A", "text": "Une hyperthyroïdite débutante" },
    { "id": "B", "text": "Au diagnostic d’une thyroïdite silencieuse" },
    { "id": "C", "text": "Au premier trimestre d’une grossesse" },
    { "id": "D", "text": "Dans une insuffisance antéhypophysaire traitée par L-thyroxyne" },
    { "id": "E", "text": "Lors d’une carence sévère en iode" }
  ],
  "expected": ["E"],
  "answerStatus": "proposed",
  "sourceComments": [],
  "provenance": {
    "session": "2024-01", "discipline": "ADULTE", "teacher": null, "formerTeacher": false,
    "sourceFile": "#Compilation endocrino 2016-2024.pdf", "page": 5, "originalNumber": 31,
    "auditRef": "2024-01-Q31"
  },
  "chapter": "thyroide", "subchapter": "explo",
  "lessonLinks": ["thyr-explo"], "tags": ["TSH"], "difficulty": 2,
  "duplicateGroup": "TSH-BASSE",
  "hints": ["…orientation générale…", "…rappel de cours…", "…aide précise sans la réponse…"],
  "explanation": { "text": "…", "status": "complement", "sources": [] }
}
```

| Champ | Règle |
|---|---|
| `id` | `ENDO-<SESSION>-<DISCIPLINE>-<TYPE>-<NNN>`. La session vaut `ND` pour la compilation 2016-2021. Un exercice créé prend `ENDO-EX-<chapitre>-…`. **Jamais réutilisé ni renuméroté**, car la progression enregistrée en dépend. |
| `kind` | `archive` (question réelle) ou `exercise` (exercice créé, toujours affiché comme tel) |
| `instruction` | consigne de l'examen : `one-correct`, `two-correct`, `one-false`, `two-false`, `one-true` ou `all-that-apply` |
| `expected` | propositions **à cocher selon la consigne**. Pour « une fausse », c'est la proposition fausse. |
| `answerStatus` | `official` · `proposed` · `disputed` · `deduced` · `absent` · `incomplete` · `authored` (exercices) |
| `answerNote` | **obligatoire** si la réponse est discutée, déduite, absente ou incomplète |
| `sourceComments` | commentaires des étudiants conservés tels quels (« pas sûr », « +1 »…) |
| `teacher` | **`null` si la source ne l'indique pas** : jamais déduit |
| `labs` | valeurs biologiques avec leur norme **et l'origine de la norme** (énoncé, laboratoire, référence vérifiée) |
| `qroc` | mots-clés, éléments indispensables, réponse modèle, erreurs graves, équivalents acceptables |
| `caseId` + `caseStep` | étapes d'un cas clinique progressif |
| `explanation.status` | `complement` (🟨 à valider) ou `validated` (🟩 relu). Les sources ne sont citées que si elles ont été vérifiées, avec la date de vérification. |

### 5.2 Formats de question et comportement de l'interface

| Format | Ce que fait l'étudiante | Correction |
|---|---|---|
| QCM à une réponse | coche 1 proposition | juste si c'est la proposition attendue |
| QCM « une fausse », « une vraie » | la consigne s'affiche en clair (« Cochez la proposition FAUSSE ») | idem |
| QCM « deux fausses » ou « deux bonnes » | coche 2 propositions. Le nombre est imposé par la consigne. | juste seulement si les deux sont exactes |
| Vrai ou faux | VRAI / FAUX | juste ou faux |
| QROC | réponse libre, puis comparaison avec la grille | **auto-évaluation**, jamais une note officielle |
| Cas clinique | étapes successives. Le diagnostic n'est révélé qu'après validation de l'étape. | par étape |
| Interprétation biologique | tableau de résultats avec les normes et leur origine | comme un QCM |

**Questions non jouables.** Une question incomplète ou sans réponse reste **consultable** dans « Anciens examens », avec son statut affiché. Elle est **exclue** de l'entraînement noté, des évaluations et des examens blancs (décision de la phase 1).

### 5.3 Validateur (`npm run validate:content`)

Le validateur bloque le déploiement si l'une de ces règles n'est pas respectée :

- **Identifiants** : uniques, avec un format conforme à la session et à la discipline.
- **Rattachement** :
  - chapitre et sous-chapitre existants ;
  - leçons liées existantes ;
  - session présente dans `exams.json`.
- **Cohérence entre statut et réponse** :
  - une réponse discutée, déduite, absente ou incomplète doit avoir une note ;
  - une réponse absente ne peut pas avoir de réponse attendue ;
  - le nombre de réponses doit correspondre à la consigne ;
  - une question à moins de 3 propositions doit être marquée incomplète.
- **Indices** : aucun indice ne recopie la proposition attendue ni ne cite une lettre de réponse.
- **Exercices créés** : identifiant `ENDO-EX-…`, statut `authored` et explication obligatoires. Un exercice ne peut pas se faire passer pour une question d'archives.
- **Règle pédiatrie** : une question pédiatrique ne peut se trouver que dans `hypo › congenitale` ou, plus tard, dans le chapitre `pediatrie`.
- **Leçons** : fichier présent, encadré `:::archives` et rubrique « À retenir » obligatoires.
- **Cas cliniques** : étapes continues (1, 2, 3…).

### 5.4 Les trois premiers modules (`content/chapters.json`)

| Chapitre | Sous-chapitres |
|---|---|
| `thyroide` Pathologies thyroïdiennes | `explo` · `nodules` · `cancers` · `thyroidites` · `goitre` |
| `hyper` Hyperthyroïdie | `diagnostic` · `basedow` · `iatrogene` |
| `hypo` Hypothyroïdie | `diagnostic` · `traitement` · `congenitale` (👶 Pédiatrie) |

- Les autres domaines (diabète, hypophyse, surrénales, gonades, obésité, phosphocalcique, pédiatrie, pharmacologie) sont **déclarés « pending »**. Ils s'affichent grisés, sans bouton factice.
- **Ajouter un domaine ne demande aucun code** : il suffit d'un chapitre, de ses leçons et de ses questions.

---

## 6. Gestion de la progression

### 6.1 Tentatives et statuts

- Une **tentative** n'existe que lorsque l'étudiante **valide** une réponse. Afficher une question n'a aucun effet sur les statistiques.
- Pour chaque tentative, on enregistre :
  - la question, la date et le mode ;
  - les propositions cochées (ou le texte libre) ;
  - le résultat (juste, faux ou non noté) ;
  - le nombre d'indices utilisés et la durée.

| Statut affiché | Règle |
|---|---|
| Non commencée | aucune tentative |
| En cours | réponse en brouillon dans un examen blanc ou un cas clinique non terminé |
| Réussie | dernière tentative juste |
| Échouée | dernière tentative fausse |
| À revoir | marquée par l'étudiante, **ou** date de révision atteinte pour une question réussie |
| Maîtrisée | ≥ 3 réussites, sur ≥ 2 jours différents, dernière réponse juste et boîte de révision ≥ 4 |

Une question réussie ou maîtrisée **ne disparaît jamais** : elle peut toujours être refaite.

### 6.2 Révision espacée (Leitner)

| Boîte | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Revient après | 1 jour | 3 jours | 7 jours | 14 jours | 30 jours |

- Bonne réponse **sans indice** : la question monte d'une boîte.
- Bonne réponse **avec indice(s)** : elle reste dans sa boîte.
- **Erreur** : elle retourne en boîte 1.

Les erreurs reviennent donc beaucoup plus souvent que les questions maîtrisées.

### 6.3 Carnet d'erreurs et révisions

Le carnet d'erreurs est **calculé à partir de l'historique des tentatives** : rien n'est dupliqué. Pour chaque erreur, il affiche :
- la question ;
- la réponse donnée et la réponse attendue, avec son statut de fiabilité ;
- l'explication et le chapitre ;
- la date et le nombre de tentatives ;
- le statut de révision.

Sessions de révision proposées :

| Session | Contenu |
|---|---|
| Erreurs récentes | erreurs des 7 derniers jours |
| Erreurs récurrentes | au moins 2 échecs |
| À revoir | questions dues ou marquées |
| Non maîtrisées | questions travaillées mais pas encore maîtrisées |
| Chapitres faibles | taux de réussite le plus bas |

### 6.4 Maîtrise d'un chapitre

| Niveau | Condition |
|---|---|
| Non commencé | aucune question travaillée |
| Découverte | au moins une question travaillée |
| En progression | ≥ 30 % des questions travaillées, réussite ≥ 50 % |
| Solide | ≥ 70 % travaillées, réussite ≥ 70 %, une évaluation finale ≥ 75 % |
| **Maîtrisé** | ≥ 80 % des questions **maîtrisées** et **deux** évaluations finales ≥ 75 % **à des jours différents** |

### 6.5 Couverture des archives

Le tableau de bord affiche, pour les questions d'archives :
- les questions disponibles et celles consultables seulement ;
- les questions travaillées, réussies et échouées ;
- celles qui restent à travailler, celles à revoir et celles maîtrisées.

Tous les chiffres sont calculés à partir des tentatives réelles. **Aucun chiffre n'est fictif.**

### 6.6 Parcours d'un chapitre (6 étapes, construites automatiquement)

| Étape | Questions utilisées |
|---|---|
| 1. Apprendre | leçons du chapitre, dans l'ordre |
| 2. Vérifier ma compréhension | questions jouables de difficulté 1, exercices « vrai ou faux » inclus |
| 3. M'entraîner | difficulté croissante (≤ 2), avec indices |
| 4. Niveau examen | toutes les questions d'archives jouables du chapitre, sans indice |
| 5. Évaluation finale | 15 questions mélangées, de formats variés, sans indice |
| 6. Bilan | score, points forts et lacunes par sous-chapitre, erreurs, questions d'examen non maîtrisées, niveau de maîtrise |

### 6.7 Examens blancs

Chaque examen blanc est enregistré avec :
- la liste des questions et les réponses en brouillon (sauvegarde continue : une coupure ne fait rien perdre) ;
- le chronomètre, l'heure de début et de fin ;
- le score.

Les corrections n'apparaissent **qu'à la fin**. Pour une session dont la composition est connue (mai 2023, janvier 2026), l'écran affiche « composition annoncée : … ; questions disponibles : … ». Une composition inconnue n'est jamais inventée.

---

## 7. Sauvegarde locale

- **Automatique** : chaque réponse validée est écrite immédiatement dans IndexedDB, dans une transaction qui enregistre à la fois la tentative et l'état de la question.
- **Persistance** : l'application demande au navigateur de ne pas effacer ses données (`navigator.storage.persist()`).
- **Export** : bouton « Télécharger ma sauvegarde », qui produit le fichier `endocrino-academy-sauvegarde-AAAA-MM-JJ.json`.
- **Import**, deux modes :
  - « **Ajouter** » (recommandé) : fusionne les tentatives sans doublon, puis recalcule les états à partir de l'historique complet. Aucune perte n'est possible.
  - « **Remplacer** » : demande une confirmation avant de tout remplacer.

  Un fichier invalide donne un message en français, sans jargon. Une sauvegarde venant d'une version plus récente de l'application est refusée.
- **Évolution du format** : le format a un numéro de version. Les changements sont gérés par des migrations qui ne suppriment jamais de progression.

**Limites à connaître**

1. **Pas de synchronisation entre appareils.** Pour passer de l'ordinateur au téléphone, il faut exporter puis importer.
2. **Navigateur.** Effacer les données de navigation efface la progression.
3. **Safari (iPhone, iPad).** Les données d'un site non installé peuvent être supprimées après une longue période sans visite. Je recommande :
   - d'**installer l'application sur l'écran d'accueil** (PWA) ;
   - d'exporter régulièrement.

   L'application affichera un rappel d'export.

---

## 8. Ce qui est déjà en place (et vérifié)

| Élément | Vérification |
|---|---|
| Correction selon la consigne (une fausse, deux fausses, vrai ou faux), questions non jouables jamais notées | tests unitaires |
| Statuts de question, Leitner, maîtrise (jamais après une seule réussite), couverture | tests unitaires |
| Maîtrise de chapitre (deux évaluations à des jours différents) | tests unitaires |
| IndexedDB : écriture, persistance après rechargement, export et import (remplacement et fusion), fichier invalide | tests unitaires (fake-indexeddb) |
| Validateur de contenu (8 familles de règles) | tests unitaires et `npm run validate:content` |
| Accueil (les 3 cours affichés comme « Intégration en cours »), page « Ma progression » (export et import réels) | tests de bout en bout sur ordinateur et smartphone |
| Rechargement direct d'une adresse (`#/progression`), absence de défilement horizontal sur mobile | tests de bout en bout |
| Build avec le chemin `/MYENDOACADEMY/`, PWA générée | `npm run build` |
| Workflow « Vérifications » sur la branche | **réussi sur GitHub Actions** (exécution n° 1, 10/11/2026) |

La navigation n'affiche que les rubriques qui fonctionnent réellement : Accueil et Ma progression. Les sept autres rubriques prévues apparaîtront au fur et à mesure (phases 4 à 6), **jamais sous forme de bouton factice**.

---

## 9. Intégration et déploiement continus

| Workflow | Déclenchement | Étapes | Permissions |
|---|---|---|---|
| `ci.yml` « Vérifications » | push sur une branche autre que `main`, pull requests | installation, TypeScript, validation du contenu, tests unitaires, build, tests de bout en bout | `contents: read` |
| `deploy.yml` « Déploiement GitHub Pages » | push sur `main` **et lancement manuel** | les mêmes étapes, **puis** publication sur GitHub Pages | `contents: read`, `pages: write`, `id-token: write` |

**Une action unique de votre part est nécessaire**, car je ne peux pas l'effectuer moi-même. Dans le dépôt GitHub, allez dans **Settings → Pages → Build and deployment → Source** et choisissez « **GitHub Actions** ». Cela se fait une seule fois. Ensuite, chaque modification validée sur `main` est publiée automatiquement.

**Publication sur `main`.** Je travaille sur la branche `claude/nice-mendel-6foiq0`. Pour publier, il faut fusionner cette branche dans `main`, et je ne le fais pas sans votre accord explicite. Deux options :
- (a) vous m'autorisez à fusionner dans `main` à la fin de chaque phase validée ;
- (b) j'ouvre une pull request que vous fusionnez.

---

## 10. Confidentialité et étude de Cloudflare Access

### 10.1 Situation actuelle

- Le dépôt `fomouborel/MYENDOACADEMY` est **public**. Tout son contenu est lisible par n'importe qui, y compris l'archive `Source Endocrino Academie.zip`, qui contient des prénoms et noms d'étudiants ayant participé aux retranscriptions.
- Sur un compte gratuit, GitHub Pages **n'est disponible que pour les dépôts publics**. Avec un dépôt privé, il faut un abonnement GitHub Pro, ce qui sort du cadre du coût zéro.
- Un site GitHub Pages est **public**. Un faux écran de connexion ne protégerait rien, donc je n'en ai pas créé.
- L'application ne stocke **aucune donnée personnelle sur un serveur** : la progression reste dans le navigateur de l'étudiante. Une personne qui trouverait l'adresse verrait les cours et les questions, mais **jamais la progression**.

### 10.2 Options étudiées

| | A. GitHub Pages public (actuel) | B. Cloudflare Pages + Cloudflare Access | C. GitHub Pages + domaine personnel + Cloudflare Access |
|---|---|---|---|
| Coût | 0 € | 0 € (offre Zero Trust gratuite, moins de 50 utilisateurs) | **domaine payant**, environ 10 à 15 € par an |
| Carte bancaire | non | **probablement demandée** lors de l'inscription Zero Trust, même pour l'offre gratuite (non débitée), selon la documentation Cloudflare. Je n'ai pas pu le confirmer sur la page officielle (non accessible depuis cet environnement). | oui (domaine) |
| Accès réservé | non : l'adresse est publique, et un avertissement « noindex » limite seulement l'indexation par les moteurs de recherche | oui : connexion par **code envoyé par e-mail** à une liste d'adresses autorisées | oui |
| Dépôt privé possible | non | **oui** (Cloudflare déploie depuis un dépôt privé) | non sans GitHub Pro (sinon le dépôt reste public) |
| Contraintes | aucune | compte Cloudflare, jeton d'API stocké en secret GitHub, deux règles Access (domaine `*.pages.dev` et aperçus), adresse en `…pages.dev` ; la couche 3 n'est plus GitHub Pages | DNS du domaine chez Cloudflare ; il faut vérifier que l'adresse `github.io` redirige bien vers le domaine protégé |
| Ce que voit l'étudiante | ouvre l'adresse | saisit son e-mail, reçoit un code, puis la session reste ouverte (durée configurable) | idem B |
| Effort de mise en place | fait | environ une demi-journée pour moi, plus la création du compte par vous | B + achat du domaine |

### 10.3 Recommandation

1. **V1 sur l'option A** : elle est gratuite, sans carte bancaire et déjà prête. Le code est **portable** : passer à B ne demande que de changer `BASE_PATH` et le workflow, sans toucher à l'application.
2. **Retirer l'archive source du dépôt public**, ou au minimum la remplacer par une version sans noms d'étudiants. Attention : un fichier déjà poussé reste dans l'historique Git. Le supprimer complètement exige de réécrire l'historique, une opération à faire **seulement avec votre accord explicite**. Alternative : créer un nouveau dépôt propre.
3. Si un accès strictement réservé devient indispensable, choisir l'**option B** après avoir vérifié vous-même si Cloudflare demande une carte bancaire. Rien ne sera fait sans votre accord.

---

## 11. Suite : phase 3 (conception pédagogique)

1. Plan détaillé des leçons des 3 cours (4 à 5 leçons par cours, 8 à 15 minutes chacune). Chaque leçon commence par l'encadré « Ce que les archives interrogent », construit à partir des familles de l'audit.
2. Rédaction selon le gabarit de la méthode :
   - explication simple, puis physiopathologique ;
   - exemple clinique et éléments biologiques ;
   - pièges classiques et « À retenir » ;
   - tableaux comparatifs (étiologies d'hyperthyroïdie selon la clinique, la biologie, les anticorps et la scintigraphie ; hypothyroïdie primaire ou centrale).
3. Provenance visible sur chaque bloc. Aucune valeur de référence ni recommandation sans source vérifiée.
4. Association des 134 questions de thyroïde aux notions des leçons.

---

### Sources consultées pour le § 10

- Offre Cloudflare Zero Trust (gratuite pour moins de 50 utilisateurs, puis 7 $ par utilisateur et par mois) : [cloudflare.com/teams-access](https://www.cloudflare.com/teams-access/) · [costbench.com](https://costbench.com/software/business-vpn/cloudflare-zero-trust/free-plan/)
- Moyen de paiement demandé à l'inscription, même pour l'offre gratuite : documentation Cloudflare One « Get started » (copie de prévisualisation : [developers.cloudflare.com/cloudflare-one/setup](https://f75b423c.previews.developers.cloudflare.com/cloudflare-one/setup/index.md)), **à confirmer sur la page officielle**
- Protection d'un site Cloudflare Pages par Access : [Known issues](https://developers.cloudflare.com/pages/platform/known-issues/) · [Preview deployments](https://developers.cloudflare.com/pages/configuration/preview-deployments/)
