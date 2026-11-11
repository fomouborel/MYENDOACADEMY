# ENDOCRINO ACADEMY — Décisions validées

Ce fichier rassemble les décisions prises avec l'utilisatrice ou l'utilisateur, pour qu'elles soient appliquées même lors d'une session de travail ultérieure. Les détails sont dans les rapports de chaque phase.

## Pédiatrie (décision du 11 novembre 2026)

**Tout ce qui concerne la pédiatrie va dans le cours d'endocrinologie pédiatrique** (chapitre `pediatrie`), et non dans les cours d'organe.

- **Surrénales, hypophyse et les domaines à venir** : les questions de pédiatrie (discipline `PEDIA`) sont réservées au cours de pédiatrie. Elles sont inventoriées mais pas encore intégrées (14 pour les surrénales, voir `DOMAINE-SURRENALES.md`).
- **Thyroïde** : en phase 1, les questions de pédiatrie sur la thyroïde avaient été placées dans `hypo › congenitale`, avec la leçon « Hypothyroïdie congénitale et thyroïde de l'enfant » (`hypo-congenitale`). **Au moment d'intégrer le cours de pédiatrie, ce contenu y sera basculé** :
  - les questions de pédiatrie sur la thyroïde (Lysy, Beauloye) et la leçon `hypo/04-congenitale-enfant.md` passent dans le chapitre `pediatrie` ;
  - les **identifiants des questions ne changent pas** : la progression déjà enregistrée (réponses, révisions, erreurs) est conservée ;
  - le cours « Hypothyroïdie » garde un renvoi vers la leçon déplacée ;
  - la règle du validateur (`src/services/content/validate.ts`) est alors simplifiée : toute question `PEDIA` doit être dans le chapitre `pediatrie`.

## Rappels des décisions antérieures

- Les questions de l'ancien titulaire (Beauloye) sont conservées, avec la mention « ancien titulaire ».
- Les questions incomplètes ou sans réponse sont consultables, mais non notées.
- Les sessions 2025 et 2026 sont incluses.
- Les identifiants suivent la méthode `ENDO-<session>-<discipline>-<type>-<numéro>`.
- Le site GitHub Pages est public pour la première version.
