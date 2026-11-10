import re
R=lambda p: re.compile(p,re.I)
HYP=R(r"hypophys|hypoph|prolactinome|macropolactinome|prolactin|acrom[ée]g|apoplexie|sheehan|insipide|desmopress|minirin|craniopharyng|selle turcique|cabergol|quinagol|somatostat|neurohypo|tige pituitaire|panhypopit|macroad[ée]nome|microad[ée]nome|ad[ée]nome (de l.)?hypo|parenchymograph|chiasma|champs? visuel|h[ée]mianopsie")
SUR=R(r"surr[ée]n|cushing|addison|adisson|aldost|\bconn\b|ph[ée]ochrom|pheocrom|incidentalome|ACTH|21.?hydrox|21 ?OH|17.?OH|hydrocortisone|cortisol")
CRO=R(r"croissance|pubert|tanner|taille|courbe|th[ée]larche|pubarche|âge osseux|age osseux|turner|silver|noonan|m[ée]narche|ambigu|SGA|dysmatur|organes g[ée]nitaux|LHRH|IGF|\bGH\b|né à terme|poids en moyenne|Achille|caryotype|cartilages|Kraainem|Solange|Prader|A\dP\d|tumeur à testost")
GON=R(r"gyn[ée]comast|hypogonad|hypoginad|Œstrog|testost[ée]rone|klinefelter|kallman|ompk|sopk|ovaire|hirsut|[œo]estrog|progest|tamoxif|m[ée]nopause|testicul")
OBE=R(r"ob[ée]s|\bBMI\b|\bIMC\b|poids|bypass|by pass|bariatr|syndrome m[ée]tabolique|amaigrissement|sleeve|p[ée]rim[eè]tre abdo|taille/ ?hanche|excès pondéral")
PCA=R(r"parathyr|vitamine d|vit d\b|bisphosph|biphosph|calc[ée]mie|\bPTH\b|mibi")
NEM=R(r"\bNEM|\bMEN ?\d|gastrinome|neuro-?endocrin|zollinger")
PHG=R(r"cyclospor|ciclospor|sirolimus|azathiop|azatiop|allopurinol|besoin journalier de fer|quantité journalière.*fer|B12|folate|statine|ezetrol|ezetim|biodisponib|CYP")
DIA=R(r"diab[èée]t(?! insipide)|\bDT2\b|\bDT1\b|Novorapid|glyc|insulin|hba1c|hb ?a1c|hbac|hgpo|ogtt|oggt|c[ée]tos|acidoc|hyperosmol|metformin|sulfamid|sulfonyl|glp|sglt|glifloz|gliflo|dpp|pedis|charcot|r[ée]tinopath|n[ée]phropath|neuropath|mody|lada|peptide|glinide|glitazon|incr[ée]tin|lipodyst|biguanide|glycation|œdème cérébral|oedème cérébral")
ORDER_STEM=[("Hypophyse",HYP),("Surrénales",SUR),("Croissance & puberté (pédiatrie)",CRO),("Gonades & hormones sexuelles",GON),("Phosphocalcique & parathyroïdes",PCA),("Tumeurs neuroendocrines & NEM",NEM),("Pharmacologie générale (hors endocrinologie)",PHG),("Obésité, nutrition & syndrome métabolique",OBE),("Diabète & hypoglycémies",DIA)]
ORDER_FULL=[("Diabète & hypoglycémies",DIA)]+ORDER_STEM[:-1]
SEC={"– Diabète":"Diabète & hypoglycémies","Hypophyse":"Hypophyse","Surrénale":"Surrénales","Hypogonadisme":"Gonades & hormones sexuelles","métabolique":"Obésité, nutrition & syndrome métabolique","bariatrique":"Obésité, nutrition & syndrome métabolique","Obésité":"Obésité, nutrition & syndrome métabolique","Croissance":"Croissance & puberté (pédiatrie)","Puberté":"Croissance & puberté (pédiatrie)","hématopoïèse":"Pharmacologie générale (hors endocrinologie)","immunosuppresseurs":"Pharmacologie générale (hors endocrinologie)","hypolipémiants":"Pharmacologie générale (hors endocrinologie)","phosphocalcique":"Phosphocalcique & parathyroïdes","hormones sexuelles":"Gonades & hormones sexuelles","Anapath pancréas":"Diabète & hypoglycémies","Anapath hypophyse":"Hypophyse"}
def redomain(q):
    stem=" ".join(q["stem"]); full=stem+"\n"+"\n".join(q["lines"])
    if q["session"]=="2016-2021":
        for k,v in SEC.items():
            if k in q["section"]: return v
    if q["disc"]=="PEDIA" and CRO.search(stem) and not DIA.search(stem): return "Croissance & puberté (pédiatrie)"
    for n,rx in ORDER_STEM:
        if rx.search(stem): return n
    for n,rx in ORDER_FULL:
        if rx.search(full): return n
    return "Autre / non classable"
