"""Compacte la sortie de extract.py : « … » = texte rouge ou surligné ; supprime les puces vides."""
import sys, re
out = []
for l in open(sys.argv[1], encoding="utf-8"):
    l = l.rstrip()
    s = re.sub(r"⟦[A-Za-z0-9]+:\s*([-•]|[a-eA-E][.)]|)\s*⟧", "", l).strip()
    if re.fullmatch(r"[-•]|[a-eA-E][.)]?|\d{1,3}|", s):
        continue
    l = re.sub(r"\s+", " ", l).strip()
    l = l.replace("⟦R:", "«").replace("⟦H:", "«").replace("⟧", "»")
    l = re.sub(r"»\s*«", " ", l)
    out.append(l)
open(sys.argv[2], "w", encoding="utf-8").write("\n".join(out))
