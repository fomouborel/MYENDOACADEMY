# ENDOCRINO ACADEMY — Intégration du domaine « Obésité et nutrition »

> Date : 11 novembre 2026
> Cinquième domaine intégré, selon la même méthode. **Toutes les explications sont des compléments « à valider »** 🟨.

## 1. Ce qui est disponible

| Élément | Contenu |
|---|---|
| **Cours « Obésité et nutrition »** | 4 leçons (environ 27 minutes de lecture) |
| **Questions d'archives** | **28**, dont **25 jouables** et 3 seulement consultables |
| **Exercices vrai ou faux** | 8 (deux par leçon) |

| # | Leçon | Questions d'archives liées |
|---|---|---:|
| 1 | Obésité : définitions, causes et dépense énergétique | 9 |
| 2 | Variations de poids d'origine endocrinienne | 4 |
| 3 | Traitement : nutrition, médicaments, chirurgie bariatrique | 13 |
| 4 | Syndrome métabolique | 6 |

## 2. Audit des questions

- **33 questions** classées « Obésité, nutrition & syndrome métabolique » par l'extraction (Thissen, Hermans, Navez, sessions 2022 à 2025), relues une par une (`scripts/audit/obesite.py`). Inventaire : `docs/audit/INVENTAIRE-OBESITE.md`.
- **5 questions de pédiatrie** (Lysy : prise de poids chez l'enfant, IMC en déviations standard) sont **réservées au cours de pédiatrie** (décision du 11 novembre 2026).

| Statut des 28 questions | Nombre |
|---|---:|
| 🟦 réponse proposée dans la compilation | 21 |
| 🟧 réponse discutée | 5 |
| ⬜ question incomplète (consultable) | 2 |

## 3. Écarts entre les archives et les recommandations actuelles

| Thème | Archives | Recommandations |
|---|---|---|
| Tour de taille de la femme (obésité androïde) | plus de 88 cm (définition américaine NCEP-ATP III) | 80 cm selon les recommandations européennes (2015) ; la définition harmonisée (2009) laisse le choix des seuils à chaque pays |
| Indications de la chirurgie bariatrique | IMC de 40 ou plus, ou de 35 ou plus avec complications (critères de 1991) | depuis 2022 (ASMBS et IFSO) : IMC de 35 ou plus même sans complication ; à envisager entre 30 et 34,9 avec maladie métabolique |

La réponse des archives sur le tour de taille est conservée (elle correspond à la définition qu'elle cite) ; la leçon et l'explication présentent les deux seuils. La question sur la chirurgie est marquée « discutée ».

## 4. Autres corrections discutées

- **Traitement d'un syndrome métabolique complet avec diabète** (Hermans Q119) : la metformine est retenue comme « à ne pas débuter d'emblée », alors que c'est le traitement de première intention habituel du diabète de type 2.
- **Coronariens et syndrome métabolique** (Hermans Q69) : proposition retenue ambiguë (« épreuve de cycloergomètre asymptomatique »).
- **« Laquelle ne fait pas maigrir »** (Thissen Q6) : deux réponses exactes marquées (insulinome et Cushing) pour une consigne au singulier.
- **Calcul de charge glycémique** (Thissen Q10) : vérifié, le résultat juste est 85 g, ce qui confirme que la proposition « 95 g » est fausse.

## 5. Références vérifiées (le 11/11/2026, niveau bibliographique)

- Yumuk V et al. *European Guidelines for Obesity Management in Adults.* Obes Facts 2015;8:402-424.
- Alberti KGMM et al. *Harmonizing the metabolic syndrome: a joint interim statement.* Circulation 2009;120:1640-1645.
- Eisenberg D et al. *2022 ASMBS and IFSO: Indications for Metabolic and Bariatric Surgery.* Surg Obes Relat Dis 2022;18:1345-1356.
