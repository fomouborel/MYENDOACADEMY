# ENDOCRINO ACADEMY — Conception pédagogique de la thyroïde (phase 3)

> Date : 11 novembre 2026 · Prérequis : `AUDIT-PHASE-1.md`, `ARCHITECTURE-PHASE-2.md`
> Livrables :
> - **13 leçons** dans `content/lessons/{thyroide,hyper,hypo}/` ;
> - leur déclaration dans `content/chapters.json` ;
> - le rattachement des 134 questions de thyroïde aux leçons : `docs/audit/rattachement-thyroide-lecons.csv`.
>
> **Statut** : contenus rédigés et vérifiés automatiquement (structure, liens, syntaxe). **Ils ne sont pas encore visibles dans l'application** : les chapitres restent « en intégration » jusqu'à la phase 4, qui construit l'écran de lecture. **Toutes les explications sont des compléments « à valider »** (🟨) : aucune n'a encore été relue par un enseignant.

---

## 1. Plan des trois cours

### Cours 1 — Pathologies thyroïdiennes (`thyroide`)

| # | Leçon | Sous-chapitre | Lecture | Questions d'archives liées |
|---|---|---|---:|---:|
| 1 | Physiologie et exploration de la thyroïde (anatomie, synthèse, iode, Wolff-Chaikoff, axe, TSH/T4L/T3L, TSH basse, anticorps, Tg, calcitonine, scintigraphie, maladie non thyroïdienne) | `explo` | 13 min | 12 |
| 2 | Nodules : facteurs de malignité, EU-TIRADS, cytoponction, Bethesda | `nodules` | 10 min | 23 |
| 3 | Cancers : papillaire, folliculaire, oncocytaire, anaplasique, médullaire, NEM | `cancers` | 9 min | 11 |
| 4 | Thyroïdites : De Quervain, silencieuse, post-partum, Hashimoto (clinique, échographie, anatomie pathologique) | `thyroidites` | 9 min | 18 |
| 5 | Goitres, carence iodée, thyroïde et grossesse (vue d'ensemble) | `goitre` | 9 min | 6 |

### Cours 2 — Hyperthyroïdie (`hyper`)

| # | Leçon | Sous-chapitre | Lecture | Questions liées |
|---|---|---|---:|---:|
| 1 | Reconnaître, confirmer, trouver la cause. **Grand tableau comparatif des étiologies** (clinique, TSH, anticorps, Tg, scintigraphie, échographie) et arbre décisionnel | `diagnostic` | 10 min | 23 |
| 2 | Maladie de Basedow : physiopathologie, orbitopathie, ATS (thiamazole ou PTU), iode radioactif, chirurgie, grossesse | `basedow` | 11 min | 10 |
| 3 | Nodules toxiques, amiodarone (types 1 et 2), prise exogène, adénome thyréotrope, complications | `diagnostic`, `iatrogene` | 10 min | 9 |
| 4 | Traiter selon la cause (tableau), surveillance, rechutes, grossesse, sujet âgé, crise aiguë thyrotoxique | `basedow`, `iatrogene` | 8 min | 6 |

### Cours 3 — Hypothyroïdie (`hypo`)

| # | Leçon | Sous-chapitre | Lecture | Questions liées |
|---|---|---|---:|---:|
| 1 | Primaire ou centrale (**tableau comparatif**), patente ou infraclinique, causes, clinique, biologie, démarche | `diagnostic` | 10 min | 16 |
| 2 | L-thyroxine : modalités de prise, interactions, doses, sujet âgé, adaptation (TSH ou T4L), surdosage | `traitement` | 9 min | 12 |
| 3 | Grossesse (augmentation précoce des doses), coma myxœdémateux, complications | `traitement`, `diagnostic` | 9 min | 5 |
| 4 | 👶 Hypothyroïdie congénitale (Guthrie, causes selon la Tg, conduite en urgence), thyroïde de l'enfant | `congenitale` | 11 min | 26 |

Les durées sont estimées à environ 140 mots par minute, un rythme de lecture attentive. Les liens entre les cours sont explicites, par exemple « voir la leçon Basedow » ou « voir le cours 1 ».

---

## 2. Structure de chaque leçon

Chaque leçon suit le gabarit de la méthode (§ 5.2), adapté aux unités demandées dans le prompt (§ 6).

| Bloc | Contenu | Provenance affichée |
|---|---|---|
| `:::archives` | **Ce que les archives interrogent** : nombre de questions, notions réellement posées, réponses proposées, pièges récurrents, corrections discutées signalées | 🟦 « Archives UCL — compilation d'étudiants » |
| `:::complement` | 1. L'essentiel (explication simple) · 2. Physiopathologie · 3. Clinique · 4. Biologie et examens · 5. Tableau comparatif ou arbre décisionnel · 6. Traitement · 7. Exemple clinique · **8. À retenir** · Pièges classiques · **Attention : corrections discutées** · 3 questions de compréhension · Références vérifiées | 🟨 « Explication complémentaire — à valider » |

**Supports visuels** : 35 tableaux comparatifs et 5 arbres décisionnels ou schémas (axe hypothalamo-hypophyso-thyroïdien, évolution des thyroïdites…), en texte lisible sur téléphone. Il y a aussi des moyens mnémotechniques, comme « 3 P » pour la NEM 1 et « deux médullaires » pour la NEM 2. Les illustrations anatomiques dessinées sont prévues avec l'interface (phase 4).

---

## 3. Rattachement des questions d'archives

- **Les 134 questions de thyroïde** de l'inventaire sont rattachées à un chapitre, un sous-chapitre et 1 à 3 leçons (`lessonLinks`). Le détail est dans `docs/audit/rattachement-thyroide-lecons.csv`.
- Le rattachement suit les **familles** de l'audit. Par exemple :
  - « TSH basse sauf… » → Physiologie et exploration, et Hyper – diagnostic ;
  - « De Quervain » → Thyroïdites, et Hyper – diagnostic ;
  - « Patiente âgée sous L-thyroxine » → L-thyroxine.
- Chaque encadré « Ce que les archives interrogent » a été **écrit à partir de ces questions** : les nombres affichés correspondent au rattachement.
- Les **26 questions pédiatriques** sont rattachées à `hypo › congenitale`, conformément à la décision de la phase 1. Le validateur l'impose.

Les questions elles-mêmes, avec énoncé original, propositions, statut, indices et explications, seront saisies en phase 5. Les leçons sont prêtes à les recevoir.

---

## 4. Sources utilisées et niveau de fiabilité

| Source | Utilisation | Comment c'est signalé |
|---|---|---|
| **Compilation des examens** (2016-2026) | contenu des encadrés « archives » : notions interrogées, réponses proposées, commentaires | bloc 🟦, jamais présenté comme une correction officielle |
| **Explications rédigées** | tout le reste des leçons | bloc 🟨 « à valider » |
| **Recommandations internationales** | citées en fin de leçon et dans le texte pour les points chiffrés | liste « Références vérifiées », avec la date |

**Références citées**. Leur existence et leurs coordonnées ont été vérifiées le 10 et le 11/11/2026, au **niveau bibliographique** : titre, revue, année, pages, DOI, et résumés ou synthèses pour les points cités.

| Thème | Référence |
|---|---|
| Nodules (EU-TIRADS) | Russ G et al., Eur Thyroid J 2017;6:225-237 |
| Nodules et cancers différenciés | Haugen BR et al. (ATA 2015), Thyroid 2016;26:1-133 |
| Classification des tumeurs | Baloch ZW et al. (OMS 2022), Endocr Pathol 2022;33:27-63 |
| Hyperthyroïdie | Ross DS et al. (ATA 2016), Thyroid 2016;26:1343-1421 |
| Basedow | Kahaly GJ et al. (ETA 2018), Eur Thyroid J 2018;7:167-186 |
| Orbitopathie | Bartalena L et al. (EUGOGO 2021), Eur J Endocrinol 2021;185:G43-G67 |
| Amiodarone | Bartalena L et al. (ETA 2018), Eur Thyroid J 2018;7:55-66 |
| Hypothyroïdie | Jonklaas J et al. (ATA 2014), Thyroid 2014;24:1670-1751 |
| Hypothyroïdie centrale | Persani L et al. (ETA 2018), Eur Thyroid J 2018;7:225-237 |
| Grossesse | Alexander EK et al. (ATA 2017), Thyroid 2017;27:315-389 |
| Hypothyroïdie congénitale | van Trotsenburg P et al. (ENDO-ERN 2021), Thyroid 2021;31:387-419 |

**Valeurs signalées « à valider » dans le texte**, faute d'avoir pu les vérifier dans le texte intégral :

| Valeur | Leçon |
|---|---|
| dose complète de L-thyroxine d'environ 1,6 µg/kg/j | L-thyroxine |
| paliers de 12,5 à 25 µg, contrôle à environ 6 semaines | L-thyroxine |
| cible de T4L dans la moitié supérieure de la normale (hypothyroïdie centrale) | L-thyroxine, Hypo – diagnostic |
| dose initiale de 10 à 15 µg/kg/j dans l'hypothyroïdie congénitale | Congénitale |
| tableau des catégories Bethesda (conduites indicatives) | Nodules |
| seuil d'environ 1 cm pour ponctionner un nodule fixant au PET-scan | Nodules |

Les seuils de ponction EU-TIRADS (20, 15 et 10 mm) ont été confirmés par des sources secondaires concordantes (Radiopaedia, revues indexées dans PMC).

**Valeurs de référence biologiques** : aucune norme « officielle » n'a été ajoutée. Les leçons renvoient aux normes **données dans les énoncés** d'examen et rappellent que les normes dépendent du laboratoire.

---

## 5. Corrections discutées : comment elles sont traitées

Chaque leçon concernée contient un encadré **« Attention : correction discutée dans les archives »**. Il présente les deux versions, ce que disent les recommandations, et rappelle qu'aucune correction officielle n'existe.

| Question | Leçon |
|---|---|
| TSH « sauf un » (deux réponses rouges), `2023-05-Q38`, syndrome de basse T3 | Physiologie et exploration |
| Basedow en anatomie pathologique (« infiltration lymphocytaire »), Hashimoto Q12 | Thyroïdites |
| Goitre « sauf un » (`2022-05-Q34`), carence iodée (hypo- ou hyperthyroxinémie) | Goitres |
| Adénome thyréotrope (énoncé incohérent) | Hyper – autres causes |
| Hypothyroïdie de l'adulte (`2022-05-Q37`) : désaccord entre compilations | Hypo – grossesse |
| « Thyroïde de l'enfant, la vraie » (B ou C selon l'année), questions « possiblement annulées » | Congénitale |

---

## 6. Contrôles effectués

- **`npm run validate:content`** :
  - 13 leçons présentes, chacune avec ses encadrés « archives » et « À retenir » ;
  - sous-chapitres existants ;
  - **nouvelle règle** : pas de deux-points collé à un mot, qui ferait disparaître du texte à l'affichage. Elle a révélé 23 lignes de références à corriger, qui l'ont été.
- **Analyse Markdown** : chaque leçon contient exactement un bloc `archives` et un bloc `complement`, et tous les tableaux sont reconnus.
- **Tests** : 31 tests unitaires au vert, dont le test « le contenu réel du dépôt est valide », qui inclut désormais les 13 leçons.

---

## 7. Ce qui vous est demandé

1. **Relecture médicale** si possible (vous-même, l'étudiante ou un enseignant). Une leçon relue passe de 🟨 « à valider » à 🟩 « validée » : il suffit de me l'indiquer.
2. **Supports officiels** : si les diapositives ou le syllabus de thyroïde de l'UCL sont disponibles, les fournir me permettrait d'aligner les leçons sur le cours. Les ajouts seraient alors marqués « support de cours ».
3. **Validation du plan** (13 leçons) avant la phase 4.

## 8. Suite : phase 4 (prototype fonctionnel)

- « Mes cours » : les 3 cours, leur sommaire et l'écran de lecture des leçons, avec les blocs colorés selon la provenance.
- Premiers exercices (QCM, vrai ou faux) avec correction, 3 indices et lien « Revoir la leçon ».
- Suivi de progression branché sur les services de la phase 2.
- Premières questions d'archives saisies pour pouvoir tester le parcours complet d'une étudiante.
