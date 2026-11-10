import json,sys,csv,re,difflib,os
from collections import Counter,defaultdict
S=sys.argv[1]; OUT=sys.argv[2]
d=json.load(open(S+"/final.json"))
real=[q for q in d if not q["placeholder"]]
NR=[q for q in d if q["placeholder"]]
norm=lambda s: re.sub(r"[^a-z0-9]","",s.lower())
def sig(q):
    st=" ".join(q["stem"]); st=re.sub(r"^\d+\s*[.\-)]\s*","",st)
    return norm(st+" ".join(q["lines"][:3]))
# duplicates
items=[(i,sig(q)) for i,q in enumerate(real) if len(sig(q))>=40]
parent=list(range(len(real)))
def f(x):
    while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
    return x
for a in range(len(items)):
    ia,sa=items[a]
    for b in range(a+1,len(items)):
        ib,sb=items[b]
        if abs(len(sa)-len(sb))>0.5*max(len(sa),len(sb)): continue
        r=difflib.SequenceMatcher(None,sa[:160],sb[:160]).quick_ratio()
        if r<0.8: continue
        r=difflib.SequenceMatcher(None,sa[:160],sb[:160]).ratio()
        if r>=0.8: parent[f(ia)]=f(ib)
groups=defaultdict(list)
for i,q in enumerate(real): groups[f(i)].append(i)
dupg=[g for g in groups.values() if len(g)>1]
gid={}
for n,g in enumerate(sorted(dupg,key=lambda g:-len(g)),1):
    for i in g: gid[i]=f"D{n:03d}"
for i,q in enumerate(real): q["dup_auto"]=gid.get(i,"")
st={}
st["entries"]=len(d); st["real"]=len(real); st["not_transcribed"]=len(NR)
st["by_session"]=Counter(q["session"] for q in real)
st["nr_by_session"]=Counter(q["session"] for q in NR)
st["by_disc"]=Counter(q["disc"] for q in real)
st["by_session_disc"]={s:dict(Counter(q["disc"] for q in real if q["session"]==s)) for s in st["by_session"]}
st["by_teacher"]=Counter(q["teacher"] for q in real)
st["by_domain"]=Counter(q["domain"] for q in real)
st["by_domain_session"]={dm:dict(Counter(q["session"] for q in real if q["domain"]==dm)) for dm in st["by_domain"]}
st["by_type"]=Counter(q["type"] for q in real)
st["clinical"]=sum(q["clinical"] for q in real)
st["status"]=Counter(q["status"] for q in d)
st["incomplete"]=sum(q["status"]=="Question incomplète" for q in real)
st["with_answer"]=sum((q["has_mark"] or q["inline"]) for q in real)
st["to_verify"]=sum(q["status"] in ("Réponse discutée ou contestée","Réponse déduite du texte, à vérifier") for q in real)
st["incomplete_with_answer"]=sum(q["status"]=="Question incomplète" and q["has_mark"] for q in real)
st["dup_groups"]=len(dupg); st["dup_questions"]=sum(len(g) for g in dupg)
st["dup_sizes"]=Counter(len(g) for g in dupg)
th=[q for q in d if q["thyroid"]=="principale"]
st["thy_total"]=len(th); st["thy_transv"]=sum(q["thyroid"]=="transversale" for q in d)
st["thy_module"]=Counter(q["module"] for q in th)
st["thy_multi"]=sum(bool(q["autres"]) for q in th)
st["thy_multi_detail"]=Counter(q["module"]+" + "+q["autres"] for q in th if q["autres"])
st["thy_session"]=Counter(q["session"] for q in th)
st["thy_session_module"]={s:dict(Counter(q["module"] for q in th if q["session"]==s)) for s in st["thy_session"]}
st["thy_disc"]=Counter(q["disc"] for q in th)
st["thy_teacher"]=Counter(q["teacher"] for q in th)
st["thy_status"]=Counter(q["status"] for q in th)
st["thy_status_module"]={m:dict(Counter(q["status"] for q in th if q["module"]==m)) for m in st["thy_module"]}
st["thy_type"]=Counter(q["type"] for q in th)
st["thy_clinical"]=sum(q["clinical"] for q in th)
st["thy_groups"]=Counter(q["groupe"] for q in th)
st["thy_sous"]=Counter(q["module"]+" | "+q["sous_theme"] for q in th)
json.dump({k:(dict(v) if isinstance(v,Counter) else v) for k,v in st.items()},open(S+"/stats.json","w"),ensure_ascii=False,indent=1,default=str)
os.makedirs(OUT,exist_ok=True)
SRCNAME={"A":"Compilation endocrino 2016-2024","E":"Retranscription janvier 2025","G":"Retranscription janvier 2026"}
def opts(q): return "" if q["placeholder"] else " ¦ ".join(q["lines"])[:600]
def stem(q): return "(question non retranscrite – nom du transcripteur masqué)" if q["placeholder"] else " ".join(q["stem"])
with open(OUT+"/inventaire-complet.csv","w",newline="",encoding="utf-8") as fh:
    w=csv.writer(fh,delimiter=";")
    w.writerow(["ref_audit","session","section_source","discipline","discipline_deduite","enseignant","page_pdf","ligne_extraction","domaine","thyroide","type","cas_clinique","statut_correction","reponse_marquee_en_rouge","enonce","propositions_et_commentaires","doublon_auto","source"])
    for q in d:
        w.writerow([q["ref"],q["session"],q["section"],q["disc"],"oui" if q["disc_inferred"] else "non",q["teacher"],q["page"],q["line"],q["domain"],q["thyroid"],q["type"],"oui" if q["clinical"] else "non",q["status"],q["answer"],stem(q),opts(q),q.get("dup_auto",""),SRCNAME[q["src"]]])
ORDERS={"2026-01":0,"2025-01":1,"2024-01":2,"2023-05":3,"2022-05":4,"2016-2021":5}
th_sorted=sorted(th,key=lambda q:(["Pathologies thyroïdiennes","Hyperthyroïdie","Hypothyroïdie"].index(q["module"]),q["groupe"],ORDERS[q["session"]]))
with open(OUT+"/inventaire-thyroide.csv","w",newline="",encoding="utf-8") as fh:
    w=csv.writer(fh,delimiter=";")
    w.writerow(["ref_audit","module_principal","autres_modules","sous_theme","famille_doublons","session","discipline","enseignant","page_pdf","type","cas_clinique","statut_correction","reponse_marquee_en_rouge","remarques","enonce","propositions_et_commentaires","source"])
    for q in th_sorted:
        w.writerow([q["ref"],q["module"],q["autres"],q["sous_theme"],q["groupe"],q["session"],q["disc"],q["teacher"],q["page"],q["type"],"oui" if q["clinical"] else "non",q["status"],q["answer"],q["note"],stem(q),opts(q),SRCNAME[q["src"]]])
json.dump(th_sorted,open(S+"/thy.json","w"),ensure_ascii=False,indent=0)
print(json.dumps({k:(dict(v) if isinstance(v,Counter) else v) for k,v in st.items() if k not in ("thy_sous","thy_multi_detail","by_domain_session","thy_groups")},ensure_ascii=False,indent=0,default=str))
