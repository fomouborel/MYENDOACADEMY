import sys, pymupdf
from collections import Counter
src, out = sys.argv[1], sys.argv[2]
doc = pymupdf.open(src)
cols = Counter()
def cname(c):
    r,g,b = (c>>16)&255,(c>>8)&255,c&255
    if max(r,g,b) < 90 and max(r,g,b)-min(r,g,b) < 40: return None  # black/dark grey
    if r>150 and g<110 and b<110: return "R"
    if g>120 and r<120 and b<140: return "G"
    if b>150 and r<120: return "B"
    if r>180 and g>120 and b<80: return "O"
    return "C%06x" % c
with open(out,"w") as f:
    for pno, page in enumerate(doc, 1):
        # highlight-like fills
        fills=[]
        for d in page.get_drawings():
            fc = d.get("fill")
            if fc and d["rect"].height < 30 and not (fc[0]>0.95 and fc[1]>0.95 and fc[2]>0.95) and not (max(fc)<0.1):
                fills.append((d["rect"], fc))
        for a in page.annots() or []:
            fills.append((a.rect, ("annot", a.type[1])))
        f.write(f"\n=====PAGE {pno}=====\n")
        d = page.get_text("dict")
        for b in d["blocks"]:
            for l in b.get("lines", []):
                parts=[]
                for s in l["spans"]:
                    t = s["text"]
                    if not t.strip(): parts.append(t); continue
                    c = cname(s["color"]); cols[c]+=1
                    hl = any(pymupdf.Rect(s["bbox"]).intersects(r) and pymupdf.Rect(s["bbox"]).intersect(r).get_area() > 0.5*pymupdf.Rect(s["bbox"]).get_area() for r,_ in fills)
                    flags = s["flags"]
                    tag = (c or "") + ("H" if hl else "")
                    if tag: t = f"⟦{tag}:{t}⟧"
                    parts.append(t)
                line="".join(parts).rstrip()
                if line.strip(): f.write(line+"\n")
print(src, cols.most_common(12), file=sys.stderr)
