# ENDOCRINO ACADEMY — Intégration de la pharmacologie générale

> Date : 11 novembre 2026
> Quatrième domaine intégré, selon la même méthode. **Toutes les explications sont des compléments « à valider »** 🟨.

## 1. Ce qui est disponible

| Élément | Contenu |
|---|---|
| **Cours « Pharmacologie générale »** | 4 leçons (environ 24 minutes de lecture) |
| **Questions d'archives** | **24**, dont **23 jouables** et 1 seulement consultable |
| **Exercices vrai ou faux** | 8 (deux par leçon) |

| # | Leçon | Questions d'archives liées |
|---|---|---:|
| 1 | Pharmacocinétique et interactions (biodisponibilité, premier passage, cytochromes) | 3 directes, plus 7 sur les immunosuppresseurs |
| 2 | Fer, vitamine B12 et folates | 7 |
| 3 | Immunosuppresseurs : ciclosporine, sirolimus, azathioprine | 12 |
| 4 | Hypolipémiants : statines et ézétimibe | 2 |

**Périmètre.** Ce cours couvre la pharmacologie **hors endocrinologie** du cours de Horsmans. Les questions de pharmacologie sur les **médicaments hormonaux** restent dans le cours de l'organe : hormones thyroïdiennes et antithyroïdiens (thyroïde), agonistes dopaminergiques et somatostatine (hypophyse), corticoïdes (surrénales). Celles du diabète (23), du calcium (9) et des hormones sexuelles (8) suivront avec leurs cours. La leçon 1 l'explique.

## 2. Audit des questions

- **24 questions** classées « Pharmacologie générale » par l'extraction, relues une par une (`scripts/audit/pharmaco.py`). Inventaire : `docs/audit/INVENTAIRE-PHARMACO.md`.
- Les entrées « non classables » de l'inventaire sont presque toutes des questions **non retranscrites**, dont seul le prénom du transcripteur figure : elles ne sont pas importées, ces prénoms ne doivent pas apparaître dans l'application. Une seule était exploitable (IRM d'un adénome hypophysaire) : rattachée au cours « Hypophyse ».

| Statut des 24 questions | Nombre |
|---|---:|
| 🟦 réponse proposée dans la compilation | 15 |
| 🟧 réponse discutée | 8 |
| ⬜ question incomplète (consultable) | 1 |

## 3. Corrections discutées (vérifiées dans les notices et les recommandations)

| Question | Problème |
|---|---|
| Ciclosporine et ézétimibe (4 sessions) | réponse retenue : l'ézétimibe « n'interagit pas ». La notice de l'ézétimibe signale pourtant une interaction : l'exposition des deux médicaments augmente, et les taux de ciclosporine sont à surveiller |
| Sirolimus, « la fausse » (2 questions) | « absorption lente » est faux, mais « élimination rénale » aussi (2,2 % dans les urines) |
| Ciclosporine, « la fausse » | « premier passage important » est retenu comme faux, alors qu'il est notable ; l'élimination rénale est faible (3 à 6 %) |
| Vitamine B12, dose quotidienne | 1 µg retenu ; les apports recommandés actuels sont de 4 µg par jour (EFSA 2015) |

Le besoin en fer de 1,5 mg par jour (archives) correspond bien à la quantité **absorbée** nécessaire chez la femme réglée.

## 4. Références vérifiées (le 11/11/2026)

- Notices (FDA) : sirolimus (Rapamune) ; ézétimibe (Zetia, 2023) ; ciclosporine (élimination biliaire).
- EFSA 2015 : valeurs de référence pour la vitamine B12 (article 4150) et le fer (article 4254).
- Revue sur l'inhibition du CYP2C8 par les métabolites glucuronides du gemfibrozil et du clopidogrel (PubMed Central, PMC9496539).
