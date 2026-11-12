# ENDOCRINO ACADEMY — Intégration du domaine « Diabète » (lot 1 sur 2)

> Date : 12 novembre 2026
> Sixième domaine intégré, selon la même méthode. **Toutes les explications sont des compléments « à valider »** 🟨.
> Le diabète est le chapitre le plus long des archives : il est intégré **en deux lots**, comme demandé.

## 1. Découpage en deux lots

| Lot | Contenu | Questions d'archives | État |
|---|---|---:|---|
| **1** | diagnostic, types de diabète, autres types (MODY, gestationnel, secondaires), complications aiguës, complications chroniques, pied diabétique | **160** | **intégré** |
| **2** | médicaments (antidiabétiques oraux, GLP-1), insuline, nutrition du diabétique, hypoglycémies (dont insulinome) | 92 | à venir |

Le découpage est défini dans `scripts/audit/diabete.py` (variable `PARTS`) ; le lot 2 s'ajoutera aux mêmes fichiers sans changer les identifiants du lot 1.

## 2. Ce qui est disponible (lot 1)

| Élément | Contenu |
|---|---|
| **Cours « Diabète et hypoglycémies »** | 6 leçons (environ 65 minutes de lecture) |
| **Questions d'archives** | **160**, dont **126 jouables** et 34 seulement consultables |
| **Exercices vrai ou faux** | 14 |

| # | Leçon | Questions d'archives liées |
|---|---|---:|
| 1 | Diagnostic : glycémies, HbA1c, HGPO, peptide C | 31 |
| 2 | Type 1, type 2 et LADA | 35 |
| 3 | MODY, diabète gestationnel, diabètes secondaires, insulinorésistance | 23 |
| 4 | Complications aiguës : acidocétose, coma hyperosmolaire, coma | 31 |
| 5 | Complications chroniques : rétine, rein, nerfs, cœur, diarrhée | 30 |
| 6 | Le pied diabétique : PEDIS, pied de Charcot | 13 |

## 3. Audit des questions

- **292 questions** classées « diabète » par l'extraction (Maiter, Marbaix, sessions 2022 à 2026), relues une par une. **252 retenues** pour le domaine. Inventaire : `docs/audit/INVENTAIRE-DIABETE.md`.
- **Écartées du domaine** (aucune n'est supprimée) :
  - **30 questions de pédiatrie** : réservées au cours de pédiatrie (décision du 11 novembre 2026) ;
  - **5 questions sur le diabète insipide ou un adénome** : rattachées au cours « Hypophyse » (4 sont jouables et ont reçu une explication) ;
  - **5 questions sur les NEM et le gastrinome** : réservées au futur cours sur les néoplasies endocriniennes multiples.

| Statut des 160 questions du lot 1 | Nombre |
|---|---:|
| 🟦 réponse proposée dans la compilation | 113 |
| 🟧 réponse discutée | 20 |
| ⬜ question incomplète (consultable) | 20 |
| 🟥 réponse absente (consultable) | 7 |

**Corrections de consigne** : deux questions dont la consigne est « que faire ? » ou « lequel exclure en premier ? » étaient lues comme « la fausse » ; elles sont corrigées en « une seule réponse » (`2023-05-Q23`, `ND-maiter-diabete-Q127`). Une question à 2 propositions sans réponse (`2026-01-p4-l131`, coma acidocétosique) est classée « incomplète ».

## 4. Écarts entre les archives et les recommandations actuelles

| Thème | Archives | Recommandations |
|---|---|---|
| Bicarbonates dans l'acidocétose | « pas d'office », « pas jusqu'à correction du pH » | consensus 2024 : seulement si le pH est inférieur à 7,0 (concordant) |
| Objectif tensionnel du diabétique avec néphropathie | faux : « inférieur à 150/80 » | ADA 2025 : inférieur à 130/80 (concordant) |
| Dépistage du diabète gestationnel en début de grossesse | « pour toutes » retenu | ADA : chez les femmes à risque (à toutes, possible) ; question marquée « discutée » |
| Tabac et rétinopathie | « facteur aggravant bien connu » | lien jugé incertain par l'ADA ; 2 questions marquées « discutées » |

## 5. Autres corrections discutées (requalifiées « discutées », réponse conservée)

- **Constipation et neuropathie autonome** (`2022-05-Q7`) : la constipation est en réalité fréquente dans la neuropathie autonome.
- **Syndrome de Garland** (`ND-maiter-diabete-Q85`) : présenté comme une neuropathie autonome, alors que c'est une amyotrophie proximale.
- **Fibrates et diarrhée** (`ND-maiter-diabete-Q53`) : les notices citent la diarrhée parmi les effets fréquents.
- **Syndrome de Cushing et diarrhée** (`ND-maiter-diabete-Q11`) : lien peu clair, deux intrus possibles.
- **GH et insulinorésistance sévère** (`2022-05-Q22`) : la pseudo-acromégalie se fait avec une GH normale.
- **Classification PEDIS** (`ND-maiter-diabete-Q87`) : trois réponses marquées pour « deux fausses » ; l'une d'elles est exacte (consultable seulement).
- **Néphropathie et amaigrissement du type 1** (`ND-maiter-diabete-Q37`), **insuffisance rénale « plus de 10 ans après »** (`ND-maiter-diabete-Q9`) : signalées dans les leçons.

## 6. Références vérifiées (le 12/11/2026, niveau bibliographique)

- American Diabetes Association Professional Practice Committee. *Standards of Care in Diabetes—2025.* Diabetes Care 2025;48(Suppl 1) : sections 2 (diagnostic et classification, S27-S49), 10 (risque cardiovasculaire), 11 (maladie rénale chronique), 12 (rétinopathie, neuropathie et pied).
- Umpierrez GE et al. *Hyperglycemic Crises in Adults With Diabetes: A Consensus Report.* Diabetes Care 2024;47:1257-1275.
- IADPSG. *Recommendations on the diagnosis and classification of hyperglycemia in pregnancy.* Diabetes Care 2010;33:676-682.
- Schaper NC et al. *Practical guidelines on the prevention and management of diabetes-related foot disease (IWGDF 2023 update).* Diabetes Metab Res Rev 2024;40:e3657.
- Lipsky BA et al. *Guidelines on the diagnosis and treatment of foot infection in persons with diabetes (IWGDF 2019 update).* Diabetes Metab Res Rev 2020;36(S1):e3280.

## 7. Limites

- Les explications sont des compléments rédigés à partir des recommandations citées : elles restent **« à valider »** face au cours de l'UCL.
- Les seuils en mg/dL suivent les archives ; certaines unités (mmol/L) ne sont pas converties partout.
- Le lot 2 (traitements et hypoglycémies) n'est pas encore intégré : les questions sur les médicaments, l'insuline et les hypoglycémies arriveront avec lui.
