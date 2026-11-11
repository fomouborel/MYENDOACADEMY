# Classement manuel des questions « Pharmacologie générale (hors endocrinologie) » de l'audit (cours de Horsmans).
# Les questions de pharmacologie sur les médicaments hormonaux restent dans leur cours d'organe.
IN = "Question incomplète"; DIS = "Réponse discutée ou contestée"; PROP = "Réponse proposée dans la compilation"

FAM = {
    "BIODISPO": ("cinetique", ["pharm-cinetique"], "Biodisponibilité"),
    "CYP2C8": ("cinetique", ["pharm-cinetique"], "Cytochromes : inhibiteurs du CYP2C8"),
    "FER": ("hematopoiese", ["pharm-hematopoiese"], "Fer : besoins quotidiens"),
    "B12-ABS": ("hematopoiese", ["pharm-hematopoiese"], "Vitamine B12 : absorption"),
    "B12-BESOIN": ("hematopoiese", ["pharm-hematopoiese"], "Vitamine B12 : besoins quotidiens"),
    "FOLATE": ("hematopoiese", ["pharm-hematopoiese"], "Folates : absorption"),
    "CYCLO-INTER": ("immunosuppresseurs", ["pharm-immunosuppresseurs", "pharm-cinetique"], "Ciclosporine : interactions"),
    "CYCLO-PK": ("immunosuppresseurs", ["pharm-immunosuppresseurs", "pharm-cinetique"], "Ciclosporine : pharmacocinétique"),
    "SIROLIMUS": ("immunosuppresseurs", ["pharm-immunosuppresseurs", "pharm-cinetique"], "Sirolimus : pharmacocinétique"),
    "AZA-ALLO": ("immunosuppresseurs", ["pharm-immunosuppresseurs"], "Azathioprine et allopurinol"),
    "AZA-TPMT": ("immunosuppresseurs", ["pharm-immunosuppresseurs"], "Azathioprine : métabolisme"),
    "STATINES": ("hypolipemiants", ["pharm-hypolipemiants"], "Statines et ézétimibe"),
}

_CYCLO = ("CYCLO-INTER", DIS, "« Tuyau » de Horsmans : la réponse retenue est l'ézétimibe (Ezetrol), qui n'agit pas sur le CYP3A4. Mais la notice de l'ézétimibe signale une interaction avec la ciclosporine (exposition des deux médicaments augmentée, taux de ciclosporine à surveiller) : « n'interagit pas » n'est pas exact au sens strict.")
_SIRO = ("SIROLIMUS", DIS, "« Tuyau » de Horsmans : la réponse retenue est « absorption intestinale lente » (le sirolimus est absorbé rapidement). Mais « élimination rénale » est aussi inexacte : environ 2 % seulement de la dose est éliminée dans les urines, l'élimination est surtout fécale.")
_AZA = ("AZA-ALLO", None, "Pharmacologie (Horsmans), « tuyau ».")

H = {
    ("A", 347): ("B12-BESOIN", DIS, "Réponse retenue : 1 µg par jour. Les apports recommandés actuels sont plus élevés (4 µg par jour pour l'adulte selon l'EFSA, 2015) ; 1 µg correspond à un ordre de grandeur ancien du besoin minimal."),
    ("A", 353): ("FOLATE", None, "Numéro de question collé à l'énoncé dans la retranscription (« 85Le folate »)."),
    ("A", 373): _CYCLO,
    ("A", 404): ("STATINES", None, "Seul le mot « ezetrol » est retranscrit."),
    ("A", 945): _AZA,
    ("A", 958): ("B12-ABS", None, "Pharmacologie (Horsmans)."),
    ("A", 982): _SIRO,
    ("A", 996): _CYCLO,
    ("A", 1003): ("AZA-TPMT", None, "Pharmacologie (Horsmans)."),
    ("A", 1009): ("BIODISPO", None, "Les lignes suivantes de la retranscription (« Horsman 100 % tuyaux… ») sont des commentaires sur l'examen, pas des propositions."),
    ("A", 1395): ("CYP2C8", None, "« Nouvelle question » en mai 2022."),
    ("A", 4007): ("FER", None, "Pharmacologie (Horsmans)."),
    ("A", 4013): ("B12-ABS", None, "Pharmacologie (Horsmans)."),
    ("A", 4019): ("FOLATE", None, "Pharmacologie (Horsmans)."),
    ("A", 4027): ("STATINES", None, "Pharmacologie (Horsmans)."),
    ("A", 4034): _CYCLO,
    ("A", 4040): ("CYCLO-PK", DIS, "Réponse retenue : « first-pass hépatique important » serait faux. Or la ciclosporine subit un effet de premier passage notable (intestinal et hépatique, CYP3A4 et glycoprotéine P), et son élimination est surtout biliaire (3 à 6 % seulement dans les urines) : « élimination rénale » est au moins aussi inexacte."),
    ("A", 4046): _AZA,
    ("A", 4052): _SIRO,
    ("E", 462): _CYCLO,
    ("E", 476): _AZA,
    ("G", 424): ("FER", None, "Pharmacologie (Horsmans), « tuyau »."),
    ("G", 474): ("BIODISPO", None, "Pharmacologie (Horsmans), « tuyau »."),
    ("G", 499): _AZA,
}
EXCLUDE = {}
