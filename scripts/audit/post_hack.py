import re
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
