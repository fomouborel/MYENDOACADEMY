import json,re,sys,csv,difflib
from collections import Counter,defaultdict
S=sys.argv[1]; OUT=sys.argv[2]; sys.path.insert(0,S+"/tools")
from thyroid import T,TRANSV
d=json.load(open(f"{S}/inv.json"))
IN="Question incomplète"; NR="Question non retranscrite (seul le nom du transcripteur figure)"
INC=re.compile(r"^\s*(\?+|…|\.\.\.|etc|[A-Ea-e][.)]\s*\?+|\(oubli.*)\s*$|j.ai oublié|je sais plus les propositions|me souviens plus|jsp quoi|pas eu le temps|une longue proposition|Encore une que j|plus les chiffres|je ne me rappelle plus",re.I|re.M)
TEACH_ADULT={"2022-05":"non attribué (adulte)","2023-05":"non attribué (adulte)","2024-01":"non attribué (adulte)","2025-01":"non attribué (adulte)"}
for q in d:
    txt=" ".join(q["stem"])+"\n"+"\n".join(q["lines"])
    # discipline for mixed sessions
    if q["disc"]=="MIXTE":
        n=q["num"]
        if n is not None and n<=55: disc="ADULTE"
        elif n is not None and re.search(r"cytoponction|ponction|imagerie|IRM|scinti|parenchymograph|neurohypophyse.*imagerie"," ".join(q["stem"]),re.I) and n<=85: disc="RADIO"
        elif n is not None and re.search(r"vit B12|vitamine B12|folate|cyclospor|sulfamid|gliflozine|glifozine|œstrogènes|Œstrogènes",txt,re.I) and n>75: disc="PHARMA"
        elif n is not None and n<=75: disc="PEDIA"
        elif n is not None and n<=85: disc="ANAPATH" if re.search(r"anapath|histolog|hyperplasie des parathyro|Hashimoto|folliculaire encapsul|tumeurs neuro|DT2 qu|couleur",txt,re.I) else "RADIO"
        elif n is not None: disc="PHARMA"
        else:
            if re.search(r"anapath",txt,re.I): disc="ANAPATH"
            elif re.search(r"Lysy|enfant|bébé|courbe|puberté|né à terme|maternité|telarche|Définition de la puberté",txt,re.I): disc="PEDIA"
            elif re.search(r"radio|imagerie|ponction|IRM|CT\b|hypophyse \(une fausse\)",txt,re.I): disc="RADIO"
            else: disc="ADULTE"
        q["disc_inferred"]=True; q["disc"]=disc
    else: q["disc_inferred"]=False
    if not q["teacher"]:
        q["teacher"]={"PEDIA":"Lysy","PHARMA":"Horsmans","ANAPATH":"Marbaix" if q["session"]!="2026-01" else "non précisé","RADIO":"Coche / Duprez" if q["session"]=="2023-05" else "non précisé"}.get(q["disc"],"non attribué (adulte)")
    # status
    if re.match(r"^(Flavio, Alexandre|eden|Helena|Cla|\(Pharmaco 100pct tuyau\))",(" ".join(q["stem"])).strip()) and q["n_opts"]<=3: q["placeholder"]=True
    if q["placeholder"]: st=NR
    elif q["reference_only"] or q["n_opts"]<3 or INC.search(txt): st=IN
    elif q["has_mark"] and q["uncertain"]: st="Réponse discutée ou contestée"
    elif q["has_mark"]: st="Réponse proposée dans la compilation"
    elif q["inline"]: st="Réponse déduite du texte, à vérifier"
    else: st="Réponse absente"
    q["status"]=st
    k=(q["src"],q["line"])
    q["thyroid"]="principale" if k in T else ("transversale" if k in TRANSV else "")
    if k in T:
        mod,autres,sous,ov,note,grp=T[k]
        q.update(module=mod,autres=autres,sous_theme=sous,note=note,groupe=grp,domain="Thyroïde")
        if ov: q["status"]=ov
        elif q["status"] in (IN,): pass
    else:
        from post_dom import redomain
        q["domain"]=redomain(q)
    if q["session"]=="2016-2021":
        import unicodedata
        sl=unicodedata.normalize("NFD",q["section"]).encode("ascii","ignore").decode().lower()
        sl=re.sub(r"\(.*?\)","",sl); sl=re.sub(r"[^a-z]+","-",sl).strip("-")
        sl=sl.replace("-adulte","").replace("anapath-","").replace("pharmaco-","")
        sl="-".join(sl.split("-")[:3])
        q["ref"]=f'ND-{sl}-' + (f'Q{q["num"]}' if q["num"] is not None else f'p{q["page"]}-l{q["line"]}')
    else:
        q["ref"]=f'{q["session"]}-' + (f'Q{q["num"]}' if q["num"] is not None else f'p{q["page"]}-l{q["line"]}')
    q["answer"]=" | ".join(m for m in q["marked"])[:300]
seen={}
for q in d:
    r=q["ref"]
    if r in seen:
        seen[r]+=1; q["ref"]=r+"abcdefgh"[seen[r]-1]
    else: seen[r]=1
json.dump(d,open(f"{S}/final.json","w"),ensure_ascii=False,indent=0)
