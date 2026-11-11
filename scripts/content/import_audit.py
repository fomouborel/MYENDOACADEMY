"""Phase 5 — importe dans content/questions/ toutes les questions de thyroïde de l'audit qui ne sont pas
déjà saisies à la main (scripts/content/build_questions.py). Préserve l'énoncé, les propositions, la
provenance, les commentaires d'étudiants et le statut de fiabilité vérifié en phase 1.
Les questions importées n'ont pas encore d'indices ni d'explication rédigée : la correction affiche la
réponse proposée, son statut et le lien vers la leçon.
Usage : python3 scripts/content/import_audit.py [domaine]   (thyroide par défaut ; ex. hypophyse)
Les données viennent de scripts/audit/data/<domaine>-audit.json. Hors thyroïde, les fichiers produits
s'appellent import-<domaine>-<session>.json."""
import json, os, re, glob, sys, unicodedata, collections

HERE = os.path.dirname(__file__)
ROOT = os.path.join(HERE, "..", "..")
DOM = sys.argv[1] if len(sys.argv) > 1 else "thyroide"
AUDIT = json.load(open(os.path.join(ROOT, f"scripts/audit/data/{DOM}-audit.json"), encoding="utf-8"))
OUTDIR = os.path.join(ROOT, "content/questions")
SRC = {"A": "#Compilation endocrino 2016-2024.pdf", "E": "02_Retranscription Janvier 2025 - Secteur Endocrinologie.pdf", "G": "Retranscription – Janvier 2026 _ Secteur Endocrinologie (1).pdf"}
STATUS = {"Réponse proposée dans la compilation": "proposed", "Réponse discutée ou contestée": "disputed", "Question incomplète": "incomplete",
          "Réponse absente": "absent", "Réponse déduite du texte, à vérifier": "deduced"}
DEFAULT_NOTE = {"incomplete": "Retranscription incomplète (propositions ou énoncé manquants) : question consultable, non notée.",
                "absent": "Aucune réponse n'est indiquée dans la compilation.",
                "disputed": "Réponse discutée dans la compilation (voir les commentaires).",
                "deduced": "Réponse indiquée dans un commentaire, à vérifier."}

# Questions déjà saisies à la main (avec indices et explications) : on ne les réimporte pas.
existing = {}
for f in glob.glob(os.path.join(OUTDIR, "*.json")):
    for q in json.load(open(f, encoding="utf-8"))["questions"]:
        if q["kind"] == "archive":
            existing[q["provenance"]["auditRef"]] = q["id"]

OPT = re.compile(r"^\s*(?:[A-Ja-j]\s*[.)\];:]|[-•●]|\d\s*[.)]|[A-J](?=\s))\s*")
COMMENT = re.compile(r"^\s*(->|=>|⇒|\(|\[|\+1)")
norm = lambda s: re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFD", s.lower()).encode("ascii", "ignore").decode())

def instruction_of(stem, n_expected):
    s = stem.lower()
    if re.search(r"2 fausses|deux fausses|2 faux|sauf 2|sauf deux|\b2f\b|deux propositions fausses|2 réponses fausses", s): return "two-false"
    if re.search(r"2 vraies|deux vraies|2 réponses justes|2 justes|\(2\)|2 réponses\)|\(2v\)|\(2 réponses|deux réponses justes", s): return "two-correct"
    if re.search(r"fausse|faux|sauf|\bne\b.*\bpas\b|n.est pas|n.apparait|ne pas|pas utile|impossible|\b1f\b|\bla f\b|exclure|ne fait pas", s): return "one-false"
    if re.search(r"vraie|\bvrai\b|juste|correcte|exacte", s): return "one-true"
    return "two-correct" if n_expected == 2 else "one-correct"

def split_stem(lines):
    """Les lignes situées avant la première proposition balisée prolongent l'énoncé (retour à la ligne du PDF)."""
    for i, l in enumerate(lines):
        if OPT.match(l.strip()) or re.match(r"^\s*(=>|⇒)", l):
            return lines[:i], lines[i:]
    return [], lines

def parse_options(lines):
    opts, comments, arrows = [], [], []
    new_item = False  # une puce seule sur sa ligne annonce une nouvelle proposition
    prev_len = 999
    for raw in lines:
        t = raw.strip()
        if not t: continue
        cur_len, prev_len = len(t), prev_len
        if re.match(r"^(=>|⇒)\s*\S", t): arrows.append(re.sub(r"^(=>|⇒)\s*", "", t)); continue
        if COMMENT.match(t):
            if len(t) > 1: comments.append(t)  # une parenthèse orpheline n'est pas un commentaire
            continue
        # Une ligne qui suit une ligne courte (non coupée par le retour à la ligne du PDF) est une nouvelle
        # proposition, même si sa lettre a été perdue à l'extraction.
        if OPT.match(t) or not opts or new_item or prev_len < 70:
            text = OPT.sub("", t, count=1).strip()
            if text:
                opts.append(text); new_item = False
            else:
                new_item = True
            prev_len = cur_len if text else 999
            continue
        else:
            opts[-1] = (opts[-1] + " " + t).strip()  # continuation d'une proposition sur plusieurs lignes
        prev_len = cur_len
    if not opts and arrows:  # propositions notées « => … » par le transcripteur
        opts = arrows
    else:
        comments += ["=> " + a for a in arrows]
    clean = []
    for o in opts:
        votes = len(re.findall(r"\+1", o))
        o2 = re.sub(r"\s*\+1(\s*\+1)*", "", o).strip()
        if votes: comments.append(f"« +1 » ×{votes} sur la proposition : {o2[:60]}")
        clean.append(o2)
    return clean[:10], comments

def expected_of(opts, marked):
    """Rattache chaque fragment marqué en rouge à une proposition. On cherche d'abord une proposition
    identique, puis une correspondance complète (le fragment contient la proposition ou l'inverse), puis
    seulement les 25 premiers caractères : deux propositions qui commencent pareil, ou dont l'une contient
    l'autre (« dosage cortisol » et « dosage cortisolurie »), ne doivent pas être confondues."""
    exp = []
    nos = [norm(o) for o in opts]
    for m in marked:
        mt = norm(OPT.sub("", m.strip(), count=1))
        if len(mt) < 3: continue
        hit = [i for i, no in enumerate(nos) if no == mt]
        if not hit: hit = [i for i, no in enumerate(nos) if no and (mt in no or (len(no) >= 8 and no in mt))]
        if not hit: hit = [i for i, no in enumerate(nos) if no and (mt[:25] in no or no[:25] in mt)]
        if hit and "ABCDEFGHIJ"[hit[0]] not in exp: exp.append("ABCDEFGHIJ"[hit[0]])
    return exp

# Numérotation stable des sections non datées (ND) : base + numéro dans la section.
ND_BASE = {"Maiter adulte – Thyroïde": 200, "Maiter adulte – Hypophyse": 300, "Lysy – Thyroïde": 160, "Marbaix – Anapath thyroïde/parathyroïdes/surrénales": 100,
           "Duprez + Coche – Imagerie": 0, "Horsmans – Pharmaco hormones": 0, "Marbaix – Anapath hypophyse": 120, "Maiter adulte – Surrénale": 400,
           "Horsmans – Pharmaco hématopoïèse": 10, "Horsmans – Pharmaco hypolipémiants": 20, "Horsmans – Pharmaco immunosuppresseurs": 30,
           "Hermans – Syndrome métabolique": 500, "Navez – Chirurgie bariatrique": 600, "Thissen – Obésité": 700}
used = collections.defaultdict(set)
for qid in existing.values():
    m = re.match(r"ENDO-(.+)-(ADULTE|PEDIA|RADIO|ANAPATH|PHARMA)-(QCM|QCMM|VF|QROC|CAS)-(\d{3})$", qid)
    if m: used[(m.group(1), m.group(2))].add(int(m.group(4)))

def number_for(q, beauloye_rank):
    sess = "ND" if q["session"] == "2016-2021" else q["session"]
    if sess == "ND":
        if q["section"].startswith("Beauloye"): n = 200 + beauloye_rank
        else: n = ND_BASE[q["section"]] + (q["num"] or 0)
    else:
        n = q["num"] if q["num"] else 900
    while n in used[(sess, q["disc"])]: n += 1
    used[(sess, q["disc"])].add(n)
    return sess, n

# Corrections ciblées après relecture (débordement de la question suivante, blocs non jouables).
TRUNCATE = {"2025-01-p16-l482": "Question sur les critères", "2026-01-Q18": "Q28."}
FORCE = {"ND-maiter-thyroide-Q1": ("incomplete", "Bloc d'association de 3 cas cliniques (énoncé du cas 1 non retranscrit) : consultable, non noté sous forme de QCM.")}
EXTRA_COMMENT = {"ND-marbaix-thyroide-parathyroides-Q2": "La proposition E est vraisemblablement une plaisanterie du transcripteur (proposition originale inconnue).",
                 "2025-01-Q50": "Mention du transcripteur : « Réponses à confirmer » (+1 ×2).",
                 "2023-05-Q100": "Commentaire du transcripteur sur l'examen : « Horsman 100 % tuyaux sauf les 2 dernières questions qui sont nouvelles »."}
# Découpage énoncé / propositions refait à la main quand l'extraction les a mélangés (texte original inchangé).
RESPLIT = {"2024-01-Q39": ("observables en cas de macropolactinome nô secretant chez femme, la fausse :",
                           ["Alopecie temporale", "Galactorhée", "Aménorrhée secondaire", "céphalées"]),
           "2025-01-Q35": ("Monsieur, connu pour macroadénome, arrive aux urgences pour céphalées, vomissements, raideur de nuque mais pas de fièvre, diagnostic :",
                           ["Méningite bactérienne", "Apoplexie hypophysaire", "Syndrôme de Sheehan", "Lymphome hypophysaire", "Métastases carcinome hypophysaire"]),
           # lettre de proposition perdue à l'extraction : deux propositions fusionnées
           "ND-maiter-hypophyse-Q2": ("Toutes les propositions sont correctes sauf 1 :",
                           ["Si hyperprolactinémie est supérieure à 50 (nl : 20), c’est toujours lié à un prolactinome",
                            "Apoplexie hypophysaire est une complication possible d’un macroadénome",
                            "Il ne faut pas se fier à des taux de TSH pour le ttmnt d’une hypothyroïdie centrale",
                            "Le traitement à la fluorohydrocortisone n’est pas indiqué dans l’insuffisance ACTH"]),
           "ND-maiter-hypophyse-Q10": ("Concernant le prolactinome, toutes sont vraies sauf une :",
                           ["Il entraîne un hypogonadisme hypergonadotrope aussi bien chez les hommes que chez les femmes",
                            "Le taux de prolactine est corrélé à la taille de la tumeur hypophysaire",
                            "Il entraîne une gynécomastie chez les hommes et une galactorrhée chez la femme",
                            "Il est traité par agoniste dopaminergique",
                            "Il n’entraîne pas de symptômes chez une femme ménopausée"]),
           "ND-marbaix-hypophyse-Q1": ("Adénome hypophysaire",
                           ["Cellules avec gros noyaux",
                            "Peut causer une amputation du champ visuel sans causer de troubles hormonaux (??)",
                            "Contient des fibres réticulaires"]),
           # lettres collées au texte (« A-IRM hypophyse ») : lettres retirées, texte inchangé
           "2025-01-Q43": ("Parmi ces propositions laquelle ne permet pas de déterminer l’étiologie du syndrome de Cushing :",
                           ["IRM hypophyse", "La concentartion plamsatique d’ACTH", "Le test de stimulation de CRH", "CTscan des surrénales", "Le test dexamethasone faible dose"]),
           # Pharmacologie : numéro collé à l'énoncé ; commentaires sur l'examen lus comme des propositions
           "2024-01-p10-l353": ("Le folate est absorbée au niveau :", ["Jéjunum", "Estomac", "Iléon", "colon", "Gastrique"]),
           "2023-05-Q100": ("biodisponibilité IV :", ["25%", "50%", "75%", "100%", "10 %"]),
           # Obésité : question suivante collée aux propositions
           "ND-thissen-obesite-Q2": ("Ces médicaments ont un effet neutre ou favorable sur l’excès de poids. Quelle est la fausse ?",
                           ["Inhibiteur DPP4", "Inhibiteur Sglt2 (glifozines)", "Sulfamidés", "Famille metformine", "analogues GLP1 (incrétinomimétiques)"]),
           "2025-01-p16-l489": ("pour excès de poids (1 faux) :",
                           ["BMI > 40", "BMI entre 27 et 29.9 avec complications cardiovasculaires", "BMI >30 sans complications cardio",
                            "BMI entre 25 et 26,9 avec complications cardiovasculaires", "BMI >35 avec complications cardiovasculaires"]),
           # la mention « Réponses à confirmer +1+1 » du transcripteur avait été lue comme une 6e proposition
           "2025-01-Q50": ("Hypercortisolémie avec ACTH élévé lesquelles des ses situations ne sont possibles (2 réponses) :",
                           ["macroadenome hypophysaire", "microadénome hypophysaire", "tumeur carcinoïde bronchique",
                            "traitement de gouttes nasales avec corticoides", "incidentalome surrénalien avec sécrétion autonome de cortisol"])}
# Consigne déduite d'une autre occurrence de la même question (énoncé abrégé dans la retranscription).
INSTR = {"ND-maiter-hypophyse-Q8": "one-false",
         # formulations de consigne non reconnues automatiquement
         "ND-maiter-hypophyse-Q14": "one-false",      # « n'apparaît pas »
         "ND-maiter-hypophyse-Q15": "two-correct",    # « (Deux justes) »
         "ND-maiter-hypophyse-Q24": "two-false",      # « 2 F »
         "2025-01-Q37": "two-false",                  # « 2 propositions fausses »
         "ND-duprez-coche-imagerie-Q9": "one-correct", # « n'est pas graisseuse » décrit la masse, pas la consigne
         # Surrénales
         "2023-05-Q50": "two-false",                  # « quels traitements sont faux » (deux marqués, comme Maiter Q21)
         "ND-maiter-surrenale-Q13": "two-false",      # « ne retrouve-t-on pas (2 réponses) »
         "ND-maiter-surrenale-Q14": "two-false",      # deux réponses marquées, toutes deux défendables
         "ND-maiter-surrenale-Q15": "two-false",      # « NE SONT PAS spécifiques (2 réponses) »
         "2023-05-Q12b": "two-false",                 # « quels 2 symptômes ne sont pas obtenus »
         "2025-01-Q50": "two-false",                  # « ne sont possibles (2 réponses) »
         "ND-maiter-surrenale-Q23": "one-false",      # « (1 mauvaise) »
         "ND-marbaix-thyroide-parathyroides-Q10": "one-correct",  # la bonne réponse est « aucune »
         "2023-05-Q35": "one-false", "2022-05-Q42": "one-false",  # « une chose à pas faire »
         "2023-05-Q42": "one-true",
         # Obésité
         "ND-thissen-obesite-Q6": "two-false",         # deux réponses exactes marquées (« laquelle ne donne pas »)
         "ND-hermans-syndrome-metabolique-Q119": "two-false",
         "ND-thissen-obesite-Q11": "two-false"}       # « Deux affirmations fausses »                   # « parmi ces propositions fausses, laquelle est la vraie »

files = collections.defaultdict(list)
report = collections.Counter()
problems = []
beauloye_lines = sorted(q["line"] for q in AUDIT if q["section"].startswith("Beauloye"))
for q in AUDIT:
    if q["placeholder"] or q["ref"] in existing:
        report["déjà saisie" if q["ref"] in existing else "non retranscrite"] += 1
        continue
    stem = re.sub(r"^\s*\d{1,3}\s*[.\-)]\s*", "", " ".join(q["stem"])).strip()
    stem = re.sub(r"^Q POSSIBLEMENT ANNULEE\s*\d*\.?\s*", "", stem)
    extra, rest = split_stem(q["lines"])
    if extra: stem = (stem + " " + " ".join(x.strip() for x in extra)).strip()
    opts, comments = parse_options(rest)
    if q["ref"] in RESPLIT: stem, opts = RESPLIT[q["ref"]][0], list(RESPLIT[q["ref"]][1])
    if q["ref"] in TRUNCATE:
        opts = [o for o in opts if not o.startswith(TRUNCATE[q["ref"]])]
    opts = [re.sub(r"\s+[a-e]$", "", o) for o in opts]  # lettre orpheline en fin de ligne
    if q["ref"] in EXTRA_COMMENT: comments.append(EXTRA_COMMENT[q["ref"]])
    exp = expected_of(opts, q["marked"])
    status = STATUS[q["status"]]
    if q["ref"] in FORCE: status = FORCE[q["ref"]][0]
    instr = INSTR.get(q["ref"]) or instruction_of(stem, len(exp))
    note = (FORCE[q["ref"]][1] if q["ref"] in FORCE else q["note"]) or None
    if status in ("proposed", "disputed", "deduced") and not exp:
        problems.append((q["ref"], "réponse marquée introuvable dans les propositions", q["marked"]))
        status, note = "incomplete", (note or "") + " Réponse marquée non rattachable à une proposition retranscrite."
    if status in ("proposed", "disputed", "deduced") and len(opts) < 3:
        status = "incomplete"
    if status == "absent": exp = []
    want = {"one-false": 1, "one-true": 1, "one-correct": 1, "two-false": 2, "two-correct": 2}[instr]
    if status in ("proposed", "deduced") and exp and len(exp) != want:
        status = "disputed"
        note = ((note or "") + f" La consigne retranscrite demande {want} réponse(s), mais {len(exp)} proposition(s) sont marquées dans la compilation.").strip()
    if "ANNULEE" in " ".join(q["stem"]).upper(): comments.append("Question signalée « possiblement annulée » par les étudiants.")
    if status in DEFAULT_NOTE and not note: note = DEFAULT_NOTE[status]
    sess, n = number_for(q, beauloye_lines.index(q["line"]) if q["section"].startswith("Beauloye") else 0)
    typ = "QCMM" if (instr in ("two-false", "two-correct") or len(exp) > 1) else "QCM"
    teacher = q["teacher"] if q["teacher"] not in ("non attribué (adulte)", "non précisé") else None
    fname = q["session"] if sess != "ND" else "nd-" + q["section"].split()[0].lower().replace("+", "")
    if DOM != "thyroide": fname = f"{DOM}-{fname}"
    item = {
        "id": f"ENDO-{sess}-{q['disc']}-{typ}-{n:03d}", "kind": "archive", "format": "mcq", "instruction": instr,
        "stem": stem, "labs": [], "options": [{"id": "ABCDEFGHIJ"[i], "text": o} for i, o in enumerate(opts)],
        "expected": exp, "answerStatus": status, "sourceComments": comments,
        "provenance": {"session": sess, "discipline": q["disc"], "teacher": teacher, "formerTeacher": q["section"].startswith("Beauloye"),
                       "sourceFile": SRC[q["src"]], "page": q["page"], "originalNumber": q["num"], "auditRef": q["ref"]},
        "chapter": q["map"]["chapter"], "subchapter": q["map"]["subchapter"], "lessonLinks": q["map"]["lessons"][:3],
        "tags": [], "difficulty": 3 if q["clinical"] else 2, "clinical": bool(q["clinical"]), "duplicateGroup": q["groupe"],
    }
    if note: item["answerNote"] = note.strip()
    files[f"import-{fname}"].append(item)
    report[status] += 1

for name, qs in files.items():
    path = os.path.join(OUTDIR, f"{name}.json")
    # On ajoute aux questions déjà présentes : un fichier existant n'est jamais remplacé.
    before = json.load(open(path, encoding="utf-8"))["questions"] if os.path.exists(path) else []
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"source": name, "questions": before + qs}, f, ensure_ascii=False, indent=2)
print(dict(report), sum(len(v) for v in files.values()), "questions importées dans", len(files), "fichiers")
for p in problems: print("À VÉRIFIER", p)
