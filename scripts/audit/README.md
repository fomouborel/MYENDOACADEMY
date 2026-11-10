# Scripts d'audit (phase 1)

Ces scripts ont produit `docs/AUDIT-PHASE-1.md` et `docs/audit/*`. Ils servent à refaire ou corriger l'audit. Ils ne font pas partie de l'application.

Prérequis : Python 3.11 ou plus, `pip install pymupdf`.

## Étapes

Tous les fichiers de travail vont dans un dossier `W`, pris hors du dépôt.

1. Décompresser `Source Endocrino Academie.zip`, puis copier les PDF dans `W/pdf/` sous ces noms :
   - `A_comp2016-2024.pdf`
   - `E_retr2025-01.pdf`
   - `G_retr2026-01.pdf`
2. `extract.py` : extraction du texte page par page, avec la couleur de chaque mot.
   - `⟦R:…⟧` marque le texte rouge, `⟦H:…⟧` le texte surligné.
   - Commande, pour chaque PDF : `python extract.py W/pdf/X.pdf W/col/X.txt`
3. `compact.py` : compactage de `W/col/X.txt` en `W/cmp2/X.txt`. Les fragments marqués deviennent `«…»` et les lignes de puces vides sont supprimées.
   - Commande : `python compact.py W/col/X.txt W/cmp2/X.txt`
4. `segment.py W` : découpage en questions et rattachement à la session et à la section. Produit `W/inv_raw.json`.
   - Les débuts de question des blocs non numérotés sont fixés à la main (dictionnaire `MANUAL`).
5. `post.py W` : fusion des fragments, type de question, statut de correction et domaine provisoire. Produit `W/inv.json`.
6. `build.py W x` : discipline, enseignant et domaine définitifs, avec application des classements manuels de `thyroid.py`. Produit `W/final.json`.
   - `build.py` importe `post_dom.py` et `post_hack.py` : lancer avec `scripts/audit` dans le `PYTHONPATH`.
7. `stats.py W docs/audit` : statistiques et inventaires CSV.
8. `thymd.py W docs/audit` : génère `INVENTAIRE-THYROIDE.md`.

## Fichier clé : `thyroid.py`

Classement **manuel** de chaque question de thyroïde. Pour chacune :
- module principal et autres modules ;
- sous-thème ;
- statut vérifié ;
- remarques ;
- famille de doublons.

Pour corriger un rattachement, modifier ce fichier puis relancer les étapes 6 à 8.
