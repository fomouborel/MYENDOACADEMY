import json,sys,re
from collections import Counter,defaultdict
S=sys.argv[1]; OUT=sys.argv[2]
th=json.load(open(S+"/thy.json"))
FAM={"NOD-SUSP":"Nodule – arguments de malignité","NOD-BILAN":"Nodule – bilan initial","CYTOPONCTION":"Nodule – échographie et indications de cytoponction","EUTIRADS":"Échographie – EU-TIRADS","CANCERS":"Cancers thyroïdiens","FOLLICULAIRE":"Anapath – carcinome folliculaire","CMT-ANAPATH":"Anapath – carcinome médullaire","HASHI-ANAPATH":"Anapath – Hashimoto","BASEDOW-ANAPATH":"Anapath – Basedow","QUERVAIN":"Thyroïdite de De Quervain","SILENCIEUSE":"Thyroïdite silencieuse","TSH-BASSE":"Interprétation d'une TSH basse / facteurs modifiant la TSH","GOITRE":"Goitre – étiologies et évolution","WOLFF":"Physiologie – iode, Wolff-Chaikoff, médicaments","IODE":"Carence iodée","T3-BASSE":"Maladie non thyroïdienne (« T3 basse »)","SCINTI":"Scintigraphie – indications","ECHO-THYROIDITE":"Échographie – thyroïdite auto-immune","ETIO-HYPER":"Étiologies de l'hyperthyroïdie","BASEDOW":"Basedow – clinique","BASEDOW-ATS":"Basedow – traitement (ATS, grossesse, rechutes)","ORBITOPATHIE":"Orbitopathie basedowienne","ECHO-BASEDOW":"Échographie – Basedow","GMN":"Goitre multinodulaire toxique","EXOGENE":"Hyperthyroïdie factice / Tg et anticorps","AMIODARONE":"Amiodarone","CENTRALE-HYPER":"Hyperthyroïdie d'origine centrale (adénome thyréotrope)","ATS-PHARMA":"Pharmacologie – antithyroïdiens de synthèse","SUIVI-HYPO":"Diagnostic et suivi de l'hypothyroïdie","HYPO-ADULTE":"Hypothyroïdie de l'adulte (causes, traitement, grossesse)","HYPO-BIO":"Hypothyroïdie sévère – biologie","LT4-AGEE":"L-thyroxine – surdosage chez la personne âgée","HYPO-CENTRALE":"Hypothyroïdie centrale – surveillance par la T4 libre","ES-HT":"Pharmacologie – hormones thyroïdiennes","PEDIA-THYR":"Thyroïde de l'enfant","NN-TSH":"Hypothyroïdie congénitale – conduite après dépistage","NN-SIGNES":"Hypothyroïdie congénitale – signes","NN-ETIO":"Hypothyroïdie congénitale – étiologie (Tg)","NN-DOSE":"Hypothyroïdie congénitale – dose de L-thyroxine","GUTHRIE":"Dépistage néonatal (Guthrie)","SUBCLIN-PEDIA":"Hypothyroïdie infraclinique de l'enfant","CROISSANCE-THYR":"Hypothyroïdie et courbe de croissance","—":"Non retranscrite"}
SHORT={"Réponse proposée dans la compilation":"🟦 proposée","Réponse discutée ou contestée":"🟧 discutée","Question incomplète":"⬜ incomplète","Réponse absente":"🟥 absente","Réponse déduite du texte, à vérifier":"🟨 déduite","Question non retranscrite (seul le nom du transcripteur figure)":"⬛ non retranscrite"}
SES={"2026-01":"janv. 2026","2025-01":"janv. 2025","2024-01":"janv. 2024","2023-05":"mai 2023","2022-05":"mai 2022","2016-2021":"2016-2021"}
def cut(s,n): s=re.sub(r"\s+"," ",s).strip().replace("|","/"); return s if len(s)<=n else s[:n-1]+"…"
L=["# Inventaire détaillé des questions sur la thyroïde","","> Généré à partir de l'extraction des PDF (voir `AUDIT-PHASE-1.md`). Tableur complet : `inventaire-thyroide.csv` (énoncés et propositions intégraux).","> **Statuts** : 🟦 réponse proposée dans la compilation (en rouge) · 🟧 discutée/contestée · ⬜ question incomplète · 🟥 réponse absente · 🟨 déduite du texte · ⬛ non retranscrite.","> Aucune correction officielle n'a été identifiée dans les sources.",""]
for mod in ["Pathologies thyroïdiennes","Hyperthyroïdie","Hypothyroïdie"]:
    qs=[q for q in th if q["module"]==mod]
    L+=[f"## {mod} — {len(qs)} questions (module principal)",""]
    byf=defaultdict(list)
    for q in qs: byf[q["groupe"]].append(q)
    for g,lst in byf.items():
        L+=[f"### {FAM.get(g,g)} ({len(lst)})","","| Réf. audit | Session · discipline · p. | Énoncé (début) | Réponse en rouge | Statut | Autres modules | Remarques |","|---|---|---|---|---|---|---|"]
        for q in lst:
            L.append(f"| `{q['ref']}` | {SES[q['session']]} · {q['disc'].lower()} · p.{q['page']} | {'(non retranscrite)' if q['placeholder'] else cut(' '.join(q['stem']),110)} | {cut(q['answer'],70) or '—'} | {SHORT[q['status']]} | {q['autres'] or '—'} | {cut(q['note'],160) or '—'} |")
        L.append("")
open(OUT+"/INVENTAIRE-THYROIDE.md","w").write("\n".join(L))
print(len(L))
