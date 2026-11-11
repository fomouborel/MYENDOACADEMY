# ENDOCRINO ACADEMY — Prototype fonctionnel (phase 4)

> Date : 11 novembre 2026 · Adresse : https://fomouborel.github.io/MYENDOACADEMY/
> **Statut** : premier parcours complet utilisable. Il faut votre validation avant de généraliser (phase 5 : banque complète de thyroïde).

## 1. Ce qui fonctionne

| Rubrique | Contenu |
|---|---|
| **Menu** | Menu latéral bleu marine, rubrique active en turquoise. Sur téléphone, il s'ouvre par le bouton ☰. Seules les rubriques qui fonctionnent sont affichées : Accueil, Mes cours, Entraînement, Ma progression. |
| **Accueil** | Les 3 cours de thyroïde avec l'avancement réel des leçons ; « Pour continuer » mène à la prochaine leçon non terminée ; couverture des archives. |
| **Mes cours** | 3 cours ouverts, 8 domaines « intégration en cours » non cliquables. |
| **Page d'un cours** | Parcours : 1. Apprendre (leçons cochées quand elles sont terminées) · 2. Vérifier ma compréhension (vrai ou faux) · 3. M'entraîner (avec indices) · 4. Niveau examen (vraies questions, sans indice) · Bilan par sous-chapitre. |
| **Leçon** | Rendu fidèle, avec les blocs 🟦 archives et 🟨 « à valider ». Tableaux défilants sur téléphone, questions de compréhension dépliables, bouton « J'ai terminé cette leçon », exercices liés à la leçon, leçon précédente et suivante. |
| **Question** | Consigne adaptée à l'énoncé (« Cochez la proposition FAUSSE », « les deux FAUSSES » : exactement 2 cases). 3 indices progressifs (désactivés au niveau examen). Pas de correction sans tentative. |
| **Correction** | Bonne ou mauvaise réponse, réponse attendue avec son **statut de fiabilité** (« Réponse proposée (compilation) — non officielle »), verdict et justification pour chaque proposition, explication 🟨, piège à éviter, source (fichier, page), lien « Revoir la leçon », bouton « Marquer à revoir ». |
| **Entraînement** | Choix des cours, du public (adulte ou pédiatrie), des questions (toutes, jamais faites, échouées, à revoir), du type (archives ou exercices) et du nombre. |
| **Ma progression** | Couverture des archives (disponibles, travaillées, réussies, échouées, à revoir, maîtrisées, restantes), niveau par cours, sauvegarde et restauration. |

## 2. Contenu intégré pour le prototype

- **30 questions d'anciens examens** de thyroïde, environ 10 par cours :
  - énoncés et propositions **originaux** ;
  - réponse **proposée par la compilation** ;
  - 3 indices, justification de chaque proposition, explication « à valider » ;
  - **valeurs biologiques** avec la norme et son origine (« énoncé »).
- **15 exercices vrai ou faux**, créés pour l'étape « Vérifier ma compréhension ». Ils sont signalés « Exercice d'entraînement (hors archives) ».
- Générateur : `scripts/content/build_questions.py`.

## 3. Garanties vérifiées par les tests

- **35 tests unitaires et 16 tests de bout en bout** (ordinateur et smartphone).
- Parcours testé de bout en bout :
  1. on lit une leçon et on la marque comme terminée ;
  2. on répond à des vrai ou faux avec indices ;
  3. on répond à une vraie question d'examen sans indice, et la correction affiche bien « non officielle » ;
  4. la progression survit au rechargement de la page.
- **Une réponse affichée comme corrigée est toujours sauvegardée** : l'enregistrement a lieu avant l'affichage de la correction. Ce défaut a été trouvé et corrigé pendant les tests.
- Un double-clic sur « Valider » ne crée pas deux tentatives.
- Aucun défilement horizontal sur téléphone ; les adresses directes fonctionnent après rechargement.

## 4. Limites connues du prototype

- Rubriques pas encore ouvertes : Anciens examens, Cas cliniques, Examens blancs, Mes erreurs, Mes révisions (phases 5 et 6).
- Évaluation finale (étape 5 du parcours) et bilan détaillé : phase 6.
- Pas encore d'illustrations anatomiques dessinées.
- La taille du fichier de l'application (environ 280 Ko compressés) reste raisonnable sur téléphone.

## 5. Ce que je vous demande de tester

1. Sur téléphone : ouvrir le menu ☰, lire une leçon, la marquer terminée.
2. Faire « Vérifier ma compréhension », puis « Niveau examen » dans un cours.
3. Regarder « Ma progression ».
4. Me dire ce qui gêne ou manque : lisibilité, taille des boutons, formulations, couleurs.
