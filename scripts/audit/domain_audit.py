"""Exporte les questions d'un domaine (hors thyroïde) à partir de l'audit, avec le classement manuel du domaine.

Usage : python3 scripts/audit/domain_audit.py W hypophyse
  W = dossier de travail de l'audit (contient final.json, voir README.md).
Produit :
  - scripts/audit/data/<domaine>-audit.json (données d'import des questions) ;
  - docs/audit/INVENTAIRE-<DOMAINE>.md et docs/audit/inventaire-<domaine>.csv.
"""
import csv, importlib, json, os, re, sys
from collections import defaultdict

W, DOM = sys.argv[1], sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", "..")
sys.path.insert(0, HERE)
cfg = importlib.import_module(DOM)
LABEL = {"hypophyse": ("Hypophyse", "Hypophyse"), "surrenales": ("Surrénales", "Surrénales"),
         "pharmaco": ("Pharmacologie générale (hors endocrinologie)", "Pharmacologie"),
         "obesite": ("Obésité, nutrition & syndrome métabolique", "Obésité et nutrition"),
         "diabete": ("Diabète & hypoglycémies", "Diabète")}[DOM]
# Intégration par parties (domaine volumineux) : « python3 domain_audit.py W diabete 1 » n'exporte que la partie 1 ;
# la partie N exporte les parties 1 à N (export cumulatif).
PART = sys.argv[3] if len(sys.argv) > 3 else None  # (domaine dans l'audit, titre du cours)

final = json.load(open(os.path.join(W, "final.json"), encoding="utf-8"))
# Le domaine de l'audit, plus les questions classées ailleurs par l'extraction et rattachées ici à la main.
pool = [q for q in final if q.get("domain") == LABEL[0] or (q["src"], q["line"]) in cfg.H]
keys = {(q["src"], q["line"]) for q in pool}
in_domain = {(q["src"], q["line"]) for q in final if q.get("domain") == LABEL[0]}
missing = (set(cfg.H) | set(cfg.EXCLUDE)) - keys
if getattr(cfg, "PEDIA_AUTO", False):  # toutes les questions de pédiatrie vont au cours de pédiatrie
    for q in pool:
        k = (q["src"], q["line"])
        if q["disc"] == "PEDIA" and k not in cfg.H: cfg.EXCLUDE.setdefault(k, cfg._PEDIA)
unclassified = in_domain - set(cfg.H) - set(cfg.EXCLUDE)
if missing or unclassified:
    sys.exit(f"classement incomplet : inconnues {sorted(missing)}, non classées {sorted(unclassified)}")

out = []
for q in pool:
    k = (q["src"], q["line"])
    if k in cfg.EXCLUDE: continue
    grp, status, note = cfg.H[k]
    sub, lessons, label = cfg.FAM[grp]
    out.append({
        "ref": q["ref"], "src": q["src"], "session": q["session"], "section": q["section"], "disc": q["disc"], "teacher": q["teacher"],
        "page": q["page"], "num": q["num"], "line": q["line"], "stem": q["stem"], "lines": q["lines"], "marked": q["marked"],
        "placeholder": q["placeholder"], "clinical": q["clinical"], "status": status or q["status"],
        "module": LABEL[1], "autres": "", "sous_theme": label, "note": note, "groupe": grp, "answer": q["answer"],
        "map": {"chapter": DOM, "subchapter": sub, "lessons": lessons[:3]},
    })
export = out
if PART:
    allowed = set().union(*(cfg.PARTS[k] for k in cfg.PARTS if k <= PART))
    export = [q for q in out if q["map"]["subchapter"] in allowed]
json.dump(export, open(os.path.join(HERE, "data", f"{DOM}-audit.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

SHORT = {"Réponse proposée dans la compilation": "🟦 proposée", "Réponse discutée ou contestée": "🟧 discutée", "Question incomplète": "⬜ incomplète",
         "Réponse absente": "🟥 absente", "Réponse déduite du texte, à vérifier": "🟨 déduite", "Question non retranscrite (seul le nom du transcripteur figure)": "⬛ non retranscrite"}
SES = {"2026-01": "janv. 2026", "2025-01": "janv. 2025", "2024-01": "janv. 2024", "2023-05": "mai 2023", "2022-05": "mai 2022", "2016-2021": "2016-2021"}
cut = lambda s, n: (lambda t: t if len(t) <= n else t[:n - 1] + "…")(re.sub(r"\s+", " ", s).strip().replace("|", "/"))
cnt = defaultdict(int)
for q in out: cnt[q["status"]] += 1
L = [f"# Inventaire détaillé des questions : {LABEL[1].lower()}", "",
     f"> Généré par `scripts/audit/domain_audit.py` à partir de l'extraction des PDF (voir `AUDIT-PHASE-1.md`) et du classement manuel `scripts/audit/{DOM}.py`.",
     f"> **{len(out)} questions** retenues : {len(in_domain)} classées automatiquement dans ce domaine, dont {len(cfg.EXCLUDE)} écartées (voir la fin), et {len(keys - in_domain)} rattachées depuis un autre domaine.",
     "> **Statuts** : 🟦 réponse proposée dans la compilation (en rouge) · 🟧 discutée/contestée · ⬜ question incomplète · 🟥 réponse absente · 🟨 déduite du texte.",
     "> Aucune correction officielle n'a été identifiée dans les sources.", "",
     "| Statut | Questions |", "|---|---:|"] + [f"| {SHORT[s]} | {n} |" for s, n in sorted(cnt.items(), key=lambda x: -x[1])] + [""]
order = list(cfg.FAM)
by = defaultdict(list)
for q in out: by[q["groupe"]].append(q)
for g in order:
    if g not in by: continue
    lst = by[g]
    L += [f"## {cfg.FAM[g][2]} ({len(lst)})", "", "| Réf. audit | Session · discipline · p. | Énoncé (début) | Réponse en rouge | Statut | Remarques |", "|---|---|---|---|---|---|"]
    for q in lst:
        L.append(f"| `{q['ref']}` | {SES[q['session']]} · {q['disc'].lower()} · p.{q['page']} | {cut(' '.join(q['stem']), 110)} | {cut(q['answer'], 70) or '—'} | {SHORT[q['status']]} | {cut(q['note'], 200) or '—'} |")
    L.append("")
L += ["## Questions écartées de ce domaine", "", "| Réf. audit | Raison |", "|---|---|"]
for q in pool:
    k = (q["src"], q["line"])
    if k in cfg.EXCLUDE: L.append(f"| `{q['ref']}` | {cfg.EXCLUDE[k]} |")
open(os.path.join(ROOT, "docs/audit", f"INVENTAIRE-{DOM.upper()}.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
with open(os.path.join(ROOT, "docs/audit", f"inventaire-{DOM}.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh, delimiter=";")
    w.writerow(["ref_audit", "session", "discipline", "enseignant", "page_pdf", "famille", "sous_chapitre", "lecons", "statut_correction", "reponse_marquee_en_rouge", "remarque", "enonce", "propositions"])
    for q in out:
        w.writerow([q["ref"], q["session"], q["disc"], q["teacher"], q["page"], q["groupe"], q["map"]["subchapter"], " ".join(q["map"]["lessons"]), q["status"], q["answer"], q["note"], " ".join(q["stem"]), " ¦ ".join(q["lines"])])
print(len(export), "questions exportées", f"(partie {PART}, sur {len(out)})" if PART else "", ";", dict(cnt))
