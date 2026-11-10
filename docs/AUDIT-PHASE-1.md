# ENDOCRINO ACADEMY — Rapport d'audit documentaire (phase 1)

> Date : 10 novembre 2026 · Branche : `claude/nice-mendel-6foiq0`
> Méthode de référence : `METHODE-ARBORESCENCE` (Digest Academy), transposée à l'endocrinologie.
> Fichiers associés :
> - `docs/audit/INVENTAIRE-THYROIDE.md`, l'inventaire thyroïde lisible (134 entrées, classées par module et par famille de questions) ;
> - `docs/audit/inventaire-thyroide.csv`, le même inventaire sous forme de tableur, avec les énoncés et les propositions en entier ;
> - `docs/audit/inventaire-complet.csv`, l'inventaire des 844 entrées, tous domaines confondus ;
> - `scripts/audit/`, les scripts d'extraction (pour pouvoir refaire l'audit).
>
> **Aucune ligne de l'application n'a encore été écrite.** Ce rapport attend votre validation.

---

## 1. Résumé

| Indicateur | Valeur |
|---|---:|
| PDF fournis / PDF au contenu distinct | 7 / **3** |
| Entrées repérées (questions et emplacements de question) | **844** |
| — questions exploitables (énoncé au moins partiel) | **814** |
| — numéros sans contenu (seul le nom de l'étudiant·e qui devait la retranscrire figure) | 30 |
| Sessions d'examen identifiées | 5 sessions datées (mai 2022 → janvier 2026) + 1 compilation non datée 2016-2021 |
| Questions avec une réponse repérable (rouge ou indiquée dans le texte) | 709 (87 %) |
| **Corrections officielles identifiées** | **0** |
| Questions incomplètes | 142 |
| Réponses discutées ou à vérifier | 52 (plus 88 questions incomplètes qui portent malgré tout une réponse) |
| Questions quasi identiques posées plusieurs fois (repérage automatique) | 128 questions réparties en 52 groupes |
| **Questions centrées sur la thyroïde** | **134** (133 exploitables + 1 non retranscrite) |
| Questions d'autres chapitres où la thyroïde intervient | 50 |
| Thyroïde : réponse proposée et question complète / à vérifier / sans réponse ou incomplète | 71 / 18 / 45 |

**Points d'attention principaux**

1. Le document « 2016-2024 » n'est pas le seul. L'archive contient aussi **janvier 2025** et **janvier 2026**, que j'ai inventoriés.
2. **Aucune correction n'est officielle.** Toutes les réponses sont des propositions d'étudiant·e·s (texte en rouge), parfois accompagnées de « +1 », « pas sûr », « je pense ».
3. Le fichier « Copie… **version réponse** » est **identique** à la compilation 2016-2024 (même texte, mêmes réponses en rouge). Il n'apporte aucune réponse supplémentaire.
4. La compilation 2016-2025 contient une **seconde couche de réponses** (surlignage jaune) pour 2022-2024. Elle est partielle et **contredit la couche rouge sur 2 questions de thyroïde** (§ 7).
5. La partie « 2016-2021 » est classée **par enseignant, sans l'année** : on ne peut pas dater ces 443 questions année par année.
6. **Pédiatrie** : 26 questions de thyroïde sont pédiatriques, dont 17 d'un **ancien titulaire (Beauloye)**. Une décision d'arborescence est nécessaire (§ 9.2).
7. Les sources ne contiennent **aucun support de cours**. Toutes les explications des futures leçons seront donc des compléments à valider (§ 8).

---

## 2. Environnement de travail

| Élément | Constat |
|---|---|
| Dépôt | `fomouborel/myendoacademy`, un seul commit (« Add files via upload ») |
| Contenu initial | un seul fichier : `Source Endocrino Academie.zip` (17,6 Mo) |
| Branche de travail | `claude/nice-mendel-6foiq0` (créée, synchronisée avec `origin`) |
| Outils disponibles | Python 3.13, poppler (`pdftotext`, `pdfimages`), PyMuPDF (installé pour lire les couleurs), Chromium et Playwright (pour les tests à venir) |
| Code applicatif | aucun |

---

## 3. Les sources

### 3.1 Contenu de l'archive

| # | Fichier | Pages | Nature | Apport réel |
|---|---|---:|---|---|
| A | `#Compilation endocrino 2016-2024.pdf` | 91 | Word. Réponses en **rouge** | **Source principale** : janvier 2024, mai 2023, mai 2022 et compilation 2016-2021 par enseignant |
| D | `Copie-de-Compilation-endocrino-2016-2024-version-réponse.pdf` | 91 | Impression iOS de A | **Doublon de A** : texte identique, mêmes réponses (vérifié ligne par ligne) |
| B | `Compilation endocrino 2016-2025.pdf` | 105 | Word | Janvier 2025 suivi de A. Sur 2022-2024, les réponses sont **surlignées en jaune**, et non en rouge. Sur 2016-2021, **aucune réponse** |
| C | `Compilation-endocrino-2016-2021-2.pdf` | 59 | Impression iOS | Partie 2016-2021 **sans réponses**. Aucune question absente de A |
| E | `02_Retranscription Janvier 2025 – Secteur Endocrinologie.pdf` | 19 | Word. Réponses en rouge | **Source de janvier 2025** |
| F | `endocrino-2025.pdf` | 14 | Impression iOS de E | Version de E sans réponses. Aucune question en plus |
| G | `Retranscription – Janvier 2026 _ Secteur Endocrinologie (1).pdf` | 12 | Google Docs. Réponses en rouge | **Source de janvier 2026** |

**Conclusion** : le corpus distinct tient dans **A + E + G**. B sert de **seconde lecture des réponses** pour 2022-2024.

### 3.2 Comment les réponses sont codées

- Les consignes des retranscriptions disent : « mettez juste la réponse **en rouge** (pas de +1+1+1 svp), les débats c'est en commentaires ».
- L'extraction lit donc la **couleur de chaque mot** (1 077 fragments rouges dans A).
- On trouve aussi des commentaires dans le texte (« +1 », « pas sûr », « je pense que c'était… », « => »), des notes en vert (titres) et quelques commentaires en d'autres couleurs.
- Le fichier B ajoute 213 fragments surlignés (2022-2024). J'ai comparé les deux couches :
  - **12** fragments surlignés ne correspondent à aucun fragment rouge ;
  - **46** réponses rouges ne sont pas surlignées.
  - La couche surlignée est surtout **incomplète**. Elle diverge réellement sur quelques questions, dont 2 de thyroïde (§ 7).

### 3.3 Images

Quatre images en tout : un tableau de glycémies (A p.31), un tableau taille/poids pour les courbes d'« Apolline » (A p.78), un tableau de glycémies (E p.3) et deux icônes. **Aucune ne concerne la thyroïde.**

La retranscription de janvier 2026 précise d'ailleurs : « pas d'image à l'examen » pour l'imagerie et l'anapath.

---

## 4. Méthode d'extraction

1. **Extraction du texte avec les couleurs** (PyMuPDF) : chaque mot rouge, surligné ou coloré est repéré.
2. **Découpage en questions**, de façon semi-automatique :
   - repérage par la numérotation, avec une tolérance pour les numérotations non continues de la partie 2016-2021 ;
   - repérage des énoncés non numérotés (« la fausse », « sauf », « ? ») ;
   - pour les blocs non numérotés (pédiatrie Beauloye, pédiatrie de mai 2022, fin de janvier 2024), les débuts de question ont été fixés **à la main**.
3. **Rattachement** :
   - session, section ou enseignant ;
   - discipline : adulte, pédiatrie, radiologie, anapath ou pharmacologie ;
   - page du PDF, type de question, cas clinique ou non, statut de correction.
4. **Domaine endocrinien** :
   - pour 2016-2021, d'après la section de l'enseignant ;
   - ailleurs, d'après des mots-clés.
5. **Thyroïde : revue manuelle de chaque question** (134 entrées) : module principal, autres modules, sous-thème, statut vérifié, remarques et famille de doublons.

**Fiabilité des chiffres** :
- Les chiffres **thyroïde** sont **exacts** (revue manuelle).
- Les chiffres **globaux** par domaine, type et statut viennent d'un **classement automatique vérifié par sondage**. Une marge de quelques questions est possible ; ils servent à préparer les extensions futures.
- La **discipline des sessions 2024 et 2025** est **déduite** de la numérotation, sur le modèle de la structure annoncée en mai 2023 (55 adultes, 20 pédiatrie, 10 radiologie et anapath, 15 pharmacologie). Elle est signalée comme « déduite » dans le tableur.

---

## 5. Sessions identifiées et composition

| Session | Source | Durée | Composition **annoncée dans la source** | Questions exploitables | Numéros non retranscrits |
|---|---|---|---|---:|---:|
| **Janvier 2026** | G | 2 h | 80 QCM : adulte 44 (Alexopoulou, Loumaye (1), Preumont) ; Lysy 16 ; radiologie 4 ; anapath 4 ; Horsmans 12. « 1 ou 2 bonnes réponses, nombre indiqué » | 65 | 2 (+ ~16 numéros absents) |
| **Janvier 2025** | E (F) | 3 h | non précisée (numérotation 1-100) | 75 | **21** |
| **Janvier 2024** | A p.1-13 | — | non précisée (numérotation 1-100) | 84 | 3 (+ numéros vides) |
| **Mai 2023** | A p.13-27 | — | 100 QCM : 55 adulte (Preumont¹, Alexopoulou, Loumaye, Orioli, Thissen, Navez) ; 20 pédiatrie (Lysy) ; 5 anapath (Marbaix) ; 5 radiologie (Coche, Duprez) ; 15 pharmacologie (Horsmans). « QCM à 1 ou 2 bonnes réponses » | 87 | 4 |
| **Mai 2022** | A p.27-37 | — | « Adulte (55 Q) », puis pédiatrie, radiologie, anapath (« même que les anciennes années », non retranscrite) et pharmacologie | 60 | — |
| **2016-2021** (non daté) | A p.37-91 | — | classement **par enseignant**, sans année ni session | 443 | — |
| **Total** | | | | **814** | **30** |

¹ Écrit « Pneumont » dans la source.

**Conséquences pour les examens blancs** :
- La composition réelle n'est **connue que pour mai 2023 et janvier 2026**.
- Aucune session n'est retranscrite en entier.
- On ne pourra donc **jamais présenter un examen comme « complet »**. L'application devra afficher « composition annoncée : … ; questions disponibles : … ».

---

## 6. Inventaire global (tous domaines)

### 6.1 Par année ou session

| Session | 2026-01 | 2025-01 | 2024-01 | 2023-05 | 2022-05 | 2016-2021 | **Total** |
|---|---:|---:|---:|---:|---:|---:|---:|
| Questions | 65 | 75 | 84 | 87 | 60 | 443 | **814** |

### 6.2 Par discipline (axe B de la méthode)

| Session | Adulte | Pédiatrie | Radiologie | Anapath | Pharmacologie |
|---|---:|---:|---:|---:|---:|
| 2026-01 | 38 | 10 | 3 | 2 | 12 |
| 2025-01* | 42 | 16 | 6 | 4 | 7 |
| 2024-01* | 50 | 18 | 4 | 1 | 11 |
| 2023-05 | 49 | 17 | 4 | 4 | 13 |
| 2022-05 | 32 | 20 | 2 | — | 6 |
| 2016-2021 | 248 | 97 | 37 | 31 | 30 |
| **Total** | **459** | **178** | **56** | **42** | **79** |

\* Discipline déduite de la numérotation.

### 6.3 Par enseignant

| Enseignant | Questions | Remarque |
|---|---:|---|
| Maiter (adulte) | 229 | 2016-2021 uniquement (diabète, thyroïde, hypophyse, surrénales, gonades) |
| Lysy (pédiatrie) | 96 | toutes les sessions |
| Beauloye (pédiatrie) | 82 | **« Ancien prof »** dans la source (ancien titulaire) |
| Horsmans (pharmacologie) | 79 | « 100 % tuyaux » selon les étudiant·e·s |
| Duprez / Coche (radiologie) | 41 | |
| Marbaix (anapath) | 40 | |
| Alexopoulou (adulte) | 22 | nommée en 2026, notamment pour la **thyroïde** |
| Preumont (adulte, diabète) | 15 | nommé en 2026 |
| Thissen (obésité) | 10 | |
| Hermans (syndrome métabolique) | 6 | |
| Navez (chirurgie bariatrique) | 3 | |
| Loumaye | 1 | |
| **Adulte, enseignant non attribué** (2022-2025) | 173 | les retranscriptions ne disent pas qui a posé chaque question adulte |
| Non précisé (radiologie/anapath 2024-2026) | 17 | |

### 6.4 Par domaine endocrinien (axe A)

| Domaine | Questions | dont 2016-2021 |
|---|---:|---:|
| Diabète et hypoglycémies (y compris pharmacologie et anapath du diabète) | 292 | 159 |
| **Thyroïde** | **133** (+1 non retranscrite) | 78 |
| Croissance et puberté (pédiatrie) | 100 | 51 |
| Hypophyse (y compris prolactine, acromégalie, diabète insipide) | 90 | 58 |
| Surrénales (Cushing, Addison, Conn, phéochromocytome, incidentalome, HCS) | 83 | 46 |
| Gonades et hormones sexuelles | 34 | 16 |
| Obésité, nutrition, syndrome métabolique | 33 | 19 |
| Pharmacologie générale (fer, B12, immunosuppresseurs, statines) | 24 | 8 |
| Phosphocalcique et parathyroïdes | 16 | 5 |
| Tumeurs neuro-endocrines et NEM | 6 | — |
| Non classable | 3 | 3 |

### 6.5 Formats

| Format | Questions |
|---|---:|
| QCM « une fausse » ou « sauf une » | 400 |
| QCM à une réponse | 297 |
| QCM « deux fausses » ou deux réponses à exclure | 50 |
| QCM « une vraie » | 44 |
| QCM à deux bonnes réponses | 22 |
| Association | 1 |
| **QROC** | **0** |
| **Cas cliniques** (vignette patient, repérage automatique) | **≈ 185** |

**QROC** : les examens sont exclusivement des QCM (« Modalités : QCM » en 2026). Certaines questions retranscrites sans propositions ressemblent à des questions ouvertes. Ce sont en réalité des **QCM incomplets** : je ne les transformerai pas en QROC sans votre accord.

### 6.6 Statut de correction (les 844 entrées)

| Statut | Entrées |
|---|---:|
| Correction officielle identifiée | **0** |
| Réponse proposée dans la compilation (en rouge, sans doute exprimé) | 566 |
| Réponse discutée ou contestée (« pas sûr », « je pense », « ?? », choix multiples, désaccord) | 51 |
| Réponse déduite d'un commentaire dans le texte, à vérifier | 1 |
| Réponse absente | 54 |
| Question incomplète (propositions manquantes ou énoncé résumé), **dont 88 qui portent une réponse** | 142 |
| Question non retranscrite (seul le nom de l'étudiant·e figure) | 30 |

### 6.7 Doublons

- **52 groupes** de questions quasi identiques, soit 128 questions. Repérage automatique, seuil de similarité de 80 % : 36 paires, 8 triplets, 8 quadruplets. La colonne `doublon_auto` du tableur indique le groupe.
- En plus, la **thyroïde** est regroupée **à la main** en **31 familles** de questions récurrentes (122 questions). On y trouve des reformulations et des variantes à réponse différente, que le repérage automatique ne voit pas.
- **Aucune occurrence n'est supprimée.** Les étudiant·e·s signalent elles-mêmes les reprises (« copié collé des années passées », « tuyau », « même que l'année passée »).

---

## 7. Inventaire thyroïde

Le détail question par question est dans `docs/audit/INVENTAIRE-THYROIDE.md`. Voici la synthèse.

### 7.1 Chiffres clés

| | Pathologies thyroïdiennes | Hyperthyroïdie | Hypothyroïdie | **Total** |
|---|---:|---:|---:|---:|
| Module **principal** | 69 | 20 | 45 | **134** |
| Questions **utiles** au module (principal ou secondaire) | 76 | 41 | 63 | — |
| Réponse proposée, question complète | 44 | 11 | 16 | **71** |
| Réponse discutée ou contestée | 5 | 3 | 10 | **18** |
| Question incomplète | 20 | 6 | 9 | **35** |
| Réponse absente | 0 | 0 | 9 | **9** |
| Non retranscrite | 0 | 0 | 1 | **1** |

- **40 questions** se rattachent à plusieurs modules. Exemples : De Quervain (pathologies + hyperthyroïdie), interprétation d'une TSH basse (les 3 modules), amiodarone (hyper + hypo), Hashimoto en anapath (pathologies + hypo), effets indésirables de la L-thyroxine (hypo + hyper).
- En plus, **50 questions transversales** citent la thyroïde dans une autre spécialité : gynécomastie et hyperthyroïdie, NEM 2 et carcinome médullaire, hyperprolactinémie et hypothyroïdie, adénome hypophysaire et T4 basse, poids et thyroïde… Elles resteront dans leur chapitre d'organe, avec une étiquette `thyroïde` (règle § 6 de la méthode).

### 7.2 Répartition par session, discipline et enseignant

| Session | Questions thyroïde | Pathologies | Hyper | Hypo |
|---|---:|---:|---:|---:|
| 2026-01 | 10 | 4 | 2 | 4 |
| 2025-01 | 12 (dont 1 non retranscrite) | 7 | 2 | 3 |
| 2024-01 | 12 | 7 | 1 | 4 |
| 2023-05 | 14 | 8 | 1 | 5 |
| 2022-05 | 8 | 4 | 1 | 3 |
| 2016-2021 | 78 | 39 | 13 | 26 |

- **Par discipline** : adulte 74 · pédiatrie 26 · radiologie 15 · anapath 13 · pharmacologie 6.
- **Par enseignant** :
  - Maiter 38 · adulte non attribué (2022-2025) 29 · **Beauloye (ancien titulaire) 17** · Marbaix 13 · Duprez/Coche 10 · Lysy 9 · Alexopoulou 7 · Horsmans 6 · non précisé 5.
- **Cas cliniques** : 30 · **association** : 1 (3 cas d'hyperthyroïdie à associer à une étiologie).

### 7.3 Ce que les archives interrogent (familles récurrentes)

| Module | Famille | Questions | Sessions où elle apparaît |
|---|---|---:|---|
| Pathologies | Nodule : échographie et indications de cytoponction | 11 | 2016-21 ×6, 2022, 2023, 2024, 2025 ×2 |
| Pathologies | Nodule : arguments de malignité (« sauf… ») | 8 | 2016-21 ×4, 2023, 2024 ×2, 2025 |
| Pathologies | Thyroïdite de De Quervain | 8 | **toutes les sessions** |
| Pathologies | Interprétation d'une TSH basse | 6 | **toutes les sessions** sauf 2026 |
| Pathologies | Cancers (papillaire, folliculaire, médullaire, Hürthle, anaplasique) | 6 + 5 en anapath | 2016-21, 2024, 2026 |
| Pathologies | Hashimoto en anapath | 6 | 2016-21 ×5, 2023 |
| Pathologies | Goitre : étiologies et évolution | 5 | 2016-21 ×3, 2022, 2026 |
| Pathologies | Iode et effet Wolff-Chaikoff, maladie non thyroïdienne, scintigraphie, EU-TIRADS | 8 | |
| Hyper | Basedow : traitement (ATS, PTU et grossesse, rechutes, tabac) | 5 (+1 clinique, +1 orbitopathie, +1 échographie) | 2016-21, 2023, 2025, 2026 |
| Hyper | Hyperthyroïdie factice et thyroglobuline, anticorps | 4 | 2016-21 ×3, 2022 |
| Hyper | Amiodarone (types 1 et 2) | 2 | 2016-21, 2026 |
| Hyper | Étiologies, goitre multinodulaire toxique, adénome thyréotrope, ATS en pharmacologie | 6 | |
| Hypo | Effet indésirable de la L-thyroxine (pharmacologie) | 5 | 2016-21, 2023, 2024 ×2, 2026 |
| Hypo | Surdosage en L-thyroxine chez la personne âgée (palpitations) | 3 | 2016-21, 2024, 2025 |
| Hypo | Hypothyroïdie centrale : surveillance par la **T4 libre**, pas la TSH | 3 (+ options dans 3 questions d'hypophyse) | 2016-21, 2023, 2026 |
| Hypo | Hypothyroïdie de l'adulte (cause, traitement, grossesse) | 4 (+1 biologie, +1 carence iodée) | |
| Hypo (pédiatrie) | Hypothyroïdie congénitale : dépistage, étiologie selon la Tg, dose, signes | 15 | 2016-21 surtout, 2022, 2023, 2025, 2026 |
| Hypo (pédiatrie) | Thyroïde de l'enfant, infraclinique, courbe de croissance | 11 | |

Ces familles serviront de base aux **sous-chapitres** et à l'encadré « Ce que les archives interrogent » de chaque leçon.

### 7.4 Questions de thyroïde dont la correction pose problème

| Réf. audit | Problème |
|---|---|
| `2022-05-Q37` Hypothyroïdie de l'adulte | **Désaccord entre compilations** : rouge (2016-2024) = « TSH à 12 → augmenter de 25 » (« pas sûre ») ; surligné (2016-2025) = « augmentation des besoins à la fin du 1er trimestre » |
| « Thyroïde de l'enfant, la vraie » (`2023-05-Q61`, `2022-05` pédiatrie, `2016-2021` Lysy Q1) | **Même question, réponses différentes** : B en rouge en 2023, C en rouge en 2022 et 2016-2021, B surligné en 2022 |
| `2022-05-Q34` Goitre « sauf un » | La réponse rouge « Hyperthyroïdie » est médicalement discutable. Les questions apparentées donnent « prise d'hormones thyroïdiennes ». Retranscription probablement inexacte |
| `2016-2021-Q13` TSH « sauf un » | Deux propositions en rouge pour une seule réponse attendue ; une proposition manque |
| `2016-2021-Q23` Syndrome de basse T3 | La proposition marquée « fausse » paraît exacte sur le fond. Marquage à vérifier |
| `2016-2021-Q26` Adénome thyréotrope | Énoncé incohérent (hyperthyroïdie clinique avec T3 et T4 « normales ») : retranscription douteuse |
| `2025-01-Q32` L-thyroxine chez une patiente de 83 ans | « soit D, soit A » |
| `2023-05-Q38` TSH abaissée | « +1 » sur deux propositions différentes |
| `2016-2021` Beauloye Q19/Q20 (athyréose, dyshormonogenèse) | « Question **possiblement annulée** » ; piège d'unités (mU/L ou µU/mL) |
| `2016-2021-Q2` Carence iodée | Doute sur la formulation d'une proposition (hyper- ou hypothyroxinémie) |
| `2016-2021` anapath Q12 (Hashimoto) | Commentaire « FAUX les follicules non ? » sur la réponse rouge |
| Courbes de croissance Beauloye (C, cas 5) | Réponse débattue : thyroïdite ou déficit en GH, thyroïde ectopique ou thyroïdite |

Ces questions garderont leur statut « discutée » et leurs commentaires. **Elles ne seront jamais présentées comme corrigées officiellement.**

---

## 8. Limites documentaires (à connaître dès maintenant)

1. **Pas de support de cours.** Les sources sont des souvenirs d'examen. Toute explication pédagogique sera donc un **complément rédigé, affiché « à valider »**, jamais attribué à l'UCL.
   → Si vous disposez des diapositives ou des syllabus du cours de thyroïde, les fournir améliorera nettement la fidélité des leçons.
2. **Retranscriptions de mémoire** : propositions manquantes (« je sais plus »), valeurs biologiques oubliées (« j'ai plus les chiffres »), formulations approchées (« un truc comme ça »).
3. **Valeurs de référence** : elles ne sont données que dans quelques énoncés (par exemple TSH 0,30-3,5 mU/L ; T4L 12-22 pmol/L ; T3L 2,0-6,0 pmol/L). Je n'en ajouterai aucune autre sans source vérifiée.
4. **Années 2016-2021 indiscernables** : l'axe « année » de ces 443 questions sera « 2016-2021 (compilation par enseignant) ».
5. **Enseignant non attribué** pour les questions adultes de 2022 à 2025. Seul 2026 indique qu'Alexopoulou couvre la thyroïde. Je n'attribuerai pas un enseignant par déduction.
6. **Sessions incomplètes** : il manque notamment 21 questions en janvier 2025 et environ 16 en janvier 2026.
7. **Noms d'étudiant·e·s** : la source contient les prénoms ou noms des étudiant·e·s qui devaient retranscrire certaines questions. Je les ai **masqués** dans les inventaires. Ils ne seront pas repris dans l'application.

---

## 9. Proposition d'arborescence pour la V1 thyroïde (à valider)

Elle applique la méthode : sous-chapitres construits à partir des familles réelles, avec au moins 5 questions chacun si possible.

### 9.1 Chapitres et sous-chapitres

| Chapitre | Sous-chapitre (`id`) | Questions principales |
|---|---|---:|
| **1. Pathologies thyroïdiennes** (`thyroide`) | `explo` Physiologie, iode et exploration (TSH, T4L, T3L, scintigraphie, maladie non thyroïdienne) | ≈ 12 |
| | `nodules` Nodules : facteurs de malignité, échographie (EU-TIRADS), cytoponction | ≈ 23 |
| | `cancers` Cancers thyroïdiens (clinique et anatomie pathologique) | ≈ 11 |
| | `thyroidites` Thyroïdites (De Quervain, silencieuse, Hashimoto, échographie, anatomie pathologique) | ≈ 18 |
| | `goitre` Goitres | ≈ 5 |
| **2. Hyperthyroïdie** (`hyper`) | `diagnostic` Diagnostic étiologique (Tg, anticorps, scintigraphie, factice, GMN, adénome toxique, origine centrale) | ≈ 9 (+ thyroïdites en secondaire) |
| | `basedow` Basedow (clinique, ATS, grossesse, rechutes, orbitopathie) | ≈ 9 |
| | `iatrogene` Amiodarone, iode et traitements | ≈ 2 (+ questions secondaires) |
| **3. Hypothyroïdie** (`hypo`) | `diagnostic` Primaire ou centrale, biologie, causes | ≈ 7 |
| | `traitement` L-thyroxine : dose, sujet âgé, grossesse, effets indésirables, surveillance (T4L dans l'hypothyroïdie centrale) | ≈ 11 |
| | `congenitale` Hypothyroïdie congénitale et de l'enfant | ≈ 26 (voir 9.2) |

L'hyperthyroïdie compte peu de questions « principales » (20). Elle bénéficiera des 21 questions secondaires (De Quervain, thyroïdite silencieuse, TSH basse…) grâce au rattachement multi-modules (`lessonLinks`).

### 9.2 Décisions à prendre

1. **Questions pédiatriques de thyroïde (26).** La méthode Digest range toutes les questions d'enfant **dans un chapitre `pediatrie` séparé**. L'appliquer strictement retirerait de la V1 l'hypothyroïdie congénitale, que vous demandez pourtant dans le cours Hypothyroïdie.
   → **Ma recommandation** : en V1, sous-chapitre `congenitale` dans Hypothyroïdie, avec le badge « 👶 Pédiatrie » et le filtre Adulte/Pédiatrie. Le futur chapitre `pediatrie` réutilisera ces questions par lien, sans les dupliquer.
2. **Questions de l'ancien titulaire (Beauloye, 17 questions de thyroïde).**
   → **Recommandation** : les garder, avec `formerTeacher = true` et la mention « ancien titulaire » visible.
3. **Questions incomplètes (35) et sans réponse (9).**
   → **Recommandation** :
   - les conserver dans la banque des anciens examens, en consultation, avec le statut affiché ;
   - les exclure de l'entraînement noté et des examens blancs tant qu'elles ne sont pas complétées ;
   - ne jamais inventer les propositions manquantes.
4. **Questions de sessions postérieures à 2024.** Les sources 2025 et 2026 sont dans l'archive.
   → **Recommandation** : les intégrer, puisque l'objectif est la couverture des anciens examens.
5. **Identifiants.** Votre exemple est `ENDO-2024-THYROIDE-QCM-001`, la méthode utilise `<APP>-<SESSION>-<DISCIPLINE>-<TYPE>-<NNN>`.
   → **Recommandation** :
   - suivre la méthode : `ENDO-2024-01-ADULTE-QCM-001`, `ENDO-ND-PEDIA-QCM-014` ;
   - « ND » désigne la compilation 2016-2021 non datée ;
   - le chapitre reste un champ séparé.

---

## 10. Suite proposée (après votre validation)

- **Phase 2, architecture** : modèle de données (repris de Digest), sauvegarde IndexedDB, export et import JSON, workflow GitHub Actions et GitHub Pages.
- **Phase 2, confidentialité** : étude chiffrée de Cloudflare Access (avantages, limites de l'offre gratuite, conséquences). Rien ne sera mis en place sans votre accord.
- **Phase 3** : rédaction des 3 cours à partir des familles ci-dessus, avec l'encadré « Ce que les archives interrogent ».
