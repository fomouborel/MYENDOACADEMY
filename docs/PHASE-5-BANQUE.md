# ENDOCRINO ACADEMY — Banque d'anciens examens : thyroïde (phase 5)

> Date : 11 novembre 2026 · Rubrique en ligne : « 🗂️ Anciens examens »

## 1. Couverture des archives

Commande de contrôle : `npx tsx scripts/content/coverage.ts`.

| | Nombre |
|---|---:|
| Questions de thyroïde inventoriées à l'audit | 134 |
| — dont non retranscrites (seul le nom du transcripteur figure) | 1 |
| **Questions intégrées dans l'application** | **133 / 133 (100 %)** |
| — **notées** (complètes, avec une réponse cohérente avec la consigne) | **81** |
| — **consultables seulement** (incomplètes, sans réponse, ou réponse discutée incohérente avec la consigne) | **52** |
| — avec indices et explication rédigée | 30 |
| Exercices créés (hors archives) | 15 |

Aucune question exploitable n'est supprimée. Les doublons sont conservés et reliés : sur la page d'une question, la rubrique « Même thème dans d'autres sessions » liste les autres occurrences.

### Répartition

| Session | 2026-01 | 2025-01 | 2024-01 | 2023-05 | 2022-05 | 2016-2021 (ND) |
|---|---:|---:|---:|---:|---:|---:|
| Questions | 10 | 11 | 12 | 14 | 8 | 78 |

| Fiabilité de la correction | Questions |
|---|---:|
| Correction officielle | 0 |
| Réponse proposée par la compilation | 69 |
| Réponse discutée | 14 |
| Question incomplète | 41 |
| Réponse absente | 9 |

| Chapitre | Questions | Notées |
|---|---:|---:|
| Pathologies thyroïdiennes | 69 | 47 |
| Hyperthyroïdie | 20 | 13 |
| Hypothyroïdie | 44 | 21 |

Par discipline : 73 adulte, 26 pédiatrie, 15 radiologie, 13 anatomie pathologique, 6 pharmacologie.

## 2. Ce qui est préservé pour chaque question

- **Énoncé et propositions originaux**, avec seulement trois types de corrections techniques :
  - retours à la ligne du PDF ;
  - lettres de propositions perdues à l'extraction ;
  - texte de la question suivante qui débordait.

  Les commentaires de transcripteurs insérés dans le texte, comme « (pas sûre) » ou « (soit ça, soit la A) », sont conservés.
- **Provenance** :
  - session ;
  - discipline ;
  - professeur, seulement s'il est indiqué dans la source, sinon « non attribué » ;
  - mention « ancien titulaire » pour Beauloye ;
  - fichier source, page, numéro d'origine et référence d'audit.
- **Commentaires des étudiants** (« +1 », « possiblement annulée », doutes) dans le champ `sourceComments`.
- **Statut de fiabilité** vérifié en phase 1, avec une note explicative quand la réponse est discutée, absente ou incomplète.

## 3. Rubrique « Anciens examens »

- **Filtres** :
  - année ou session ;
  - discipline, professeur ;
  - chapitre, sous-chapitre ;
  - type de question, difficulté ;
  - **mon statut** : non commencée, en cours, réussie, échouée, à revoir, maîtrisée ;
  - **fiabilité** ;
  - public adulte ou pédiatrie ;
  - recherche plein texte (sans accents).
- **Session choisie** : la composition **annoncée** et le nombre de questions non retranscrites s'affichent, avec l'avertissement « la session n'est pas complète ». Aucune composition n'est inventée.
- **Question notée** : réponse, indices s'ils existent, correction avec le statut de fiabilité, lien vers la leçon.
- **Question consultable** : affichage en lecture seule. Une éventuelle réponse marquée apparaît comme « marquée en rouge dans la compilation (non officielle) ». Aucune note n'est donnée.
- **« Travailler ces questions »** lance une série avec les questions notées de la sélection (50 au maximum).

## 4. Contrôles qualité

- **Import** (`scripts/content/import_audit.py`) :
  - découpage des propositions sur plusieurs lignes ;
  - puces seules sur leur ligne ;
  - propositions notées « => » ;
  - débordements de la question suivante ;
  - cohérence entre la consigne et le nombre de réponses marquées : en cas d'écart, la question est classée « discutée », consultable mais non notée.

  Les 47 questions notées importées ont été **relues une par une** (propositions et réponse attendue).
- **Validateur** : 148 questions valides.
- **Tests** : 39 tests unitaires et 22 tests de bout en bout (ordinateur et smartphone), dont les filtres de la banque, une question consultable non notée, une question « deux fausses » et le filtre « ancien titulaire ».

## 5. Limites et suite

- **51 questions notées n'ont pas encore d'indices ni d'explication rédigée.** La correction affiche la réponse proposée, son statut et la leçon liée. La rédaction se poursuit chapitre par chapitre ; chaque explication restera 🟨 « à valider ».
- Les autres domaines (diabète, hypophyse, surrénales…) sont inventoriés, mais pas encore intégrés.
- **Phase 6** :
  - cas cliniques progressifs ;
  - examens blancs chronométrés ;
  - Mes erreurs ;
  - Mes révisions (répétition espacée déjà prête) ;
  - évaluation finale de chapitre ;
  - tableau de bord complet.
