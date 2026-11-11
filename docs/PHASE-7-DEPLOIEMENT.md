# ENDOCRINO ACADEMY — Tests et déploiement final (phase 7)

> Date : 11 novembre 2026
> **Adresse de l'application : https://fomouborel.github.io/MYENDOACADEMY/**
> Le déploiement GitHub Pages est confirmé par l'API GitHub : statut « success » et adresse ci-dessus. L'environnement de développement ne peut pas ouvrir le site lui-même ; la vérification visuelle finale se fait sur vos appareils.

## 1. Vérifications effectuées

| Point du cahier des charges (§ 16) | Comment c'est vérifié | Résultat |
|---|---|---|
| Navigation (9 rubriques, menu ☰ sur téléphone) | tests de bout en bout | ✅ |
| Affichage des cours et des unités pédagogiques (13 leçons) | parcours de bout en bout, analyse Markdown, validateur | ✅ |
| QCM simples, QCM multiples (« deux fausses »), vrai ou faux | tests unitaires de correction et tests de bout en bout | ✅ |
| QROC | **sans objet** : les examens sont exclusivement des QCM (phase 1). Le format est prévu dans le modèle (grille de mots-clés, auto-évaluation). | — |
| Cas cliniques progressifs | test « aucune étape révélée avant la réponse » | ✅ |
| Indices (3 niveaux, désactivés au niveau examen) | tests de bout en bout | ✅ |
| Corrections (fiabilité affichée, « non officielle ») | tests de bout en bout | ✅ |
| Calcul des scores, statuts, maîtrise, révision espacée | tests unitaires | ✅ |
| Sauvegarde locale et persistance après rechargement | tests unitaires et de bout en bout | ✅ |
| Importation et exportation (remplacement, fusion, fichier invalide) | tests unitaires et de bout en bout | ✅ |
| Suivi des questions et couverture des archives | tests unitaires | ✅ |
| Carnet d'erreurs, révisions | tests unitaires et de bout en bout | ✅ |
| Examens blancs (sans correction pendant, reprise, chronomètre) | tests de bout en bout | ✅ |
| Responsive (aucun défilement horizontal sur 9 pages) | tests de bout en bout sur smartphone (Pixel 7) | ✅ |
| **Accessibilité** (WCAG 2 A/AA, violations graves ou critiques) sur 13 pages | axe-core, sur ordinateur et smartphone | ✅ 0 violation |
| **Hors connexion** (PWA) | test : rechargement et ouverture d'une leçon sans réseau | ✅ |
| Build, chemins GitHub Pages (`/MYENDOACADEMY/`) | `npm run build`, test « rechargement direct d'une adresse » | ✅ |
| Déploiement automatique | GitHub Actions : vérifications, puis publication sur `main` | ✅ |

**Bilan chiffré** : 49 tests unitaires et 32 tests de bout en bout (16 scénarios × 2 appareils).

**Défauts corrigés grâce à ces tests (phases 4 à 7)** :
- une réponse pouvait être perdue si l'on quittait la page juste après avoir validé ;
- double enregistrement en cas de double-clic ;
- débordements horizontaux sur téléphone ;
- contraste insuffisant de deux textes ;
- tableaux défilants non accessibles au clavier ;
- barre de progression sans nom accessible.

## 2. Ajouts de cette phase

- **Rappel de sauvegarde** : après 20 réponses, si aucune sauvegarde n'a été téléchargée, ou si la dernière date de plus de 14 jours, un message apparaît sur l'accueil et dans « Ma progression ».
- **Mode d'emploi** (lien « ❔ Mode d'emploi » en bas du menu), sans jargon : par où commencer, signification des couleurs, sauvegarde, installation sur iPhone ou Android, que faire si une question semble fausse.

- **Explications des questions importées** (après la phase 7) : 51 questions complétées, 33 pour le cours 1 et 18 pour les cours 2 et 3.
  - Les textes sont dans `scripts/content/explications/*.py`, et `scripts/content/add_explanations.py` les reporte dans `content/questions/import-*.json`. Ce script est relançable et ne touche ni aux énoncés, ni aux propositions, ni aux réponses.
  - Quand la correction est discutée, l'explication présente les deux versions et ce qui est le plus défendable sur le fond, sans jamais changer la réponse retenue.
  - Une seule question a changé de statut, de « proposée » à « discutée » : l'anatomie pathologique de Basedow en janvier 2025, déjà signalée dans la leçon Thyroïdites.
  - Défauts de retranscription signalés dans l'explication, sans modifier la question :
    - mai 2022, pédiatrie : la proposition A est en réalité la fin de l'énoncé ;
    - janvier 2025, pédiatrie : la proposition F est un commentaire du transcripteur ;
    - une question de l'ancien titulaire réunit deux propositions en une seule.

## 3. Limites à connaître

1. **Pas de synchronisation entre appareils** : il faut passer par la sauvegarde (export sur un appareil, import sur l'autre).
2. **Effacer les données du navigateur efface la progression.** Sur iPhone, installer l'application sur l'écran d'accueil protège mieux les données.
3. **Site public** : toute personne qui connaît l'adresse peut voir les cours et les questions, jamais la progression. Voir l'étude Cloudflare Access (phase 2, § 10).
4. **Corrections non officielles** : 0 correction officielle dans les sources. 14 réponses sont discutées et 52 questions ne sont que consultables.
5. **Explications** : toutes les questions d'examen notées ont désormais 3 indices, une explication et une remarque par proposition (complété après la phase 7, en deux lots). **Toutes ces explications sont « à valider »** : aucune n'a été relue par un enseignant. Un test empêche désormais d'ajouter une question notée sans explication.
6. **Périmètre** : la thyroïde, l'hypophyse, les surrénales et la pharmacologie générale (voir les rapports `DOMAINE-*.md`). Les autres domaines sont inventoriés (phase 1), mais pas encore intégrés.
7. **Taille** : l'application pèse environ 300 Ko compressés. Elle reste utilisable hors connexion après la première visite.
