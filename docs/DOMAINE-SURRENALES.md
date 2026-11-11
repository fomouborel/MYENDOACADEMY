# ENDOCRINO ACADEMY — Intégration du domaine « Surrénales »

> Date : 11 novembre 2026
> Troisième domaine intégré, selon la même méthode que la thyroïde et l'hypophyse.
> **Toutes les explications sont des compléments « à valider »** 🟨 : aucune n'a été relue par un enseignant.

## 1. Ce qui est disponible

| Élément | Contenu |
|---|---|
| **Cours « Surrénales »** | 6 leçons (environ 50 minutes de lecture) |
| **Questions d'archives** | **68**, dont **50 jouables** (indices, explication, remarque par proposition) et 18 seulement consultables |
| **Exercices vrai ou faux** | 12 (deux par leçon) |

| # | Leçon | Questions d'archives liées |
|---|---|---:|
| 1 | Physiologie et insuffisance surrénale (Addison, insuffisance centrale, crise, traitement, corticothérapie) | 15 |
| 2 | Syndrome de Cushing : démarche diagnostique et causes surrénaliennes | 11 |
| 3 | Hyperaldostéronisme primaire (syndrome de Conn) | 19 |
| 4 | Phéochromocytome et paragangliome | 12 |
| 5 | Incidentalome surrénalien et imagerie (scanner, densité, IRM) | 19 |
| 6 | Hyperandrogénie : hirsutisme, ovaires polykystiques, hyperplasie congénitale | 5 |

La leçon sur le Cushing complète celle du cours « Hypophyse » (signes, maladie de Cushing), sans la répéter. Les questions d'hirsutisme et d'ovaires polykystiques sont classées dans la partie « Surrénale » de la compilation (Maiter) : elles sont traitées ici.

## 2. Audit des questions

- **83 questions** classées « Surrénales » par l'extraction, relues une par une (`scripts/audit/surrenales.py`). Inventaire : `docs/audit/INVENTAIRE-SURRENALES.md`.
- **14 questions de pédiatrie** (Lysy, Beauloye : hyperplasie congénitale du nouveau-né, crise d'Addison chez l'enfant, doses de stress) sont **réservées au futur cours d'endocrinologie pédiatrique**, selon la règle de la phase 1 : seules les questions de pédiatrie sur la thyroïde vont dans un cours d'organe.
- **1 question** porte sur un adénome **hypophysaire** silencieux : rattachée au cours « Hypophyse ».

| Statut des 68 questions | Nombre |
|---|---:|
| 🟦 réponse proposée dans la compilation | 44 |
| 🟧 réponse discutée | 11 |
| ⬜ question incomplète (consultable) | 11 |
| 🟥 réponse absente (consultable) | 2 |

## 3. Corrections discutées

| Question | Problème |
|---|---|
| `2024-01-Q24` (Conn, test de posture) | « en cas d'adénome, l'aldostérone augmente de 33 % » contredit les autres sessions : c'est l'**hyperplasie** qui répond à la posture |
| `2023-05-Q42` (Conn, « la vraie ») | « traitée par spironolactone » est aussi exacte (deux « +1 ») |
| `2023-05-Q12b` (phéochromocytome) | « hypotension » retenue comme absente, alors que l'hypotension orthostatique est classique |
| `2023-05-Q28` (corticothérapie) | « Cushing iatrogène » est aussi exact |
| `2024-01-Q16` (nouveau-né, hémorragie surrénalienne) | ACTH retenue, mais le cortisol est tout aussi indispensable |
| `2025-01-Q50` (ACTH élevée) | 3 réponses pour 2 ; la tumeur carcinoïde bronchique donne bien une ACTH élevée : seulement consultable |
| `ND-maiter-surrenale-Q22` (bloc en 21-hydroxylase) | l'hirsutisme est marqué faux à tort : seulement consultable |
| `ND-maiter-surrenale-Q13` et `Q15` (insuffisance surrénale) | nombre de réponses marquées incohérent avec la consigne : seulement consultables |
| `ND-maiter-surrenale-Q1` et `Q14` (incidentalome) | deux réponses pour une consigne au singulier |

## 4. Corrections de l'outil d'import

- Les fichiers de questions existants ne sont **plus jamais remplacés** : l'import ajoute les nouvelles questions à la suite.
- Le rattachement de la réponse en rouge cherche d'abord une **proposition identique** : « dosage cortisol » n'est plus confondu avec « dosage cortisolurie ». Vérifié sans effet sur la thyroïde et l'hypophyse.
- **9 consignes** non reconnues automatiquement (« 2 réponses » au sens de « 2 fausses », « 1 mauvaise », « une chose à pas faire »…) et 2 découpages corrigés à la main, sans toucher au texte.

## 5. Références vérifiées (le 11/11/2026, niveau bibliographique)

| Thème | Référence |
|---|---|
| Insuffisance surrénale primaire | Bornstein SR et al. (Endocrine Society), J Clin Endocrinol Metab 2016;101:364-389 |
| Insuffisance surrénale due aux corticoïdes | Beuschlein F et al. (ESE et Endocrine Society), Eur J Endocrinol 2024;190:G25-G51 |
| Cushing | Nieman LK et al. (Endocrine Society), J Clin Endocrinol Metab 2008;93:1526-1540 |
| Incidentalome | Fassnacht M et al. (ESE et ENSAT), Eur J Endocrinol 2023;189:G1-G42 |
| Hyperaldostéronisme primaire | Adler GK et al. (Endocrine Society), J Clin Endocrinol Metab 2025;110:2453-2495 |
| Phéochromocytome | Lenders JWM et al. (Endocrine Society), J Clin Endocrinol Metab 2014;99:1915-1942 |
| Hirsutisme | Martin KA et al. (Endocrine Society), J Clin Endocrinol Metab 2018;103:1233-1257 |
| Ovaires polykystiques | Teede HJ et al. (recommandation internationale 2023), J Clin Endocrinol Metab 2023;108:2447-2469 |
| Hyperplasie congénitale | Speiser PW et al. (Endocrine Society), J Clin Endocrinol Metab 2018;103:4043-4088 |

**Valeurs signalées « à valider »** : dose quotidienne d'hydrocortisone (environ 15 à 25 mg), proportions hyperplasie bilatérale et adénome dans l'hyperaldostéronisme (environ deux tiers et un tiers), seuil de taille d'environ 4 cm pour suspecter un carcinome.

## 6. Pour refaire ou corriger

1. `scripts/audit/surrenales.py`, puis `python3 scripts/audit/domain_audit.py W surrenales`.
2. `python3 scripts/content/import_audit.py surrenales`.
3. `scripts/content/explications/surrenales.py`, puis `python3 scripts/content/add_explanations.py`.
4. Exercices vrai ou faux : `scripts/content/build_questions.py`.
