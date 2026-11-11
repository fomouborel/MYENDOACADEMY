# ENDOCRINO ACADEMY — Fonctionnalités complètes (phase 6)

> Date : 11 novembre 2026 · Les **9 rubriques** du cahier des charges sont en service.

## 1. Ce qui a été ajouté

| Rubrique ou fonction | Contenu |
|---|---|
| **Parcours d'un cours, étape 5 : évaluation finale** | 15 questions mélangées (anciens examens et exercices de formats variés), sans indice. Les corrections s'affichent à la fin. Le score est enregistré et compte pour la maîtrise du cours. |
| **Parcours d'un cours, étape 6 : bilan** | Niveau de maîtrise, points forts et lacunes par sous-chapitre, notions (leçons) à revoir, erreurs en cours, questions d'examen pas encore maîtrisées, avec des liens pour les retravailler. |
| **🩺 Cas cliniques** | 3 cas progressifs (Basedow ; hypothyroïdie centrale ; nodule puis cancer papillaire), soit 11 étapes. Chaque étape se débloque après la réponse ; le diagnostic n'est jamais révélé avant. Les tableaux biologiques affichent les normes et leur origine. La rubrique liste aussi les cas cliniques des anciens examens. |
| **⏱️ Examens blancs** | Composition au choix (mélange des 3 cours, une session, un professeur), nombre de questions, chronomètre. Aucune correction pendant l'examen. Brouillon enregistré à chaque clic, avec l'indication « ✓ réponses enregistrées » ; reprise possible après une interruption. Remise automatique à la fin du temps, puis correction détaillée et historique des examens. |
| **❗ Mes erreurs** | Toutes les erreurs, même corrigées ensuite. Pour chacune : la question, la réponse donnée, la réponse attendue et son statut de fiabilité, l'explication, le chapitre, la date, le nombre d'échecs et de tentatives, le statut de révision. Filtres : non corrigées, récurrentes, par cours. Bouton « Retravailler ces erreurs ». |
| **🔁 Mes révisions** | Révision espacée : à revoir aujourd'hui, erreurs récentes (7 jours), erreurs récurrentes, questions non maîtrisées, chapitre le plus faible. Les questions échouées passent en premier. Calendrier des 7 prochains jours. |
| **🏠 Tableau de bord** | Reprendre la leçon en cours, révisions du jour, avancement des 3 cours, couverture des archives, taux de réussite, niveau par cours (maîtrisés et à renforcer), dernières erreurs, prochaines révisions, activité des 7 derniers jours. |

**Tous les chiffres viennent des réponses réelles.** Aucun chiffre n'est fictif. Une question simplement affichée, ou laissée sans réponse dans un examen blanc, n'est pas comptée comme travaillée.

## 2. Règles de fiabilité respectées

- **Examen blanc construit à partir d'une session** : la composition **annoncée** est affichée, avec la mention qu'il ne s'agit **pas** de la reproduction complète de l'examen officiel (seule la thyroïde est intégrée).
- **Cas cliniques** : ils sont créés pour l'entraînement et signalés « hors archives ». Leurs normes biologiques sont reprises d'un énoncé d'examen UCL et présentées comme propres au laboratoire de l'exercice.
- **Étapes de cas cliniques** : elles ne sont jamais tirées isolément dans les séries d'entraînement, car elles dépendent de l'étape précédente.
- **Maîtrise d'un cours** : il faut 80 % de questions maîtrisées dans la durée **et** deux évaluations finales réussies (≥ 75 %) à des jours différents.

## 3. Qualité

- **46 tests unitaires et 28 tests de bout en bout** (ordinateur et smartphone). Ils couvrent :
  - le cas progressif sans révélation anticipée ;
  - l'examen blanc sans correction pendant l'épreuve, avec reprise du brouillon après rechargement ;
  - l'évaluation finale ;
  - le carnet d'erreurs (réponse donnée affichée) ;
  - les révisions et le tableau de bord ;
  - l'absence de défilement horizontal sur les 9 rubriques.
- **Défauts trouvés et corrigés pendant les tests** :
  - débordement horizontal de la page d'un cours et de la liste des sessions sur téléphone ;
  - risque de perdre une réponse d'examen blanc en rechargeant au moment exact du clic.

## 4. Suite possible (phase 7 : tests et déploiement final)

- Rédaction des indices et explications des 51 questions d'archives notées qui n'en ont pas encore.
- Relecture médicale des contenus (passage de 🟨 « à valider » à 🟩 « validé »).
- Intégration des autres domaines (diabète, hypophyse, surrénales…), déjà inventoriés.
- Vérification finale sur les vrais appareils de l'étudiante, et rappel d'export régulier de la sauvegarde.
