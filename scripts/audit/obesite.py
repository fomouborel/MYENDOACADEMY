# Classement manuel des questions « Obésité, nutrition & syndrome métabolique » de l'audit (Thissen, Hermans, Navez, sessions récentes).
IN = "Question incomplète"; DIS = "Réponse discutée ou contestée"; PROP = "Réponse proposée dans la compilation"

FAM = {
    "OBES-DEF": ("definitions", ["obes-definitions"], "Définitions : IMC, tour de taille"),
    "OBES-GENET": ("definitions", ["obes-definitions"], "Causes de l'obésité : génétique"),
    "OBES-ENERGIE": ("definitions", ["obes-definitions", "obes-traitement"], "Dépense énergétique, nutrition, idées reçues"),
    "POIDS-ENDO": ("poids-endocrino", ["obes-poids-endocrino"], "Variations de poids d'origine endocrinienne"),
    "MEDIC-POIDS": ("traitement", ["obes-traitement"], "Médicaments du diabète et poids"),
    "NUTRITION": ("traitement", ["obes-traitement"], "Nutrition : index et charge glycémiques"),
    "TRT-SEUILS": ("traitement", ["obes-traitement"], "Seuils de prise en charge de l'excès de poids"),
    "BARIA-INDIC": ("traitement", ["obes-traitement"], "Chirurgie bariatrique : indications"),
    "BARIA-COMPL": ("traitement", ["obes-traitement"], "Chirurgie bariatrique : complications"),
    "SM-DEF": ("syndrome-metabolique", ["obes-metabolique"], "Syndrome métabolique : définition et associations"),
    "SM-CORONAIRE": ("syndrome-metabolique", ["obes-metabolique"], "Syndrome métabolique et maladie coronarienne"),
    "SM-TRT": ("syndrome-metabolique", ["obes-metabolique", "obes-traitement"], "Syndrome métabolique : traitement"),
}

H = {
    ("A", 113): ("OBES-DEF", None, "Seul le thème est retranscrit."),
    ("A", 137): ("POIDS-ENDO", None, ""),
    ("A", 398): ("MEDIC-POIDS", None, "Deux propositions seulement (pharmacologie, Horsmans)."),
    ("A", 575): ("MEDIC-POIDS", None, ""),
    ("A", 614): ("OBES-DEF", None, "Seuil de la définition américaine (NCEP-ATP III) ; les recommandations européennes retiennent 80 cm."),
    ("A", 622): ("OBES-GENET", PROP, "Doute du transcripteur sur la proposition D (« pas sûre »), pas sur la réponse."),
    ("A", 1067): ("OBES-DEF", None, "Seuil de la définition américaine (NCEP-ATP III) ; les recommandations européennes retiennent 80 cm."),
    ("A", 1073): ("OBES-GENET", None, ""),
    ("A", 2848): ("SM-DEF", None, "Hermans."),
    ("A", 2854): ("SM-CORONAIRE", DIS, "Hermans. Formulation ambiguë de la proposition retenue (« épreuve de cycloergomètre asymptomatique ») : l'ischémie est souvent silencieuse, mais l'épreuve d'effort peut la révéler."),
    ("A", 2860): ("SM-DEF", None, "Hermans. Consigne incertaine (« une vraie » ou « une fausse ? »)."),
    ("A", 2867): ("SM-TRT", DIS, "Hermans. Consigne au singulier, deux réponses marquées (fibrate et biguanide). La metformine (biguanide) est pourtant le traitement de première intention du diabète de type 2 en l'absence d'insuffisance rénale : réponse discutable."),
    ("A", 2874): ("SM-DEF", PROP, "Hermans. 5e proposition non retranscrite (« ? ») ; la réponse marquée est sans ambiguïté."),
    ("A", 2880): ("SM-DEF", None, "Hermans."),
    ("A", 2888): ("BARIA-COMPL", None, "Navez."),
    ("A", 2894): ("BARIA-INDIC", DIS, "Navez. Réponse conforme aux critères de 1991 (IMC ≥ 40, ou ≥ 35 avec complications). Depuis 2022 (ASMBS et IFSO), la chirurgie est recommandée dès un IMC ≥ 35, même sans complication : « IMC plus de 35 » serait aussi exacte."),
    ("A", 2900): ("BARIA-COMPL", None, "Navez."),
    ("A", 2907): ("MEDIC-POIDS", None, "Thissen."),
    ("A", 2913): ("MEDIC-POIDS", None, "Thissen. La question suivante (« la plupart des obésités sont… ») était collée aux propositions dans la retranscription."),
    ("A", 2925): ("OBES-DEF", None, "Thissen. Seuil de la définition américaine (NCEP-ATP III) ; les recommandations européennes retiennent 80 cm."),
    ("A", 2931): ("OBES-ENERGIE", None, "Thissen."),
    ("A", 2937): ("POIDS-ENDO", DIS, "Thissen. Consigne au singulier (« laquelle ») mais deux réponses marquées, toutes deux exactes : l'insulinome et le Cushing font prendre du poids."),
    ("A", 2942): ("POIDS-ENDO", None, "Thissen."),
    ("A", 2948): ("OBES-ENERGIE", None, "Thissen."),
    ("A", 2955): ("POIDS-ENDO", None, "Thissen."),
    ("A", 2961): ("NUTRITION", None, "Thissen. La charge glycémique se calcule : 200 g × 50 % × 0,75 + 200 g × 10 % × 0,50 = 75 + 10 = 85 g, et non 95 g."),
    ("A", 2969): ("OBES-ENERGIE", None, "Thissen."),
    ("E", 489): ("TRT-SEUILS", None, "Énoncé abrégé (« pour excès de poids ») : vraisemblablement les seuils de prise en charge médicamenteuse. La question suivante (radiologie du phéochromocytome) était collée aux propositions."),
}

_PEDIA = "Pédiatrie : réservée au cours d'endocrinologie pédiatrique (décision du 11/11/2026, docs/DECISIONS.md)."
EXCLUDE = {("A", 318): _PEDIA, ("A", 804): _PEDIA, ("A", 1286): _PEDIA, ("A", 1348): _PEDIA, ("E", 306): _PEDIA}
