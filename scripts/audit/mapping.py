import json,sys,re
S=sys.argv[1]
th=json.load(open(S+"/thy.json"))
F={
"NOD-SUSP":("thyroide","nodules",["thyr-nodules"]),"NOD-BILAN":("thyroide","nodules",["thyr-nodules"]),"CYTOPONCTION":("thyroide","nodules",["thyr-nodules"]),"EUTIRADS":("thyroide","nodules",["thyr-nodules"]),
"CANCERS":("thyroide","cancers",["thyr-cancers"]),"FOLLICULAIRE":("thyroide","cancers",["thyr-cancers"]),"CMT-ANAPATH":("thyroide","cancers",["thyr-cancers"]),
"QUERVAIN":("thyroide","thyroidites",["thyr-thyroidites","hyper-diagnostic"]),"SILENCIEUSE":("thyroide","thyroidites",["thyr-thyroidites","hyper-diagnostic"]),
"HASHI-ANAPATH":("thyroide","thyroidites",["thyr-thyroidites","hypo-diagnostic"]),"ECHO-THYROIDITE":("thyroide","thyroidites",["thyr-thyroidites"]),
"BASEDOW-ANAPATH":("thyroide","thyroidites",["thyr-thyroidites","hyper-basedow"]),
"TSH-BASSE":("thyroide","explo",["thyr-explo","hyper-diagnostic"]),"WOLFF":("thyroide","explo",["thyr-explo"]),"T3-BASSE":("thyroide","explo",["thyr-explo"]),"SCINTI":("thyroide","explo",["thyr-explo"]),
"GOITRE":("thyroide","goitre",["thyr-goitre"]),"IODE":("hypo","diagnostic",["hypo-diagnostic","thyr-goitre"]),
"ETIO-HYPER":("hyper","diagnostic",["hyper-diagnostic"]),"EXOGENE":("hyper","diagnostic",["hyper-diagnostic","hyper-autres"]),"GMN":("hyper","diagnostic",["hyper-autres","hyper-diagnostic"]),"CENTRALE-HYPER":("hyper","diagnostic",["hyper-autres"]),
"BASEDOW":("hyper","basedow",["hyper-basedow"]),"BASEDOW-ATS":("hyper","basedow",["hyper-basedow","hyper-traitements"]),"ORBITOPATHIE":("hyper","basedow",["hyper-basedow"]),"ECHO-BASEDOW":("hyper","basedow",["hyper-basedow"]),"ATS-PHARMA":("hyper","basedow",["hyper-traitements"]),
"AMIODARONE":("hyper","iatrogene",["hyper-autres"]),
"SUIVI-HYPO":("hypo","diagnostic",["hypo-diagnostic","hypo-traitement"]),"HYPO-ADULTE":("hypo","diagnostic",["hypo-diagnostic","hypo-grossesse"]),"HYPO-BIO":("hypo","diagnostic",["hypo-diagnostic"]),
"LT4-AGEE":("hypo","traitement",["hypo-traitement"]),"ES-HT":("hypo","traitement",["hypo-traitement"]),"HYPO-CENTRALE":("hypo","traitement",["hypo-traitement","hypo-diagnostic"]),
"PEDIA-THYR":("hypo","congenitale",["hypo-congenitale"]),"NN-TSH":("hypo","congenitale",["hypo-congenitale"]),"NN-SIGNES":("hypo","congenitale",["hypo-congenitale"]),"NN-ETIO":("hypo","congenitale",["hypo-congenitale"]),
"NN-DOSE":("hypo","congenitale",["hypo-congenitale"]),"GUTHRIE":("hypo","congenitale",["hypo-congenitale"]),"SUBCLIN-PEDIA":("hypo","congenitale",["hypo-congenitale"]),"CROISSANCE-THYR":("hypo","congenitale",["hypo-congenitale"]),
"—":("hypo","diagnostic",[]),
}
PREG_REFS={"ND-maiter-thyroide-Q14","ND-maiter-thyroide-Q29","2022-05-Q37","ND-maiter-thyroide-Q10"}
out=[]
for q in th:
    ch,sub,ll=F[q["groupe"]]
    txt=" ".join(q["stem"])+" "+" ".join(q["lines"])
    ll=list(ll)
    if q["ref"] in PREG_REFS and "hypo-grossesse" not in ll: ll.append("hypo-grossesse")
    q["map"]=dict(chapter=ch,subchapter=sub,lessons=ll[:3])
    out.append(q)
json.dump(out,open(S+"/thy_map.json","w"),ensure_ascii=False,indent=0)
from collections import defaultdict
per=defaultdict(list)
for q in out:
    for l in q["map"]["lessons"]: per[l].append(q)
for l in sorted(per):
    qs=per[l]
    print(f"\n### {l} ({len(qs)})")
    for q in qs:
        print(f"- {q['ref']} [{q['status'][:12]}] {' '.join(q['stem'])[:80]} || {q['answer'][:60]}")

import csv
LT={"thyr-explo":"Physiologie et exploration","thyr-nodules":"Nodules","thyr-cancers":"Cancers","thyr-thyroidites":"Thyroïdites","thyr-goitre":"Goitres et grossesse","hyper-diagnostic":"Hyper – diagnostic","hyper-basedow":"Basedow","hyper-autres":"Hyper – autres causes","hyper-traitements":"Hyper – traitements","hypo-diagnostic":"Hypo – diagnostic","hypo-traitement":"L-thyroxine","hypo-grossesse":"Hypo – grossesse, formes sévères","hypo-congenitale":"Congénitale et enfant"}
with open(sys.argv[2],"w",newline="",encoding="utf-8") as fh:
    w=csv.writer(fh,delimiter=";")
    w.writerow(["ref_audit","session","discipline","module_principal","chapter","subchapter","lessonLinks","lecons","famille","statut_correction","enonce"])
    for q in out:
        m=q["map"]
        w.writerow([q["ref"],q["session"],q["disc"],q["module"],m["chapter"],m["subchapter"]," ".join(m["lessons"])," | ".join(LT[l] for l in m["lessons"]),q["groupe"],q["status"],"(non retranscrite)" if q["placeholder"] else " ".join(q["stem"])[:200]])
