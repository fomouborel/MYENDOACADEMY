"""Phase 5 — importe dans content/questions/ toutes les questions de thyroïde de l'audit qui ne sont pas
déjà saisies à la main (scripts/content/build_questions.py). Préserve l'énoncé, les propositions, la
provenance, les commentaires d'étudiants et le statut de fiabilité vérifié en phase 1.
Les questions importées n'ont pas encore d'indices ni d'explication rédigée : la correction affiche la
réponse proposée, son statut et le lien vers la leçon.
Usage : python3 scripts/content/import_audit.py"""
import json, os, re, glob, unicodedata, collections

HERE = os.path.dirname(__file__)
ROOT = os.path.join(HERE, "..", "..")
AUDIT = json.load(open(os.path.join(ROOT, "scripts/audit/data/thyroide-audit.json"), encoding="utf-8"))
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
        if COMMENT.match(t): comments.append(t); continue
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
    exp = []
    for m in marked:
        mt = norm(OPT.sub("", m.strip(), count=1))
        if len(mt) < 3: continue
        for i, o in enumerate(opts):
            no = norm(o)
            if no and (mt[:25] in no or no[:25] in mt):
                if "ABCDEFGHIJ"[i] not in exp: exp.append("ABCDEFGHIJ"[i])
                break
    return exp

# Numérotation stable des sections non datées (ND) : base + numéro dans la section.
ND_BASE = {"Maiter adulte – Thyroïde": 200, "Maiter adulte – Hypophyse": 300, "Lysy – Thyroïde": 160, "Marbaix – Anapath thyroïde/parathyroïdes/surrénales": 100,
           "Duprez + Coche – Imagerie": 0, "Horsmans – Pharmaco hormones": 0}
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
EXTRA_COMMENT = {"ND-marbaix-thyroide-parathyroides-Q2": "La proposition E est vraisemblablement une plaisanterie du transcripteur (proposition originale inconnue)."}

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
    if q["ref"] in TRUNCATE:
        opts = [o for o in opts if not o.startswith(TRUNCATE[q["ref"]])]
    opts = [re.sub(r"\s+[a-e]$", "", o) for o in opts]  # lettre orpheline en fin de ligne
    if q["ref"] in EXTRA_COMMENT: comments.append(EXTRA_COMMENT[q["ref"]])
    exp = expected_of(opts, q["marked"])
    status = STATUS[q["status"]]
    if q["ref"] in FORCE: status = FORCE[q["ref"]][0]
    instr = instruction_of(stem, len(exp))
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
    with open(os.path.join(OUTDIR, f"{name}.json"), "w", encoding="utf-8") as f:
        json.dump({"source": name, "questions": qs}, f, ensure_ascii=False, indent=2)
print(dict(report), sum(len(v) for v in files.values()), "questions importées dans", len(files), "fichiers")
for p in problems: print("À VÉRIFIER", p)
