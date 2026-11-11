"""Ajoute indices, explications et remarques par proposition aux questions d'archives importées.

Les textes sont des compléments rédigés (statut « complement », affichés « à valider »).
Ils ne modifient jamais l'énoncé, les propositions ni la réponse retenue.
Données : scripts/content/explications/*.py (un dictionnaire EXPL par cours).
Relançable sans effet de bord : seuls les champs ci-dessous sont (ré)écrits.
"""
import glob, importlib.util, json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
QDIR = os.path.join(ROOT, "content/questions")

def typo(s):
    return s.replace("'", "’")

EXPL = {}
for path in sorted(glob.glob(os.path.join(os.path.dirname(__file__), "explications/*.py"))):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    for k in mod.EXPL:
        if k in EXPL: sys.exit(f"identifiant en double dans les explications : {k}")
    EXPL.update(mod.EXPL)

seen, errors = set(), []
for f in sorted(glob.glob(os.path.join(QDIR, "*.json"))):
    data = json.load(open(f, encoding="utf-8")); changed = False
    for q in data["questions"]:
        x = EXPL.get(q["id"])
        if not x: continue
        seen.add(q["id"])
        if len(x["h"]) != 3: errors.append(f"{q['id']} : il faut 3 indices"); continue
        if len(x["o"]) != len(q["options"]): errors.append(f"{q['id']} : {len(x['o'])} remarques pour {len(q['options'])} propositions"); continue
        q["hints"] = [typo(h) for h in x["h"]]
        q["explanation"] = {"text": typo(x["e"]), "status": "complement", "sources": []}
        for o, t in zip(q["options"], x["o"]): o["explanation"] = typo(t)
        if x.get("p"): q["pitfall"] = typo(x["p"])
        if x.get("status"):  # réponse requalifiée « discutée » : jamais l'inverse
            assert x["status"] == "disputed", q["id"]
            q["answerStatus"] = "disputed"; q["answerNote"] = typo(x["note"])
        changed = True
    if changed:
        with open(f, "w", encoding="utf-8") as out:
            json.dump(data, out, ensure_ascii=False, indent=2)
missing = set(EXPL) - seen
for m in sorted(missing): errors.append(f"{m} : identifiant inconnu")
for e in errors: print("ERREUR", e)
print(f"{len(seen)} question(s) complétée(s).")
sys.exit(1 if errors else 0)
