# ENDOCRINO ACADEMY — Intégration du domaine « Hypophyse »

> Date : 11 novembre 2026
> Deuxième domaine intégré après la thyroïde, selon la même méthode : audit, plan, leçons, banque de questions, explications, tests.
> **Toutes les explications sont des compléments « à valider »** 🟨 : aucune n'a été relue par un enseignant.

## 1. Ce qui est disponible

| Élément | Contenu |
|---|---|
| **Cours « Hypophyse »** | 7 leçons (67 minutes de lecture), un nouveau cours dans « Mes cours » |
| **Questions d'archives** | **88**, dont **73 jouables** (avec indices, explication et une remarque par proposition) et 15 seulement consultables |
| **Exercices vrai ou faux** | 14 (deux par leçon), créés pour l'étape « Vérifier ma compréhension » |
| **Rubriques** | les questions apparaissent aussi dans « Anciens examens », « Entraînement », « Examens blancs », « Mes erreurs » et « Mes révisions » |

### Les 7 leçons

| # | Leçon | Questions d'archives liées |
|---|---|---:|
| 1 | Anatomie, physiologie et imagerie (IRM, rehaussement, loge hypophysaire) | 22 |
| 2 | Adénomes, syndrome tumoral, apoplexie, craniopharyngiome, métastases | 34 |
| 3 | Hyperprolactinémie et prolactinome (causes, agonistes dopaminergiques, grossesse) | 16 |
| 4 | Acromégalie et somatostatine | 18 |
| 5 | Maladie et syndrome de Cushing | 9 |
| 6 | Insuffisance antéhypophysaire (Sheehan, ordre de substitution) | 7 |
| 7 | Posthypophyse et diabète insipide | 6 |

Une question peut être liée à plusieurs leçons. Le syndrome de Cushing est traité ici parce que les archives le classent dans la partie « Hypophyse » (Maiter) ; ses causes surrénaliennes seront détaillées dans le cours « Surrénales ».

## 2. Audit des questions

- **90 questions** ont été classées automatiquement dans le domaine « Hypophyse » lors de l'audit de la phase 1. Je les ai relues une par une (classement manuel dans `scripts/audit/hypophyse.py`).
- **4 relèvent d'un autre domaine** et y restent : 3 questions de pédiatrie sur la croissance et la puberté, et 1 sur les NEM et le phéochromocytome.
- **1 question a été rattachée** depuis les surrénales (lors de l'intégration de ce domaine) : un adénome hypophysaire silencieux, classé « Surrénales » par l'extraction. Sa correction est discutée.
- **1 question a été rattachée** depuis « non classable » (lors de l'intégration de la pharmacologie) : l'IRM ne distingue pas un adénome sécrétant d'un adénome non sécrétant. Propositions mal retranscrites : consultable.
- **Inventaire détaillé** : `docs/audit/INVENTAIRE-HYPOPHYSE.md` (et `inventaire-hypophyse.csv`).

| Statut des 88 questions | Nombre |
|---|---:|
| 🟦 réponse proposée dans la compilation | 66 |
| 🟧 réponse discutée | 10 |
| ⬜ question incomplète (consultable) | 11 |
| 🟥 réponse absente (consultable) | 1 |

Aucune correction officielle n'existe dans les sources.

## 3. Corrections discutées

Chaque explication présente les deux versions et ce qui est le plus défendable sur le fond, **sans changer la réponse retenue**.

| Question | Problème |
|---|---|
| `2023-05-Q13` (adénome non fonctionnel) | deux réponses en rouge, dont « TSH normale, T4 basse », pourtant possible : seulement consultable |
| `ND-maiter-hypophyse-Q20` (acromégalie) | « syndrome métabolique » retenu comme faux, discutable |
| `ND-maiter-hypophyse-Q24` (diagnostic du Cushing) | « ACTH très bas » n'est pas non plus un test de dépistage |
| `ND-maiter-hypophyse-Q29` (maladie de Cushing) | trois réponses en rouge pour « deux fausses » : seulement consultable |
| Somatostatine (4 questions) | les diarrhées sont aussi un effet réel ; l'hypoglycémie est possible |
| `2025-01` diabète insipide (p. 18) | deux réponses en rouge pour une seule fausse : seulement consultable |
| `ND-maiter-hypophyse-Q15` (hypogonadisme central) | « alcool et autres drogues » peut aussi être une cause centrale (opioïdes) : requalifiée « discutée » |

## 4. Corrections de l'import, sans toucher au texte original

La relecture a révélé des défauts de découpage de l'extraction, corrigés dans `scripts/content/import_audit.py` :

- **3 questions** où une lettre de proposition s'était perdue : deux propositions avaient fusionné ;
- **2 questions** où énoncé et propositions étaient mélangés ;
- **6 consignes** mal reconnues (« Deux justes », « 2 F », « 2 propositions fausses », « n'apparaît pas »…) ;
- **un défaut du script** : quand deux propositions commençaient par les mêmes mots, la bonne réponse pouvait être attachée à la mauvaise lettre. Corrigé et vérifié sur la thyroïde : une seule question y était touchée, déjà en consultation seule.

## 5. Améliorations de l'application

- **Plus de bouton vers une liste vide** : une étape de cours sans question affiche « Pas encore de questions de ce type pour ce cours ».
- **Textes automatiques** : l'accueil, « Anciens examens » et « Examens blancs » citent les domaines réellement intégrés (« thyroïde et hypophyse »), au lieu d'un texte écrit pour la thyroïde seule.
- **Tests** : les pages de l'hypophyse sont ajoutées aux contrôles d'accessibilité et d'affichage sur téléphone.

## 6. Références vérifiées (le 11/11/2026, niveau bibliographique)

| Thème | Référence |
|---|---|
| Classification | Asa SL et al. (OMS 2022), Endocr Pathol 2022;33:6-26 |
| Incidentalome | Freda PU et al. (Endocrine Society), J Clin Endocrinol Metab 2011;96:894-904 |
| Apoplexie | Rajasekaran S et al. (recommandations britanniques), Clin Endocrinol 2011;74:9-20 |
| Hyperprolactinémie | Melmed S et al. (Endocrine Society), J Clin Endocrinol Metab 2011;96:273-288 |
| Prolactinome | Petersenn S et al. (Pituitary Society), Nat Rev Endocrinol 2023;19:722-740 |
| Acromégalie | Katznelson L et al. (Endocrine Society), J Clin Endocrinol Metab 2014;99:3933-3951 ; Giustina A et al., Pituitary 2024;27:7-22 |
| Cushing | Nieman LK et al. (Endocrine Society), J Clin Endocrinol Metab 2008;93:1526-1540 ; Fleseriu M et al., Lancet Diabetes Endocrinol 2021;9:847-875 |
| Insuffisance hypophysaire | Fleseriu M et al. (Endocrine Society), J Clin Endocrinol Metab 2016;101:3888-3921 |
| Diabète insipide | Fenske W et al., N Engl J Med 2018;379:428-439 ; Arima H et al., Endocr Connect 2022;11:e220378 |

**Valeurs signalées « à valider » dans le texte** : le seuil d'environ 250 µg/L de prolactine en faveur d'un prolactinome (leçon 3) et la cible de T4 libre dans la moitié supérieure de la norme (leçon 6).

## 7. Pour refaire ou corriger

1. Audit : `scripts/audit/hypophyse.py` (classement), puis `python3 scripts/audit/domain_audit.py W hypophyse`.
2. Import : `python3 scripts/content/import_audit.py hypophyse`. Les questions déjà présentes ne sont jamais réécrites.
3. Explications : `scripts/content/explications/hypophyse.py`, puis `python3 scripts/content/add_explanations.py`.
4. Exercices vrai ou faux : `scripts/content/build_questions.py`.
