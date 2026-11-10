import json,re,sys,difflib
from collections import Counter,defaultdict
S=sys.argv[1]
d=json.load(open(f"{S}/inv_raw.json"))
MERGE_PREFIX=["taille une fois adulte","Toutes les propo sont vraies","glycémie systématiquement au-dessus","indétectable, anticorps négatifs",
 "2- lors du diagnostic du DT1","L’effet incrétine est augmenté","Complications au moment du diagnostic","Les sulfonylurés à longue durée",
 "Demander si autre maladie","Respiration rapide ?","Des anticorps anti-GAD signent","Quel est le diagnostic ?","Fluoangiographie",
 "Modifications morphologiques","l’hypophyse (?) et au MEN-2","Cancer folliculaire diagnostic par cytologie","B. peuvent etre associés",
 "proposition et donc il y en a une","charge de cette jeune fille","Glucocorticoide dans le traitement","Le C peptide peut être disable",
 "Insulinome est l’élément caractéristique","1er cause en Europe est la thyroïdite","Diarrhée ?","PPAR bêta","3 mg","Le diagnostic d’insuffisance en GH est aisé"]
DROP_EXACT={("2026-01","Preumont :"),("2026-01","Loumeye :"),("2026-01","Alexopoulou :")}
out=[];seen_dup11=False
for q in d:
    st=" ".join(q["stem"])
    if (q["session"],st) in DROP_EXACT: continue
    if st.startswith("Parmi ces propositions, une seule est correcte") and not q["lines"]: continue
    if out and any(st.startswith(m) for m in MERGE_PREFIX) and not (st.startswith("Quel est le diagnostic ?") and "Thyroïde" in q["section"]):
        p=out[-1]; p["lines"]+= [st]+q["lines"]; p["marked"]+=q["marked"]; continue
    out.append(q)
PLACEHOLDER=re.compile(r"^(AF|Momo|Wik|Antoine|Lidia|Oihan|Maïlys|Flavio, Alexandre|merlinios|Baptiste|Thomas G|Charlotte Pirson|Charlotte|Moi|Océane|Rosa|eden|Helena|Cla|Sacha|Mim|Jana|Juliette|Ysaline|MJ|MP|Emma N|Hypothyroidie)$")
REF=re.compile(r"même que|la même question|la meme question|même question|copié collé",re.I)
UNC=re.compile(r"pas s[uû]r|je pense|je crois|\?\?|jsp|je sais plus|je ne sais plus|plus s[uû]re|à confirmer|a confirmer|à vérifier|c.était pas|non \?|ou l.inverse|\(\?\)|annul|me souvien|j.ai oublié|oubli|pas hyper sur|soit ça, soit|help|jme souviens", re.I)
INC=re.compile(r"^\s*(\?+|…|\.\.\.|etc|E\. \?|e\. \?|D\. \?|\(oubli.*)\s*$|j.ai oublié|je sais plus les propositions|me souviens plus|jsp quoi|pas eu le temps|une longue proposition|Encore une que j|plus les chiffres", re.I)
INLINE=re.compile(r"(->|=>|⇒|🡺)\s*\S|c.est la [A-E]\b|c.était (ça|celle)|\(elle est juste\)|\(vrai\)|bonne réponse\)", re.I)
T=lambda q:(" ".join(q["stem"])+"\n"+"\n".join(q["lines"]))
THY=re.compile(r"thyro|thyré|basedow|graves|hashimoto|quervain|quievrain|goitre|go[iî]tre|tirads|cytoponction|ponction|calcitonine|thyroglob|amiodarone|strumaz|propylthio|\bPTU\b|\bATS\b|l-?thyrox|levothyr|lévothyr|guthrie|athyr|dyshormono|myx|h[uü]rthle|papillaire|folliculaire|anaplasique|wolff|exophtal|ophtalmopathie|\bTSH\b|\bT4\b|\bT3\b|carence en iode|iode|\bCMT\b|médullaire de la thyro|NEM ?2|MEN ?2", re.I)
DOM=[("Thyroïde",None),
 ("Diabète & hypoglycémies",re.compile(r"diab|glyc|insulin|hba1c|hb ?a1c|hgpo|ogtt|oggt|c[ée]tos|acidoc|hyperosmol|metformin|sulfamid|sulfonyl|glp|sglt|glifloz|gliflo|dpp|pedis|charcot|r[ée]tinopath|n[ée]phropath|neuropath|mody|lada|peptide|glinide|glitazon|incr[ée]tin|coma hypo|lipodyst",re.I)),
 ("Hypophyse",re.compile(r"hypophys|prolactin|acrom[ée]g|\bGH\b|IGF|apoplexie|sheehan|insipide|desmopress|minirin|craniopharyng|selle turcique|cabergol|quinagol|somatostat|neurohypo|tige pituitaire|panhypopit",re.I)),
 ("Surrénales",re.compile(r"surr[ée]n|cushing|addison|adisson|aldost|conn\b|ph[ée]ochrom|incidentalome|cortisol|ACTH|21.?hydrox|21 ?OH|17.?OH|hydrocortisone|dexam",re.I)),
 ("Gonades, puberté & croissance",re.compile(r"gyn[ée]comast|hypogonad|testost|klinefelter|kallman|ompk|sopk|ovaire|hirsut|[œo]estrog|progest|tamoxif|m[ée]nopause|turner|croissance|pubert|tanner|taille|courbe|th[ée]larche|pubarche|âge osseux|silver|noonan|m[ée]narche|prader|caryotype|ambigu|SGA|dysmatur|organes g[ée]nitaux|LHRH|testicul",re.I)),
 ("Obésité, nutrition & syndrome métabolique",re.compile(r"ob[ée]s|\bBMI\b|\bIMC\b|poids|bypass|by pass|bariatr|syndrome m[ée]tabolique|amaigrissement|sleeve",re.I)),
 ("Phosphocalcique & parathyroïdes",re.compile(r"parathyr|vitamine d|vit d|bisphosph|biphosph|calc[ée]mie|\bPTH\b|mibi",re.I)),
 ("Tumeurs neuroendocrines & NEM",re.compile(r"\bNEM|\bMEN|gastrinome|neuro-?endocrin|zollinger",re.I)),
 ("Pharmacologie générale (hors endocrino)",re.compile(r"cyclospor|ciclospor|sirolimus|azathiop|azatiop|allopurinol|\bfer\b|B12|folate|statine|ezetrol|ezetim|biodisponib|CYP",re.I)),
]
SECDOM={"Diabète":"Diabète & hypoglycémies","Thyroïde":"Thyroïde","Hypophyse":"Hypophyse","Surrénale":"Surrénales","Hypogonadisme":"Gonades, puberté & croissance","métabolique":"Obésité, nutrition & syndrome métabolique","bariatrique":"Obésité, nutrition & syndrome métabolique","Obésité":"Obésité, nutrition & syndrome métabolique","Croissance":"Gonades, puberté & croissance","Puberté":"Gonades, puberté & croissance","hématopoïèse":"Pharmacologie générale (hors endocrino)","immunosuppresseurs":"Pharmacologie générale (hors endocrino)","hypolipémiants":"Pharmacologie générale (hors endocrino)","phosphocalcique":"Phosphocalcique & parathyroïdes","hormones sexuelles":"Gonades, puberté & croissance","Anapath pancréas":"Diabète & hypoglycémies","Anapath hypophyse":"Hypophyse"}
for q in out:
    txt=T(q); st=" ".join(q["stem"])
    q["placeholder"]=bool(PLACEHOLDER.match(st.strip())) and not q["lines"]
    q["reference_only"]=bool(REF.search(st)) and len(q["lines"])<2
    q["lines"]=[l for l in q["lines"] if not re.match(r"^\d{1,3}\s*[.\-]?\s*$",l)]
    opts=[l for l in q["lines"] if not re.match(r"^(->|=>|\(|\[)",l)]
    q["n_opts"]=len(opts)
    q["has_mark"]=len(q["marked"])>0
    q["inline"]=bool(INLINE.search(txt))
    q["uncertain"]=bool(UNC.search(txt))
    q["incomplete"]= (not q["placeholder"]) and (q["n_opts"]<3 or bool(INC.search(txt)) or q["reference_only"])
    dom=None
    sec=q["section"]
    if THY.search(txt) and not re.search(r"adénome hypophysaire.*(TSH|T4)|IGF1 augment|igf1\s*augment",txt,re.I):
        dom="Thyroïde"
    if dom is None and q["session"]=="2016-2021":
        for k,v in SECDOM.items():
            if k in sec: dom=v;break
    if dom is None:
        for name,rx in DOM[1:]:
            if rx.search(txt): dom=name;break
    q["domain"]=dom or "Autre / non classable"
    lo=txt.lower()
    if re.search(r"associez",lo): typ="Association"
    elif re.search(r"2 fausses|deux fausses|2 faux|sauf 2|sauf deux|2 réponses fausses|deux réponses fausses|les 2 deux fausses|2f\b|2 qui ne|2 ne diminuent|\(2 réponses\)|ne sont pas.*\(2|sauf 2|2 informations",lo): typ="QCM – deux fausses / deux réponses"
    elif re.search(r"2 vraies|deux vraies|2 justes|deux justes|2 propositions correctes|2 bonnes|deux réponses|2 réponses|\(2v\)|2 causes|2 médicaments|2 diagnostics|2 éléments|deux justes",lo): typ="QCM – deux bonnes réponses"
    elif re.search(r"fausse|faux|sauf|1f\b|\bla f\b|ne .* pas|n.est pas|n.apparait|impossible|à exclure|inutile|mauvaise",lo): typ="QCM – une fausse / « sauf une »"
    elif re.search(r"vraie|vrai\b|juste|correcte|exacte",lo): typ="QCM – une vraie"
    else: typ="QCM – une réponse"
    q["type"]=typ
    q["clinical"]=bool(re.search(r"\b\d{1,2}\s*(ans|jours|j de vie|mois)\b|patient|patiente|dame|monsieur|\bmr\b|madame|femme de|homme de|enfant de|bébé|bb |nouveau-né|cas clinique|consultation|urgences|[A-Z][a-zé]+,? \d+ ans",txt,re.I))
    # status
    if q["placeholder"]: s="Question non retranscrite (seul le nom du transcripteur figure)"
    elif q["reference_only"] or (q["n_opts"]==0 and not q["has_mark"]): s="Question incomplète"
    elif q["has_mark"] and q["uncertain"]: s="Réponse discutée ou contestée"
    elif q["has_mark"]: s="Réponse proposée dans la compilation"
    elif q["inline"]: s="Réponse déduite du texte, à vérifier"
    else: s="Réponse absente"
    q["status"]=s
json.dump(out,open(f"{S}/inv.json","w"),ensure_ascii=False,indent=0)
real=[q for q in out if not q["placeholder"]]
print("total entries",len(out),"placeholders",len(out)-len(real),"real",len(real))
print(Counter(q["session"] for q in real))
print(Counter(q["domain"] for q in real))
print(Counter(q["status"] for q in out))
print(Counter(q["type"] for q in real))
print("clinical",sum(q["clinical"] for q in real),"incomplete",sum(q["incomplete"] for q in real))
