# Cours « Diabète » (lot 1 : diagnostic, types, autres types, complications aiguës et chroniques, pied).
# Compléments rédigés « à valider » : h = 3 indices progressifs ; e = explication ; o = une remarque par proposition ;
# p = piège (facultatif) ; status="disputed" + note : requalification prudente (jamais l'inverse).

NR = "Proposition non retranscrite dans la compilation."

# ───────────── Diagnostic ─────────────
_HBA1C_E = ("L'HbA1c reflète la glycémie moyenne des 2 à 3 derniers mois (durée de vie des globules rouges). "
            "Elle est sous-estimée quand les globules rouges sont jeunes (hémolyse, hémorragie, transfusion) et "
            "surestimée en cas de carence en fer ou chez le sujet âgé. Elle s'exprime en % ou en mmol/mol, la glycation "
            "est irréversible, et le diagnostic de diabète est posé à 6,5 % ou plus (ADA 2025).")
_HBA1C_H = ["Pense à la durée de vie des globules rouges.",
            "Des globules rouges plus jeunes ont eu moins de temps pour se glyquer, des globules rouges plus vieux davantage.",
            "Que fait une carence en fer à l'âge moyen des globules rouges circulants ?"]

_HGPO_H = ["L'HGPO sert quand la glycémie à jeun ne suffit pas à conclure.",
           "Elle a aussi des indications en dehors du diabète (freinage d'une hormone, hypoglycémies après le repas).",
           "Si une glycémie à jeun confirme déjà le diabète, que t'apporterait une HGPO ?"]
_HGPO_E = ("Indications de l'HGPO (75 g de glucose) : diabète gestationnel, glycémie à jeun limite (100 à 125 mg/dL) "
           "pour chercher un diabète ou une intolérance, acromégalie (absence de freinage de la GH) et hypoglycémie "
           "réactionnelle (épreuve prolongée). Elle est inutile quand le diagnostic est déjà posé par une glycémie à jeun "
           "de 126 mg/dL ou plus confirmée, et elle n'explore pas une insuffisance hypophysaire.")

_PEPC_H = ["Le peptide C est coupé de la proinsuline en même temps que l'insuline.",
           "Il témoigne donc de la sécrétion propre du pancréas, pas de l'insuline injectée.",
           "Que devient la sécrétion du pancréas quand on injecte beaucoup d'insuline ?"]

EXPL = {
    "ENDO-2022-05-ADULTE-QCM-001": dict(
        h=["Une proposition porte sur la durée reflétée par l'HbA1c.",
           "Cette durée dépend de la vie des globules rouges (environ 120 jours).",
           "Le dernier trimestre compte, pas le dernier semestre."],
        e=_HBA1C_E + " Une glycémie de 140 à 199 mg/dL à la 120e minute de l'HGPO définit l'intolérance au glucose.",
        o=["Vrai : glycémie à jeun normale inférieure à 100 mg/dL.",
           NR,
           "Vrai : 140 à 199 à la 120e minute = intolérance au glucose.",
           "Retenue comme vraie par la compilation : le glucose interstitiel est un peu plus bas et décalé dans le temps (pourcentage non vérifié).",
           "Faux (réponse attendue) : l'HbA1c reflète les 2 à 3 derniers mois, pas 6."]),
    "ENDO-2023-05-ADULTE-QCMM-001": dict(
        h=["Rappelle-toi les seuils : 126 à jeun, 200 à la 2e heure.",
           "Une glycémie entre 100 et 125 à jeun est un prédiabète.",
           "Entre 140 et 199 à la 2e heure, c'est une intolérance au glucose."],
        e="Diabète : glycémie à jeun de 126 mg/dL ou plus, 200 ou plus à la 120e minute de l'HGPO, ou 200 ou plus à n'importe quel moment avec des symptômes (ADA 2025). Une glycémie à jeun de 124 est un prédiabète (glycémie à jeun anormale) ; 180 à la 120e minute est une intolérance au glucose.",
        o=["Permet le diagnostic (126 ou plus, à confirmer).", "Ne permet pas (réponse attendue) : prédiabète.",
           "Permet : 200 ou plus avec des symptômes.", "Permet : 200 ou plus à la 120e minute.",
           "Ne permet pas (réponse attendue) : intolérance au glucose."]),
    "ENDO-2023-05-ADULTE-QCM-002": dict(h=_HGPO_H, e=_HGPO_E,
        o=["Indication.", "Indication : glycémie à jeun limite.", "Pas d'indication (réponse attendue) : 130 à jeun (confirmée) suffit au diagnostic.",
           "Indication (épreuve prolongée).", "Indication : absence de freinage de la GH."]),
    "ENDO-2023-05-ADULTE-QCM-003": dict(h=_HBA1C_H, e=_HBA1C_E,
        o=["Vrai : 2 à 3 mois.", "Faux (réponse attendue) : surestimée en cas de carence en fer.", "Vrai : globules rouges jeunes.",
           "Vrai : 6,5 % ou plus.", "Vrai."]),
    "ENDO-2024-01-ADULTE-QCM-002": dict(
        h=["L'HbA1c mesure l'équilibre moyen, quel que soit le mécanisme.",
           "Un type 1 et un type 2 également déséquilibrés ont la même valeur.",
           "Peut-elle dire de quel type de diabète il s'agit ?"],
        e="L'HbA1c sert au suivi de l'équilibre glycémique (2 à 3 mois), au diagnostic du diabète (6,5 % ou plus) et du prédiabète (5,7 à 6,4 %), et peut compléter une glycémie à jeun limite. Elle ne permet pas de typer un diabète : on utilise pour cela la clinique, les anticorps et le peptide C.",
        o=["Utile : 5,7 à 6,4 %.", "Utile : 6,5 % ou plus.", "Utile.", "Utile : complète une glycémie à jeun limite.",
           "Pas utile (réponse attendue) : elle ne type pas le diabète."]),
    "ENDO-2024-01-ADULTE-QCM-003": dict(h=_HBA1C_H, e=_HBA1C_E,
        o=["Vrai : 2 à 3 mois.", "Faux (réponse attendue) : surestimée.", "Vrai.", "Vrai : % ou mmol/mol."]),
    "ENDO-2024-01-ADULTE-QCM-015": dict(
        h=["Un critère diagnostique est un seuil de glycémie, éventuellement associé à des symptômes.",
           "Une glycémie au hasard de 200 ou plus n'est un critère qu'avec des symptômes.",
           "Les anticorps et la glycosurie servent-ils à poser le diagnostic ?"],
        e="Le diagnostic repose sur la glycémie (à jeun, à la 2e heure de l'HGPO, ou au hasard avec des symptômes) ou l'HbA1c. Chaque proposition prise isolément est insuffisante : les anticorps servent à typer, la polyurie et la glycosurie orientent mais ne suffisent pas, une glycémie de plus de 200 n'est un critère qu'avec des symptômes. D'où « aucune des propositions ».",
        o=["Non : ils servent à typer.", "Non : symptôme seul, sans glycémie.", "Pas seule : il faut des symptômes (ou une confirmation).",
           "Non : la glycosurie n'est pas un critère.", "Oui (réponse attendue)."]),
    "ENDO-2025-01-ADULTE-QCM-002": dict(h=_PEPC_H,
        e="Le peptide C reflète la sécrétion des cellules bêta. Il est éliminé par le rein, élevé dans l'insulinome, indosable dans un type 1 ancien. Les marqueurs auto-immuns du type 1 sont les anticorps anti-GAD, anti-IA2, anti-ZnT8 et anti-insuline : il n'existe pas d'anticorps « anti-peptide C » utilisés pour le diagnostic.",
        o=["Vrai.", "Vrai.", "Vrai : sécrétion endogène élevée.", "Vrai.", "Faux (réponse attendue) : ce marqueur n'existe pas en pratique."]),
    "ENDO-2025-01-ADULTE-QCM-004": dict(h=_HBA1C_H, e=_HBA1C_E,
        o=["Faux : 2 à 3 mois.", "Vrai (réponse attendue).", "Faux comme règle générale : selon l'hémoglobinopathie et la méthode, l'erreur se fait dans un sens ou dans l'autre.",
           "Faux : il faut 6,5 % ou plus.", "Faux : glycation irréversible."]),
    "ENDO-2025-01-ADULTE-QCM-008": dict(
        h=["Chez un patient sans symptôme, une valeur anormale doit être confirmée.",
           "Pour confirmer une glycémie à jeun de 130, quel test est le plus simple ?",
           "L'histoire familiale sur plusieurs générations oriente vers une cause particulière."],
        e="Sans symptôme, une glycémie à jeun de 130 mg/dL se confirme par une seconde glycémie à jeun (ou une HbA1c) : l'HGPO n'est pas nécessaire. L'histoire familiale sur plusieurs générations chez une femme jeune fait évoquer un MODY (recherche génétique) ; doser les anti-GAD est utile pour écarter un diabète auto-immun. Asymptomatique, elle n'a pas de raison d'être en cétose. La transmission maternelle peut faire penser au diabète mitochondrial, mais il manque ici les signes associés (surdité, atteinte neurologique).",
        o=["Faux (réponse attendue) : on répète la glycémie à jeun ; l'HGPO n'est pas nécessaire.",
           "Vrai : histoire familiale, sujet jeune.", "Vrai.", "Vrai : asymptomatique.", "Retenue comme vraie : pas de surdité ni d'autre signe."],
        p="L'HGPO n'est pas le test de confirmation d'une glycémie à jeun anormale."),
    "ENDO-2025-01-RADIO-QCM-060": dict(
        h=["Une glycation qui existe chez tout le monde est physiologique.",
           "Regarde la valeur normale de l'HbA1c.",
           "Elle n'est pas nulle chez le sujet sain."],
        e="La glycation est une réaction non enzymatique entre le glucose et les protéines : elle existe chez tout le monde, proportionnellement à la glycémie. L'HbA1c normale (environ 4 à 5,6 %) n'est donc pas nulle. Elle ne nécessite pas une glycémie supérieure à 130 mg/dL, augmente avec la glycémie, favorise plutôt le stress oxydatif et n'a rien à voir avec le bronzage (mélanine).",
        o=["Vrai (réponse attendue).", "Faux : elle se produit à glycémie normale.", "Faux : elle dépend de la glycémie.",
           "Faux : les produits de glycation favorisent le stress oxydatif.", "Faux : le bronzage vient de la mélanine."]),
    "ENDO-ND-ADULTE-QCMM-804": dict(
        h=["L'HbA1c reflète une moyenne sur plusieurs mois.",
           "Elle sert à juger si un diabète connu est bien ou mal équilibré.",
           "Depuis 2010, elle sert aussi au diagnostic, ce qui rend la question discutable."],
        e="L'HbA1c reflète la glycémie moyenne des 2 à 3 derniers mois et sert à juger l'équilibre d'un diabète. Elle est aussi un critère diagnostique (6,5 % ou plus) : la proposition « suspicion diagnostique » est donc également défendable, alors que la question ne demande que 2 vraies.",
        o=["Défendable : critère diagnostique depuis 2010 (ADA).", "Vrai (réponse attendue).", "Vrai (réponse attendue)."]),
    "ENDO-ND-ADULTE-QCM-820": dict(
        h=["La polyurie vient soit d'un soluté qui entraîne l'eau, soit d'un rein insensible à l'ADH, soit de boissons excessives.",
           "Le calcium et le potassium peuvent bloquer l'action de l'ADH sur le rein, mais dans un seul sens.",
           "Est-ce l'excès ou le manque de calcium qui donne une polyurie ?"],
        e="Polyurie et polydipsie : diabète sucré (diurèse osmotique), diabète insipide central ou néphrogénique, potomanie, hypercalcémie et hypokaliémie (rein insensible à l'ADH). L'hypocalcémie ne donne pas de polyurie.",
        o=["Vrai.", "Vrai.", "Vrai.", "Faux (réponse attendue) : c'est l'hypercalcémie.", "Vrai : diabète insipide néphrogénique acquis."]),
    "ENDO-ND-ADULTE-QCM-843": dict(h=_PEPC_H,
        e="Le peptide C reflète la sécrétion des cellules bêta. Il augmente en cas d'insuffisance rénale (élimination rénale) et d'insulinorésistance (hyperinsulinisme). Après une injection d'insuline chez un non-diabétique, l'insuline mesurée est très élevée mais le peptide C est effondré, car la sécrétion pancréatique est freinée.",
        o=["Vrai.", "Vrai.", "Faux (réponse attendue) : il s'effondre.", "Vrai.", "Proposition incomplète (« indétectable » dans le type 1 ancien)."]),
    "ENDO-ND-ADULTE-QCM-845": dict(h=_HBA1C_H[:1] + ["Elle donne une moyenne, pas les pics ni les creux.", "Que sait-on de l'équilibre d'un patient avec un chiffre moyen sur 3 mois ?"],
        e="L'HbA1c évalue l'équilibre glycémique moyen des 2 à 3 derniers mois. Elle n'explique pas une anémie, ne type pas un diabète, ne compte pas les hypoglycémies (une moyenne peut cacher de grandes variations) et ne mesure pas l'insulinorésistance.",
        o=["Non.", "Non.", "Oui (réponse attendue).", "Non : une moyenne masque les hypoglycémies.", "Non : HOMA ou clamp."]),
    "ENDO-ND-ADULTE-QCM-862": dict(
        h=["Une proposition compare deux prélèvements de sang.",
           "La différence classique est entre le plasma et le sang total, pas entre veine et capillaire.",
           "À jeun, les glycémies veineuse et capillaire sont proches."],
        e="À jeun, la glycémie normale est inférieure à 100 mg/dL. La microangiopathie est due à l'hyperglycémie. 140 à 199 à la 120e minute = intolérance. L'HbA1c est surestimée chez le sujet âgé. La glycémie veineuse n'est pas « 10 à 15 % inférieure » à la capillaire : à jeun, elles sont proches (la capillaire est un peu plus haute après un repas) ; l'écart de 10 à 15 % concerne le sang total et le plasma.",
        o=["Vrai (60 à 100 dans la compilation).", "Vrai.", "Vrai.", "Faux (réponse attendue).", "Vrai."]),
    "ENDO-ND-ADULTE-QCM-882": dict(
        h=["Interprète séparément le temps 0 et le temps 120.",
           "À jeun : 100 à 125 = glycémie à jeun anormale.",
           "À 120 minutes : 140 à 199 = intolérance. Seule la 120e minute compte pour le diagnostic."],
        e="À jeun 124 mg/dL = glycémie à jeun anormale (100 à 125). À 120 minutes 180 mg/dL = intolérance au glucose (140 à 199). Les valeurs intermédiaires (60 et 90 minutes au-delà de 200) ne servent pas au diagnostic. Diagnostic : glycémie à jeun anormale et intolérance au glucose.",
        o=["Non.", "Incomplet : la glycémie à jeun est aussi anormale.", "Incomplet : il y a aussi une intolérance.", "Oui (réponse attendue).", "Non : ni 126 à jeun, ni 200 à 120 minutes."]),
    "ENDO-ND-ADULTE-QCM-883": dict(h=_HGPO_H, e=_HGPO_E,
        o=["Pas indiqué (réponse attendue) : on utilise d'autres tests (hypoglycémie insulinique, voir le cours « Hypophyse »).",
           "Indiqué.", "Indiqué.", "Indiqué.", "Indiqué."]),
    "ENDO-ND-ADULTE-QCM-896": dict(h=_PEPC_H[:2] + ["Dans un type 2 ancien, la sécrétion baisse mais disparaît-elle ?"],
        e="Le peptide C vient de la coupure de la proinsuline, il est éliminé dans les urines, et il est dosable (élevé) en cas de surdosage en sulfamides, qui stimulent la sécrétion. Dans un type 2 ancien, la sécrétion diminue mais reste habituellement dosable : il n'est indosable que dans un type 1 ancien.",
        o=["Faux (réponse attendue) : habituellement encore dosable.", "Vrai : coupure de la proinsuline.", "Vrai.", "Vrai : sécrétion stimulée.", NR]),
    "ENDO-ND-ADULTE-QCM-908": dict(h=_HGPO_H, e=_HGPO_E,
        o=["Indication.", "Indication.", "Indication (glycémie à jeun limite).", "Indication.", "Pas d'indication (réponse attendue) : 150 à jeun suffit, à confirmer par un second dosage."]),
    "ENDO-ND-ADULTE-QCM-909": dict(
        h=["Regarde d'abord le temps 0, puis le temps 120.",
           "Intolérance : glycémie à jeun normale et 140 à 199 à 120 minutes.",
           "Au-delà de 200 à 120 minutes, c'est un diabète."],
        e="Intolérance au glucose : 140 à 199 mg/dL à la 120e minute. 90 puis 180 = intolérance. 90 puis 130 = normal. 90 puis 210 = diabète. 130 à jeun = diabète (à confirmer), quelle que soit la 2e heure.",
        o=["Normal.", "Diabète.", "Intolérance (réponse attendue).", "Diabète.", "Diabète par la glycémie à jeun."]),
    "ENDO-ND-ADULTE-QCMM-910": dict(h=_HBA1C_H[:2] + ["Combien de temps vit un globule rouge, et à partir de quel pourcentage parle-t-on de diabète ?"], e=_HBA1C_E,
        o=["Vrai.", "Faux (réponse attendue) : 2 à 3 mois.", "Faux (réponse attendue) : 6,5 % ou plus.", "Vrai.", "Vrai."]),
}

# ───────────── Types ─────────────
_DT1_E = ("Au diagnostic, le diabète de type 1 touche souvent un sujet de moins de 30 ans, de poids normal ou bas, "
          "qui a maigri récemment, avec un syndrome polyuro-polydipsique, une cétose et des anticorps anti-GAD. "
          "Les complications microangiopathiques sont absentes (elles demandent des années d'hyperglycémie), "
          "la ferritine n'est pas augmentée, et le peptide C est bas mais souvent encore dosable (sécrétion résiduelle).")
_DT1_H = ["Le type 1 se révèle brutalement, peu après le début de l'hyperglycémie.",
          "Les complications chroniques demandent des années pour apparaître.",
          "Au diagnostic, reste-t-il un peu de sécrétion d'insuline ?"]
_DT2_H = ["Le type 2 est insidieux et découvert souvent tard.",
          "Il garde assez d'insuline pour éviter la cétose spontanée.",
          "Il n'a pas de marqueur auto-immun propre."]
_DT2FR_H = ["Le type 2 associe une susceptibilité familiale et un mode de vie.",
            "La nutrition pendant la vie fœtale compte aussi.",
            "Une des propositions ne favorise pas l'insulinorésistance ni l'épuisement des cellules bêta."]
_ANAPATH_DT1_H = ["Dans le type 1, la cible de l'auto-immunité est un seul type de cellule de l'îlot.",
                  "Les cellules alpha et delta survivent : l'îlot garde sa place.",
                  "Avec quel marquage vérifierait-on la présence des cellules bêta ?"]
_ANAPATH_DT1_E = ("Dans le type 1 ancien, l'auto-immunité a détruit les cellules bêta, mais les îlots de Langerhans restent en place, "
                  "formés des cellules alpha, delta et PP. On ne met plus en évidence d'insuline ni de pro-insuline par immunohistochimie. "
                  "L'insulite (infiltrat lymphocytaire) se voit au début, pas des années plus tard. Il n'y a ni fibrose cicatricielle, "
                  "ni dépôt amyloïde (propre au type 2), ni hyperplasie compensatrice.")
_ANAPATH_DT2_E = ("Dans le type 2, le pancréas ne montre pas d'inflammation (pas d'insulite), les cellules bêta diminuent progressivement, "
                  "et on peut voir des dépôts amyloïdes (amyline) dans les îlots, colorés au rouge Congo, avec une biréfringence "
                  "en lumière polarisée. Une biopsie n'est jamais nécessaire au diagnostic d'un diabète.")

EXPL.update({
    "ENDO-2022-05-ADULTE-QCMM-005": dict(h=_DT2_H,
        e="Au diagnostic, un type 2 est souvent asymptomatique ; une rétinopathie peut déjà être présente, car le diabète évoluait depuis des années ; un coma hyperosmolaire peut être révélateur. L'acidocétose est très inhabituelle (il reste de l'insuline) et la ferritine n'est pas diminuée (elle est plutôt augmentée en cas de stéatose et d'insulinorésistance).",
        o=["Présent : découverte fortuite.", "Présent possible.", "Présent possible : révélateur.", "Pas présent (réponse attendue).", "Pas présent (réponse attendue) : plutôt augmentée."]),
    "ENDO-2023-05-ADULTE-QCM-005": dict(h=_DT1_H, e=_DT1_E,
        o=["Caractéristique.", "Caractéristique.", "Pas caractéristique (réponse attendue).", "Caractéristique.", "Caractéristique."]),
    "ENDO-2023-05-ADULTE-QCM-006": dict(
        h=["Le type 1 peut survenir à tout âge.",
           "La plupart des enfants diabétiques de type 1 n'ont aucun parent atteint.",
           "Le risque pour l'enfant de deux parents atteints est-il proche des trois quarts ?"],
        e="Le type 1 peut survenir à tout âge, y compris chez la personne âgée. Une rémission partielle transitoire (« lune de miel ») est possible après le début de l'insuline. L'hyperglycémie apparaît quand environ 80 % des cellules bêta sont détruites. Le risque héréditaire est modeste : quelques pour cent si un parent est atteint, nettement plus si les deux le sont, mais loin de 75 % (ordre de grandeur de 10 à 30 % selon les études, à valider).",
        o=["Vrai.", "Vrai (selon la compilation).", "Vrai.", NR, "Faux (réponse attendue)."]),
    "ENDO-2023-05-ADULTE-QCM-008": dict(h=_DT2FR_H,
        e="Facteurs favorisant le type 2 : hérédité, sédentarité, surpoids, malnutrition ou retard de croissance in utero, antécédent de diabète gestationnel, ovaires polykystiques. L'alcoolisme chronique peut donner une pancréatite chronique et un diabète secondaire, mais n'est pas un facteur prédisposant au type 2.",
        o=["Vrai.", "Vrai.", "Vrai.", "Faux (réponse attendue).", "Vrai : retard de croissance intra-utérin."]),
    "ENDO-2024-01-ADULTE-QCM-006": dict(h=_DT1_H[:2] + ["Quel signe supposerait des années d'hyperglycémie ?"], e=_DT1_E,
        o=["Présent.", "Présent.", "Présent.", "Non présent (réponse attendue)."]),
    "ENDO-2025-01-ADULTE-QCM-006": dict(h=["Le type 2 touche de plus en plus de jeunes.", "Il est fortement lié à l'hérédité et au poids, et peut régresser.", "Le poids actuel suffit-il à écarter un type 2 ?"],
        e="Le type 2 touche aussi des jeunes, il est favorisé par un retard de croissance in utero, une histoire familiale est fréquente, et il peut régresser après une perte de poids importante. Un IMC inférieur à 25 ne l'exclut pas : la graisse abdominale, l'origine ethnique et la génétique jouent aussi.",
        o=["Vrai.", "Vrai.", "Vrai.", "Vrai.", "Faux (réponse attendue)."]),
    "ENDO-2025-01-ANAPATH-QCM-085": dict(h=["Le type 2 n'est pas une maladie auto-immune.", "Les dépôts amyloïdes se colorent au rouge Congo.", "A-t-on besoin d'un prélèvement de pancréas pour diagnostiquer un diabète ?"], e=_ANAPATH_DT2_E,
        o=["Vrai : pas d'insulite.", "Retenue comme vraie : les cellules bêta diminuent fortement avec le temps.", "Vrai : amyline.", "Vrai.", "Faux (réponse attendue)."]),
    "ENDO-2026-01-ANAPATH-QCM-043": dict(h=["Le type 2 n'est pas une maladie auto-immune.", "Les dépôts amyloïdes se colorent au rouge Congo.", "A-t-on besoin d'un prélèvement de pancréas pour diagnostiquer un diabète ?"], e=_ANAPATH_DT2_E,
        o=["Vrai : pas d'insulite.", "Retenue comme vraie : les cellules bêta diminuent fortement avec le temps.", "Vrai : amyline.", "Vrai.", "Faux (réponse attendue)."]),
    "ENDO-ND-ADULTE-QCM-805": dict(h=_DT1_H[2:] + ["Le type 1 s'associe à d'autres maladies auto-immunes.", "Un type 2 très insulinopénique peut-il faire une cétose ?"],
        e="Le type 1 s'associe à d'autres maladies auto-immunes (Addison, thyroïdite) et se caractérise par des anticorps anti-GAD. Un type 2 très insulinopénique peut faire une acidocétose. Le LADA est un diabète auto-immun de l'adulte. Au diagnostic du type 1, le peptide C est bas mais souvent encore dosable : il ne devient indosable qu'après des années.",
        o=["Vrai.", "Faux (réponse attendue) : souvent encore dosable.", "Vrai.", "Vrai.", "Retenue comme vraie : diabète auto-immun de l'adulte (souvent après 30 ou 35 ans)."]),
    "ENDO-ND-ADULTE-QCMM-807": dict(h=_DT2_H,
        e="Au diagnostic, le type 2 touche un adulte souvent de plus de 40 ans, en surpoids, sans cétose spontanée. Le début est insidieux, pas brutal. Les « anticorps anti-adipocytes » n'existent pas comme marqueur : le type 2 n'est pas auto-immun.",
        o=["Non habituel (réponse attendue) : début insidieux.", "Habituel.", "Habituel.", "Habituel.", "Non (réponse attendue) : marqueur inexistant."]),
    "ENDO-ND-ADULTE-QCM-821": dict(h=["Dans le type 2, les hormones digestives qui amplifient la sécrétion d'insuline après un repas perdent de leur efficacité.", "La metformine a un effet connu sur une vitamine.", "Les gliflozines agissent sur le rein : que se passe-t-il quand il filtre peu ?"],
        e="Dans le type 2, l'effet incrétine (l'amplification de la sécrétion d'insuline par le GLP-1 et le GIP après un repas oral) est diminué, et le glucagon est trop élevé : les deux anomalies coexistent, l'une n'augmente pas l'autre. La metformine peut causer un déficit en vitamine B12 ; l'effet des gliflozines sur la glycémie diminue en cas d'insuffisance rénale sévère ; une chirurgie peut nécessiter une insuline transitoire.",
        o=["Vrai : insuline transitoire en cas de chirurgie lourde ou de déséquilibre.", "Vrai.", "Faux (réponse attendue) : l'effet incrétine est diminué.", "Vrai."]),
    "ENDO-ND-ADULTE-QCMM-827": dict(h=["Le type 1 se révèle souvent brutalement après un événement (infection).", "Après le début de l'insuline, les besoins peuvent baisser pendant un temps.", "Les anticorps précèdent le diabète de combien de temps ?"],
        e="Le type 1 se révèle souvent brutalement, à l'occasion d'un événement précipitant (infection). Après le début de l'insuline, une rémission partielle (« lune de miel ») est possible, mais elle est toujours transitoire. Le peptide C est bas mais souvent dosable au diagnostic. Les anticorps anti-GAD apparaissent souvent des mois ou des années avant le diabète. Le diabète de type 1 appartient classiquement au syndrome polyendocrinien auto-immun de type 2 (avec l'Addison et la thyroïdite) ; il est possible mais plus rare dans le type 1 (hypoparathyroïdie, Addison, candidose).",
        o=["Faux : souvent encore dosable.", "Vrai (réponse attendue).", "Retenue comme fausse : l'association classique du diabète de type 1 est le syndrome polyendocrinien de type 2.", "Vrai (réponse attendue).", "Faux : des mois ou des années."]),
    "ENDO-ND-ADULTE-QCM-832": dict(h=["Pour distinguer deux types, il faut un critère qui diffère selon le mécanisme.", "La clinique, l'âge, les anticorps, les complications au diagnostic et la cétose diffèrent.", "Un marqueur d'équilibre moyen dépend-il du type ?"],
        e="Distinguent un type 1 d'un type 2 : l'IMC, les complications déjà présentes au diagnostic (en faveur d'un type 2 ancien méconnu), les anticorps anti-GAD, et la respiration rapide (Kussmaul, signe d'acidocétose, en faveur d'un type 1). L'HbA1c reflète seulement l'équilibre moyen : elle ne type pas le diabète.",
        o=["Ne permet pas (réponse attendue).", "Permet.", "Permet.", "Permet.", "Permet : acidocétose."]),
    "ENDO-ND-ADULTE-QCM-833": dict(h=_DT2FR_H[:2] + ["Une infection virale de l'enfance a-t-elle un lien établi avec le type 2 ?"],
        e="Favorisent le type 2 : syndrome métabolique, retard de croissance intra-utérin, histoire familiale, ovaires polykystiques. Les oreillons ne sont pas un facteur du type 2 (les infections virales sont discutées comme déclencheurs du type 1).",
        o=["Pas un facteur (réponse attendue).", "Facteur.", "Facteur.", "Facteur.", "Facteur : insulinorésistance."]),
    "ENDO-ND-ADULTE-QCM-837": dict(h=["Un type 1 maigrit quand il manque d'insuline, ou quand une autre maladie accélère le catabolisme.", "Pense aux maladies auto-immunes associées.", "Une maladie qui fait plutôt gonfler fait-elle maigrir ?"],
        e="Un diabétique de type 1 maigrit en cas d'insulinopénie (oubli d'insuline), d'hyperthyroïdie ou d'Addison associés, de maladie cœliaque, ou d'amyotrophie diabétique proximale (syndrome de Garland). La néphropathie avec macroprotéinurie donne plutôt des œdèmes (prise de poids) : c'est la réponse retenue, mais un syndrome néphrotique sévère peut s'accompagner d'une fonte musculaire.",
        o=["Réponse retenue (discutée).", "Fait maigrir : amyotrophie proximale.", "Fait maigrir.", "Fait maigrir.", "Fait maigrir : insulinopénie."]),
    "ENDO-ND-ADULTE-QCM-844": dict(h=["Distingue facteur de risque et mécanisme de la maladie.", "La perte des cellules bêta fait partie de l'évolution du type 2, pas des facteurs qui le favorisent.", "Quelle proposition décrit une conséquence plutôt qu'un facteur ?"],
        e="Favorisent le type 2 : retard de croissance intra-utérin, insulinorésistance, surpoids, antécédents familiaux. La diminution progressive des cellules bêta fait partie de l'histoire naturelle de la maladie : la compilation la retient comme la proposition fausse.",
        o=["Facteur.", "Retenue comme fausse (réponse attendue) : évolution de la maladie plutôt que facteur.", "Facteur.", "Facteur.", "Facteur."]),
    "ENDO-ND-ADULTE-QCMM-855": dict(h=_DT1_H[:2] + ["La ferritine est-elle un marqueur du type 1 ?"], e=_DT1_E,
        o=["Caractéristique.", "Pas présent (réponse attendue).", "Pas présent (réponse attendue).", "Caractéristique.", "Caractéristique."]),
    "ENDO-ND-ADULTE-QCM-879": dict(h=["Typer, c'est trouver le mécanisme : auto-immunité, insulinorésistance, sécrétion.", "L'histoire du poids et les autres maladies auto-immunes orientent.", "Lequel de ces examens ne mesure qu'un équilibre moyen ?"],
        e="Pour typer un diabète : anticorps anti-GAD, poids maximal atteint dans la vie, autres maladies auto-immunes, test HOMA (sensibilité et sécrétion), peptide C. L'HbA1c ne type pas le diabète.",
        o=["Permet.", "Permet.", "Permet.", "Ne permet pas (réponse attendue).", "Permet."]),
    "ENDO-ND-ADULTE-QCM-881": dict(h=["Une proposition donne un pourcentage.", "La plupart des diabétiques de type 2 ont un syndrome métabolique.", "40 % est-il un chiffre trop bas ou trop haut ?"],
        e="La grande majorité des diabétiques de type 2 (de l'ordre de 70 à 80 %, selon les définitions) ont un syndrome métabolique : 40 % est trop bas. Un type 2 peut donner une cétose s'il est très insulinopénique. Les anti-GAD signent un diabète auto-immun (type 1 ou LADA). Le test HOMA estime la fonction des cellules bêta et la sensibilité à l'insuline.",
        o=["Faux (réponse attendue) : bien plus.", "Vrai.", "Vrai (diabète auto-immun).", "Vrai.", NR]),
    "ENDO-ND-ADULTE-QCM-898": dict(h=_DT2FR_H[:2] + ["Le type 2 est-il une maladie familiale ?"],
        e="Le type 2 est favorisé par le retard de croissance intra-utérin et la malnutrition fœtale, il s'accompagne souvent d'un syndrome métabolique, et les anticorps anti-GAD et anti-IA2 sont négatifs. L'histoire familiale est fréquente, pas rare.",
        o=["Vrai.", "Vrai.", "Faux (réponse attendue).", "Vrai (s'ils sont positifs, c'est un diabète auto-immun).", "Vrai."]),
    "ENDO-ND-ADULTE-QCM-911": dict(h=_DT1_H, e=_DT1_E,
        o=["Caractéristique.", "Caractéristique.", "Caractéristique.", "Caractéristique.", "Pas caractéristique (réponse attendue) : souvent encore dosable."]),
    "ENDO-ND-ADULTE-QCM-930": dict(h=["Le LADA est un diabète auto-immun.", "La destruction des cellules bêta progresse.", "Quel traitement remplace une sécrétion qui disparaît ?"],
        e="Le LADA est un diabète auto-immun de l'adulte : l'insulinopénie s'installe en quelques mois à années. Le traitement repose sur l'insuline, y compris chez la personne âgée. Les sulfamides épuisent des cellules bêta déjà menacées, et les seules mesures hygiéno-diététiques ne suffisent pas.",
        o=["Oui (réponse attendue).", "Non.", "Insuffisant seul."]),
    "ENDO-ND-ANAPATH-QCM-132": dict(h=_ANAPATH_DT1_H, e=_ANAPATH_DT1_E,
        o=["Non : l'insulite est précoce.", "Oui (réponse attendue).", "Non : les îlots restent.", "Non.", "Non : type 2."]),
    "ENDO-ND-ANAPATH-QCM-135": dict(h=_ANAPATH_DT1_H, e=_ANAPATH_DT1_E,
        o=["Non.", "Non.", "Non : type 2.", "Oui (réponse attendue).", "Non."]),
    "ENDO-ND-ANAPATH-QCM-136": dict(h=_ANAPATH_DT1_H, e=_ANAPATH_DT1_E,
        o=["Non : les îlots restent.", "Non : phase précoce.", "Oui (réponse attendue).", "Non : phase précoce.", "Non."]),
    "ENDO-ND-ANAPATH-QCM-137": dict(h=_ANAPATH_DT1_H, e=_ANAPATH_DT1_E,
        o=["Non.", "Non : les îlots restent.", "Non : type 2.", "Oui (réponse attendue).", "Non."]),
    "ENDO-ND-ANAPATH-QCM-139": dict(h=_ANAPATH_DT1_H, e=_ANAPATH_DT1_E,
        o=["Oui (réponse attendue).", "Non.", "Non : type 2.", "Non."]),
})

# ───────────── Autres types ─────────────
_SEC_H = ["Un diabète secondaire vient d'une destruction du pancréas, d'hormones hyperglycémiantes ou de médicaments.",
          "Les hormones hyperglycémiantes : GH, cortisol, catécholamines, glucagon.",
          "Une des maladies proposées ne produit pas d'hormone hyperglycémiante et n'abîme pas le pancréas."]
_SEC_E = ("Causes de diabète secondaire : maladies du pancréas (pancréatite chronique, pancréatectomie, cancer, mucoviscidose, "
          "hémochromatose), endocrinopathies avec hormones hyperglycémiantes (Cushing, acromégalie, phéochromocytome, glucagonome), "
          "médicaments (corticoïdes, antipsychotiques atypiques, antiprotéases), hépatite C et cirrhose. Ne donnent pas de diabète : "
          "l'hépatite A (aiguë, sans séquelle), l'insuffisance surrénalienne (elle donne plutôt des hypoglycémies), le cancer "
          "médullaire de la thyroïde, l'hyperprolactinémie.")
_IR_H = ["L'insulinorésistance accompagne l'excès de graisse abdominale et les hormones de contre-régulation.",
         "Certains médicaments l'augmentent, d'autres l'améliorent.",
         "Une des propositions désigne une situation sans effet notable, voire favorable, sur la sensibilité à l'insuline."]
_IR_E = ("Causes d'insulinorésistance : obésité abdominale, ovaires polykystiques, stéatose hépatique (NASH), cirrhose, Cushing et "
         "corticoïdes, acromégalie, phéochromocytome, antiprotéases, hémochromatose, lipodystrophies. Ne la donnent pas : les IEC "
         "(plutôt favorables), l'hypothyroïdie, l'infarctus du myocarde (hyperglycémie de stress transitoire).")
_MODY2_H = ["Le MODY 2 touche le capteur de glucose de la cellule bêta.",
            "Le seuil de déclenchement de la sécrétion est simplement réglé plus haut.",
            "L'hyperglycémie est-elle forte et évolutive, ou modérée et stable ?"]
_MODY2_E = ("Le MODY 2 est dû à une mutation de la glucokinase, transmise de façon autosomique dominante (histoire familiale). "
            "L'hyperglycémie à jeun est modérée et stable (souvent 100 à 145 mg/dL), rarement au-delà de 200 ; il n'y a pas de cétose, "
            "et les complications micro et macrovasculaires sont habituellement absentes. Un traitement est rarement nécessaire.")
_GEST_H = ["Le dépistage se fait en deux temps au cours de la grossesse.",
           "Les objectifs sont plus stricts que hors grossesse.",
           "Quel traitement médicamenteux ne traverse pas le placenta ?"]
_GEST_E = ("Diabète gestationnel : glycémie à jeun en début de grossesse (au moins chez les femmes à risque), puis HGPO avec 75 g "
           "entre 24 et 28 semaines (seuils de 92, 180 et 153 mg/dL). Objectifs : moins de 95 mg/dL à jeun, moins de 140 une heure "
           "après le repas. Mesures diététiques d'abord, puis insuline : la metformine n'est pas le traitement de référence. "
           "L'HbA1c n'est pas un bon marqueur pendant la grossesse. Le diabète disparaît le plus souvent après l'accouchement, "
           "mais le risque ultérieur de diabète de type 2 est fortement augmenté.")
_HERED_H = ["Distingue une maladie génétique d'une maladie acquise.",
            "L'alcool est la première cause d'une de ces maladies.",
            "Laquelle n'a pas de gène responsable dans la grande majorité des cas ?"]

EXPL.update({
    "ENDO-2022-05-ADULTE-QCM-003": dict(h=_HERED_H,
        e="Ont un caractère génétique : l'hémochromatose (gène HFE, autosomique récessive), le diabète mitochondrial (transmission maternelle), les MODY (autosomiques dominants), la lipodystrophie familiale de Dunnigan. La pancréatite chronique est le plus souvent alcoolique : elle n'est habituellement pas héréditaire (de rares formes génétiques existent).",
        o=["Héréditaire.", "Héréditaire (maternelle).", "Pas héréditaire (réponse attendue) : le plus souvent alcoolique.", "Héréditaire.", "Héréditaire."]),
    "ENDO-2022-05-ADULTE-QCMM-013": dict(h=_SEC_H, e=_SEC_E,
        o=["Cause : catécholamines.", "Pas une cause (réponse attendue) : plutôt des hypoglycémies.", "Cause : atteinte du pancréas.", "Cause : GH.", "Pas une cause (réponse attendue)."]),
    "ENDO-2022-05-ADULTE-QCM-022": dict(
        h=["L'insulinorésistance sévère donne des signes cutanés, ovariens et lipidiques.",
           "Une stéatose s'accompagne souvent d'une ferritine modifiée dans un sens.",
           "La ferritine monte-t-elle ou baisse-t-elle dans la stéatose métabolique ?"],
        e="Une insulinorésistance sévère donne : ovaires polykystiques (hyperandrogénie), acanthosis nigricans, hypertriglycéridémie, stéatose hépatique. Dans la stéatose métabolique, la ferritine est souvent augmentée, pas diminuée. La compilation retient aussi comme vraie « une augmentation de la sécrétion de GH » ; or la pseudo-acromégalie de l'insulinorésistance sévère se fait avec une GH normale (l'insuline en excès stimule les récepteurs de l'IGF-1), et l'obésité diminue plutôt la sécrétion de GH.",
        o=["Possible.", "Possible.", "Retenue comme vraie par la compilation, mais discutable : la GH n'augmente pas habituellement.", "Faux (réponse attendue) : ferritine plutôt augmentée.", "Possible."],
        status="disputed", note="Réponse retenue (D) exacte, mais la proposition C (« augmentation de sécrétion de GH ») est elle aussi discutable : l'insulinorésistance sévère donne une pseudo-acromégalie avec une GH normale. À valider auprès du cours."),
    "ENDO-2023-05-ADULTE-QCM-007": dict(h=["Une seule de ces maladies est un défaut pur de sécrétion d'insuline.", "Elle touche le capteur de glucose de la cellule bêta.", "Quel diabète monogénique ne s'accompagne d'aucune insulinorésistance ?"],
        e="Le MODY 2 est un défaut de sécrétion pur (glucokinase), sans insulinorésistance. L'hémochromatose (atteinte du foie et du pancréas), l'hépatite (C surtout), le Cushing et l'acromégalie donnent un diabète en partie par insulinorésistance.",
        o=["Insulinorésistance (hépatique) en partie.", "Insulinorésistance.", "Pas d'insulinorésistance (réponse attendue).", "Insulinorésistance.", "Insulinorésistance."]),
    "ENDO-2023-05-ADULTE-QCMM-009": dict(h=_MODY2_H, e=_MODY2_E,
        o=["Faux (réponse attendue).", "Faux (réponse attendue) : complications habituellement absentes.", "Vrai.", "Vrai."]),
    "ENDO-2023-05-ADULTE-QCMM-010": dict(h=_GEST_H, e=_GEST_E,
        o=["Faux (réponse attendue) : 24 à 28 semaines.", "Vrai.", "Vrai.", "Faux (réponse attendue) : insuline."]),
    "ENDO-2024-01-ADULTE-QCM-004": dict(h=_SEC_H[:2] + ["Parmi les hépatites virales, laquelle guérit sans laisser de maladie chronique ?"], e=_SEC_E,
        o=["Cause.", "Cause.", "Cause.", "Cause : insulinorésistance.", "Pas une cause (réponse attendue)."]),
    "ENDO-2024-01-ADULTE-QCM-009": dict(h=_MODY2_H, e=_MODY2_E,
        o=["Faux (réponse attendue) : glycémie modérée.", "Vrai.", "Vrai.", "Vrai.", "Vrai."]),
    "ENDO-2024-01-ADULTE-QCM-010": dict(h=_GEST_H, e=_GEST_E,
        o=["Faux (réponse attendue) : insuline.", "Vrai le plus souvent.", "Vrai : 24 à 28 semaines."]),
    "ENDO-2024-01-ADULTE-QCM-019": dict(h=_SEC_H[:2] + ["Parmi les hépatites virales, laquelle guérit sans laisser de maladie chronique ?"], e=_SEC_E,
        o=["Cause.", "Pas une cause (réponse attendue).", "Cause.", "Cause."]),
    "ENDO-2025-01-ADULTE-QCM-902": dict(h=_IR_H[:2] + ["Un des diabètes cités est monogénique et touche la sécrétion."],
        e="Le MODY 5 (HNF1B) est un défaut de sécrétion avec des kystes rénaux, sans insulinorésistance. L'hémochromatose, les antiprotéases et les glucocorticoïdes donnent un diabète en partie par insulinorésistance.",
        o=["Faux (réponse attendue).", "Vrai.", "Vrai.", "Vrai."]),
    "ENDO-2026-01-ADULTE-QCM-004": dict(h=_GEST_H, e=_GEST_E + " Selon l'ADA, la glycémie de début de grossesse est recommandée chez les femmes à risque (et peut être proposée à toutes) ; plusieurs pays, dont la Belgique, la proposent à toutes.",
        o=["Faux : insuline si nécessaire.", "Faux : cibles plus strictes.", "Faux.", "Vrai (réponse attendue) : dépistage universel.", "Défendable aussi (ADA : dépistage précoce des femmes à risque)."],
        status="disputed", note="La compilation retient D (dépistage pour toutes). La proposition E (dépistage précoce des femmes à risque) correspond aussi aux recommandations de l'ADA : les deux se défendent selon la stratégie de dépistage. À valider auprès du cours."),
    "ENDO-2026-01-ADULTE-QCM-006": dict(h=["Le diabète mitochondrial se transmet par la mère.", "L'hémochromatose surcharge surtout le foie et le pancréas.", "Un médicament injecté localement peut avoir un effet général."],
        e="Le diabète mitochondrial se transmet par la mère (pas autosomique dominant). Un cancer du pancréas peut donner un diabète franc. L'hémochromatose est liée surtout à des mutations du gène HFE (avec une hepcidine insuffisante) et surcharge le foie, le pancréas, l'hypophyse, le cœur et la peau. Une infiltration de corticoïdes (sciatique) passe en partie dans le sang et peut provoquer une hyperglycémie, souvent transitoire : c'est la réponse retenue.",
        o=["Faux : transmission maternelle.", "Faux : un diabète franc est possible.", "Faux : gène HFE surtout, surcharge du foie et du pancréas.", "Vrai (réponse attendue) : plutôt une hyperglycémie transitoire, qui révèle souvent un diabète latent."]),
    "ENDO-ND-ADULTE-QCM-806": dict(h=_SEC_H, e=_SEC_E,
        o=["Peut causer un diabète.", "Peut causer : catécholamines.", "Ne peut pas (réponse attendue)."]),
    "ENDO-ND-ADULTE-QCM-818": dict(h=_IR_H, e=_IR_E,
        o=["Pas une cause (réponse attendue) : plutôt favorables.", "Cause.", "Cause.", "Cause."]),
    "ENDO-ND-ADULTE-QCM-822": dict(h=["Le diabète bronzé de l'hémochromatose a une couleur de peau particulière.", "Elle vient du fer et d'un pigment de la peau.", "Le fer stimule-t-il l'hypophyse à produire de la MSH ?"],
        e="Des diabètes génétiques se transmettent par la mère (mitochondrial). Un cancer du pancréas peut révéler un diabète récent. L'hémochromatose s'accompagne d'hypogonadisme et de cirrhose. Les antiprotéases donnent une insulinorésistance sévère. La mélanodermie de l'hémochromatose vient des dépôts de fer et d'un excès de mélanine dans la peau, pas d'une stimulation de la POMC ou de la MSH (mécanisme de l'Addison).",
        o=["Vrai.", "Vrai.", "Vrai.", "Faux (réponse attendue).", "Vrai."]),
    "ENDO-ND-ADULTE-QCMM-842": dict(h=_SEC_H, e=_SEC_E,
        o=["Pas une cause (réponse attendue).", "Cause.", "Cause.", "Pas une cause (réponse attendue).", "Cause."]),
    "ENDO-ND-ADULTE-QCM-846": dict(h=["Le test HOMA utilise deux dosages simples.", "Ces dosages doivent être faits dans des conditions précises.", "Un repas récent fausse-t-il la glycémie et l'insuline ?"],
        e="L'HbA1c n'est pas fiable en cas d'hémolyse ; des anti-GAD fortement positifs orientent vers un type 1 ; un type 2 très insulinopénique peut faire une cétose ; le LADA est un diabète auto-immun de l'adulte. Le test HOMA se calcule à partir de la glycémie et de l'insuline à jeun : il ne se fait pas chez un patient non à jeun.",
        o=["Vrai.", "Vrai.", "Vrai.", "Retenue comme vraie : diabète auto-immun de l'adulte.", "Faux (réponse attendue) : à jeun."]),
    "ENDO-ND-ADULTE-QCM-861": dict(h=_HERED_H[:1] + ["Une maladie due à un adénome hypophysaire est-elle habituellement transmise ?", "La NEM 1 est une maladie génétique."],
        e="Sont héréditaires : la NEM 1 (autosomique dominante, avec possible acromégalie), le diabète mitochondrial, les MODY et l'hémochromatose. La maladie de Cushing (adénome hypophysaire corticotrope) est habituellement sporadique.",
        o=["Héréditaire.", "Pas héréditaire (réponse attendue).", "Héréditaire.", "Héréditaire.", "Héréditaire."]),
    "ENDO-ND-ADULTE-QCM-870": dict(h=_IR_H[:2] + ["Un stress aigu donne une hyperglycémie transitoire, pas une insulinorésistance sévère durable."],
        e="Les ovaires polykystiques et la NASH s'accompagnent d'insulinorésistance ; l'acanthosis nigricans en est un marqueur (plutôt une conséquence qu'une cause). La pancréatite aiguë peut donner une hyperglycémie transitoire. L'infarctus du myocarde donne une hyperglycémie de stress, mais pas d'insulinorésistance sévère : c'est la réponse retenue.",
        o=["Insulinorésistance.", "Ne la provoque pas (réponse attendue).", "Retenue comme cause par la compilation (hyperglycémie, stress inflammatoire).", "Marqueur d'insulinorésistance.", "Insulinorésistance."]),
    "ENDO-ND-ADULTE-QCM-893": dict(h=_SEC_H, e=_SEC_E,
        o=["Cause.", "Cause.", "Cause.", "Cause.", "Pas une cause (réponse attendue)."]),
    "ENDO-ND-ADULTE-QCM-923": dict(h=_IR_H, e=_IR_E,
        o=["Ne la donne pas (réponse attendue).", "La donne.", "La donne.", "La donne.", "La donne (et détruit les cellules bêta)."]),
})

# ───────────── Complications aiguës ─────────────
_DD_H = ["Pour distinguer deux comas, il faut un signe qui diffère entre eux au moment où on examine le patient.",
         "L'un s'installe en quelques minutes, avec des sueurs ; l'autre en plusieurs heures ou jours, avec une déshydratation.",
         "Ce que le patient prend habituellement comme traitement est-il différent dans les deux cas ?"]
_DD_E = ("Coma hypoglycémique : installation brutale, sueurs profuses, agitation et convulsions possibles, pas de déshydratation. "
         "Coma acidocétosique : installation progressive, peau et muqueuses sèches (déshydratation), respiration de Kussmaul, haleine "
         "acétonique (« pomme de reinette »). La glycémie capillaire tranche immédiatement. Ne permettent pas de les distinguer : la dose "
         "ou le schéma d'insuline, le type de diabète (les deux surviennent chez le diabétique de type 1 sous insuline), la tension artérielle.")
_ACT_H = ["Le traitement repose sur trois piliers : eau et sel, insuline, potassium.",
          "Le liquide de départ doit corriger une déshydratation avec perte de sel.",
          "Un des traitements proposés n'est réservé qu'aux acidoses extrêmes."]
_ACT_E = ("Acidocétose : réhydratation par sérum physiologique (NaCl 0,9 %), insuline IV continue (environ 0,1 U/kg/h), potassium dès que "
          "la kaliémie le permet, glucosé ajouté quand la glycémie descend sous 250 mg/dL, traitement de la cause (antibiotiques IV après "
          "hémocultures). Les bicarbonates ne sont pas donnés d'office : seulement si le pH est inférieur à 7,0 (consensus 2024), "
          "car ils exposent à l'hypokaliémie et à l'acidose paradoxale du LCR.")
_HHS_H = ["Dans l'état hyperosmolaire, il reste assez d'insuline pour bloquer la fabrication des corps cétoniques.",
          "Sans corps cétoniques, quels signes d'acidose manquent ?",
          "La déshydratation est majeure, d'où une insuffisance rénale fonctionnelle."]
_HHS_E = ("État hyperosmolaire : souvent une personne âgée, diabétique de type 2, après une infection ; glycémie très élevée (600 mg/dL ou "
          "plus, souvent au-delà de 800), osmolalité très élevée, déshydratation majeure, insuffisance rénale fonctionnelle (urée "
          "augmentée, plus que la créatinine), hémoconcentration, pseudohyponatrémie. Pas d'acidose (pH normal), pas de cétose importante, "
          "donc pas de respiration de Kussmaul ni d'haleine acétonique.")

EXPL.update({
    "ENDO-2022-05-ADULTE-QCM-002": dict(h=["La cétose précède l'acidose.", "Les corps cétoniques irritent le tube digestif.", "Lequel de ces signes est digestif ?"],
        e="La cétose (sans acidose) se manifeste surtout par des troubles digestifs : nausées, vomissements, douleurs abdominales. La polyurie, la polydipsie et l'amaigrissement traduisent l'hyperglycémie et la carence en insuline, pas spécifiquement la cétose.",
        o=["Oui (réponse attendue).", "Non : hyperglycémie.", "Non : carence en insuline.", NR]),
    "ENDO-2022-05-ADULTE-QCM-900": dict(h=_DD_H, e=_DD_E,
        o=["Ne permet pas (réponse attendue).", "Permet : déshydratation.", "Permet : hypoglycémie.", "Permet : hypoglycémie.", "Permet : hypoglycémie."]),
    "ENDO-2022-05-ADULTE-QCM-014": dict(h=_DD_H, e=_DD_E,
        o=["Permet.", "Permet.", "Ne permet pas (réponse attendue).", "Permet."]),
    "ENDO-2022-05-ADULTE-QCM-015": dict(h=_ACT_H[:2] + ["Le glucosé arrive plus tard dans le traitement : quand ?"], e=_ACT_E,
        o=["Pas recommandé (réponse attendue) : glucosé seulement quand la glycémie passe sous 250.", "Recommandé.", "Recommandé si la kaliémie le permet.", "Recommandé.", "Possible si le phosphore est très bas."]),
    "ENDO-2023-05-ADULTE-QCMM-015": dict(h=_HHS_H, e=_HHS_E,
        o=["Présente.", "Absente (réponse attendue).", "Présente.", "Présente.", "Absente (réponse attendue)."]),
    "ENDO-2023-05-ADULTE-QCMM-016": dict(h=_DD_H, e=_DD_E,
        o=["Ne permet pas (réponse attendue).", "Permet.", "Permet.", "Ne permet pas (réponse attendue).", "Permet."]),
    "ENDO-2023-05-ADULTE-QCM-017": dict(h=_ACT_H, e=_ACT_E,
        o=["Oui.", "Oui, quand la glycémie passe sous 250.", "Oui.", "Oui, selon la kaliémie.", "Pas d'office (réponse attendue) : pH de 7,15."]),
    "ENDO-2025-01-ADULTE-QCM-014": dict(h=_ACT_H, e=_ACT_E,
        o=["Oui.", "Oui, quand la glycémie passe sous 250.", "Oui.", "Oui, selon la kaliémie.", "Faux (réponse attendue) : pH de 7,2."]),
    "ENDO-2025-01-ADULTE-QCM-016": dict(h=["Compare la cétose, l'acidose et l'osmolalité dans les deux tableaux.", "Un des éléments est présent dans les deux, à des degrés divers.", "Les deux sont des crises d'hyperglycémie."],
        e="L'acidocétose et l'état hyperosmolaire se distinguent par la cétose, l'acidose et l'osmolalité (très élevée dans l'état hyperosmolaire). Les troubles de la conscience sont plus fréquents et plus profonds dans l'état hyperosmolaire. La glycémie est élevée dans les deux : même si elle est plus haute dans l'état hyperosmolaire, la compilation retient qu'elle ne permet pas de trancher.",
        o=["Ne permet pas (réponse attendue).", "Permet.", "Permet (formulation de la compilation : c'est l'osmolalité, très élevée dans l'état hyperosmolaire).", "Permet en partie : plus fréquents dans l'état hyperosmolaire.", "Permet."]),
    "ENDO-2025-01-ADULTE-QCM-020": dict(h=_DD_H, e=_DD_E,
        o=["Ne permet pas (réponse attendue).", "Permet : sueurs de l'hypoglycémie.", "Permet.", "Permet."]),
    "ENDO-2026-01-ADULTE-QCM-012": dict(h=_DD_H, e=_DD_E + " L'état hyperosmolaire se reconnaît à une glycémie très élevée sans acidose.",
        o=["Permet.", "Ne permet pas (réponse attendue).", "Permet.", "Permet.", "Permet."]),
    "ENDO-ND-ADULTE-QCM-812": dict(h=_HHS_H, e=_HHS_E + " Le diabète est souvent méconnu au moment de l'état hyperosmolaire, d'où la discussion.",
        o=["Caractéristique.", "Caractéristique.", "Discutable : le diabète est souvent méconnu.", "Pas caractéristique (réponse attendue).", NR]),
    "ENDO-ND-ADULTE-QCM-813": dict(h=_ACT_H, e=_ACT_E + " Le paracétamol traite la fièvre ; les antibiotiques IV traitent la pyélonéphrite.",
        o=["Recommandé.", "Recommandé.", "Possible.", "Pas recommandé (réponse attendue).", "Recommandé."]),
    "ENDO-ND-ADULTE-QCM-829": dict(h=["Une proposition décrit le calcul de l'osmolalité.", "Les principales particules du plasma sont le sodium, le glucose et l'urée.", "Le potassium plasmatique est-il en concentration suffisante pour peser ?"],
        e="L'osmolalité plasmatique se calcule à partir de la natrémie, de la glycémie et de l'urée : 2 × Na + glycémie/18 + urée/6 (en mg/dL). La kaliémie y pèse très peu. Les bicarbonates peuvent donner une acidose paradoxale du LCR ; la metformine en insuffisance rénale sévère favorise l'acidose lactique ; on vaccine les diabétiques contre la grippe et le pneumocoque ; la tigette urinaire (nitroprussiate) ne détecte pas l'acide bêta-hydroxybutyrique.",
        o=["Vrai.", "Vrai.", "Vrai.", "Faux (réponse attendue) : natrémie, pas kaliémie.", "Vrai."]),
    "ENDO-ND-ADULTE-QCMM-841": dict(h=_DD_H, e=_DD_E,
        o=["Inutile (réponse attendue).", "Utile.", "Inutile (réponse attendue).", "Utile.", "Utile."]),
    "ENDO-ND-ADULTE-QCM-848": dict(h=_HHS_H, e=_HHS_E,
        o=["En faveur.", "En faveur.", "En faveur : insuffisance rénale fonctionnelle.", "En faveur.", "Pas en faveur (réponse attendue) : cétose."]),
    "ENDO-ND-ADULTE-QCMM-849": dict(h=_ACT_H, e=_ACT_E,
        o=["Recommandé.", "Pas recommandé (réponse attendue) : sérum physiologique au départ.", "Recommandé.", "Pas recommandé (réponse attendue).", "Recommandé : germe sensible."]),
    "ENDO-ND-ADULTE-QCM-866": dict(h=_ACT_H, e=_ACT_E,
        o=["Pas recommandé (réponse attendue).", "Recommandé.", "Recommandé.", "Recommandé.", "Possible."]),
    "ENDO-ND-ADULTE-QCM-901": dict(h=_HHS_H, e=_HHS_E,
        o=["Vrai.", "Vrai.", "Vrai.", "Faux (réponse attendue).", "Vrai : pseudohyponatrémie."]),
    "ENDO-ND-ADULTE-QCM-902": dict(h=_ACT_H, e=_ACT_E,
        o=["À faire selon la kaliémie.", "À faire.", "À ne pas faire (réponse attendue).", "À faire après hémocultures.", "À faire."]),
    "ENDO-ND-ADULTE-QCM-912": dict(h=_ACT_H, e=_ACT_E,
        o=["Oui.", "Oui, quand la glycémie passe sous 250.", "Oui.", "Oui, selon la kaliémie.", "Pas d'office (réponse attendue)."]),
    "ENDO-ND-ADULTE-QCM-913": dict(h=_DD_H, e=_DD_E,
        o=["Ne permet pas (réponse attendue).", "Permet.", "Permet.", "Permet.", "Permet."]),
    "ENDO-ND-ADULTE-QCM-916": dict(h=_HHS_H, e=_HHS_E,
        o=["Suggestive.", "Pas suggestive (réponse attendue).", "Suggestive.", "Suggestive.", "Suggestive : hémoconcentration."]),
})

# ───────────── Complications chroniques ─────────────
_NA_H = ["La neuropathie autonome touche le cœur, le tube digestif, la vessie, les organes génitaux et la sudation.",
         "Sur le plan tensionnel, elle empêche la tension de se maintenir debout.",
         "Une des propositions décrit l'inverse de ce que fait la neuropathie autonome sur la tension, ou une atteinte qui n'est pas végétative."]
_NA_E = ("Neuropathie autonome du diabétique : tachycardie de repos et perte de la variation de la fréquence cardiaque avec la respiration, "
         "hypotension orthostatique, ischémie myocardique indolore, gastroparésie, diarrhée motrice (souvent nocturne) ou constipation, "
         "dysfonction érectile, vessie neurologique, troubles de la sudation (anhidrose des pieds, hypersudation du haut du corps), "
         "mauvaise perception des hypoglycémies. L'hypertension artérielle n'en est pas un signe.")
_NEPH_H = ["Ce qui aggrave la néphropathie : ce qui augmente la pression dans le glomérule ou abîme directement le rein.",
           "Pense à la tension, à l'albumine qui fuit, au sucre et aux produits toxiques pour le rein.",
           "Une classe de médicaments du diabète protège au contraire le rein."]
_NEPH_E = ("Aggravent la néphropathie diabétique : HTA mal contrôlée, protéinurie, diabète mal équilibré, produits de contraste iodés, "
           "anti-inflammatoires, dyslipidémie. Ne l'aggravent pas : les gliflozines (inhibiteurs de SGLT2), qui la ralentissent ; "
           "l'insuline, même introduite tôt ; boire beaucoup. Traitement : IEC ou sartan en premier en cas d'albuminurie, gliflozine, "
           "tension inférieure à 130/80 mmHg (ADA 2025). Albuminurie anormale à partir de 30 mg/24 h (ou 30 mg/g de créatinine).")
_RETINO_E = ("Rétinopathie diabétique : cause majeure de cécité ; dépistage par un fond d'œil annuel après dilatation (ou photographies) ; "
             "les exsudats cotonneux, les hémorragies en taches et les AMIR signent une forme sévère (mauvais pronostic) ; les néovaisseaux "
             "définissent la forme proliférante, traitée par photocoagulation au laser ; l'œdème maculaire touche la vision centrale et se "
             "traite par anti-VEGF ; la vitrectomie sert à sauver la vision. Elle s'aggrave avec un mauvais équilibre glycémique et l'HTA ; "
             "le sexe ne change pas le risque.")
_RETINO_NOTE = ("La compilation tient le tabac pour un facteur aggravant « bien connu » de la rétinopathie. Les recommandations de l'ADA jugent ce lien "
                "incertain (le tabac aggrave surtout la macroangiopathie et la néphropathie) : la proposition sur le tabac est donc discutable. "
                "À valider auprès du cours.")
_CORO_H = ["La neuropathie autonome rend l'ischémie silencieuse.",
           "Le diabète fait perdre à la femme sa protection relative.",
           "Une proposition décrit le résultat d'un test d'effort : la compilation la juge fausse."]
_CORO_E = ("Coronaropathie du diabétique : souvent silencieuse (infarctus indolore), lésions diffuses, survenue et décès plus précoces, "
           "même fréquence chez les hommes et les femmes, resténoses plus fréquentes après dilatation. La compilation tient pour fausse "
           "l'affirmation « l'épreuve d'effort est souvent faussement négative » ; en pratique, l'épreuve d'effort est souvent peu contributive "
           "chez le diabétique, et on lui préfère volontiers une imagerie de stress.")
_DIAR_H = ["Pense aux médicaments du diabète qui agissent dans l'intestin.",
           "Pense aussi aux maladies associées : auto-immunes, pancréatiques, thyroïdiennes, et à la neuropathie autonome.",
           "Une des propositions est un médicament réputé bien toléré sur le plan digestif, ou une atteinte qui ne touche pas l'intestin."]
_DIAR_E = ("Diarrhée chronique d'un diabétique : metformine (très fréquent), acarbose, analogues du GLP-1, neuropathie autonome (diarrhée motrice, "
           "pullulation bactérienne), maladie cœliaque (associée au type 1), pancréatite chronique (insuffisance exocrine), hyperthyroïdie. "
           "Les inhibiteurs de la DPP-4 et les glinides sont peu pourvoyeurs de diarrhée ; la néphropathie n'en donne pas.")
_PEDIS_H = ["PEDIS est un acronyme de 5 lettres, en anglais.",
            "Chaque lettre décrit la plaie ou le pied : vascularisation, taille, profondeur, infection, sensibilité.",
            "Les résultats du laboratoire de bactériologie en font-ils partie ?"]
_PEDIS_E = ("Classification PEDIS (IWGDF) : Perfusion, Extent (étendue de la plaie), Depth (profondeur), Infection (grades 1 à 4), "
            "Sensation (sensibilité). Elle ne tient compte ni des germes ni de leurs résistances, ni de la douleur, ni de l'impotence "
            "fonctionnelle. L'ostéite est à la fois D3 et I3 ; l'ischémie critique se définit notamment par une TcPO2 inférieure à 30 mmHg.")
_CHARCOT_H = ["Le pied de Charcot survient sur un pied qui a perdu sa sensibilité.",
              "En phase aiguë, il ressemble à une infection : rouge, chaud, gonflé.",
              "Son traitement est mécanique, pas médicamenteux."]
_CHARCOT_E = ("Pied de Charcot (neuro-arthropathie) : il survient seulement chez des patients neuropathes (diabète surtout, mais aussi d'autres neuropathies). "
              "En phase aiguë : pied rouge, chaud, gonflé, peu ou pas douloureux ; c'est une urgence diagnostique et thérapeutique. "
              "Le diagnostic est clinique et radiologique (IRM si la radiographie est normale). Le traitement de référence est la décharge "
              "par botte plâtrée à contact total, pas les anti-inflammatoires ni les corticoïdes. En phase chronique : déformations sévères, "
              "ulcère médio-plantaire.")
_GANG_E = ("Une gangrène d'orteil chez une patiente âgée qui vit seule, avec un diabète déséquilibré et des pouls non perçus (ischémie), "
           "impose l'hospitalisation : bilan artériel (artériographie programmée), revascularisation si possible, traitement de l'infection, "
           "insuline, soins locaux. On ne la renvoie pas chez son médecin traitant, et on n'ampute pas d'emblée.")

EXPL.update({
    "ENDO-2022-05-ADULTE-QCM-007": dict(h=_NA_H[:2] + ["La compilation retient un trouble du transit comme l'intrus."], e=_NA_E,
        o=["Vrai.", "Retenue comme fausse (réponse attendue), mais la constipation est un trouble fréquent de la neuropathie autonome.", "Vrai.", "Vrai.", "Vrai."],
        status="disputed", note="La compilation retient la « constipation opiniâtre » comme la proposition fausse. Or la constipation est l'un des troubles digestifs les plus fréquents de la neuropathie autonome diabétique. À valider auprès du cours."),
    "ENDO-2022-05-ADULTE-QCM-011": dict(h=_CHARCOT_H, e=_CHARCOT_E,
        o=["Vrai : botte plâtrée.", "Faux (réponse attendue) : d'autres neuropathies peuvent en donner.", "Retenue comme vraie (formulation peu claire).", "Vrai.", "Vrai : clinique et radiographie."]),
    "ENDO-2022-05-ADULTE-QCM-012": dict(h=_DIAR_H, e=_DIAR_E,
        o=["Cause.", "Cause.", "Pas une cause (réponse attendue).", "Cause.", "Cause."]),
    "ENDO-2022-05-ADULTE-QCM-020": dict(h=_CORO_H, e=_CORO_E,
        o=["Vrai.", "Retenue comme fausse (réponse attendue).", "Vrai.", "Vrai : survenue plus précoce.", "Vrai."]),
    "ENDO-2023-05-ADULTE-QCM-014": dict(h=_NEPH_H, e=_NEPH_E,
        o=["Aggrave.", "Aggrave.", "N'aggrave pas (réponse attendue) : néphroprotecteur.", "Aggrave.", "Aggrave."]),
    "ENDO-2023-05-ADULTE-QCM-023": dict(h=["Le patient est neuropathe et a un pied rouge.", "Plusieurs diagnostics sont possibles ; un seul impose une prise en charge urgente spécifique chez le neuropathe.", "Lequel, s'il est raté, mène à des déformations définitives ?"],
        e="Chez un diabétique neuropathe qui a un pied rouge, chaud et gonflé, avec peu de syndrome inflammatoire, il faut d'abord penser au pied de Charcot aigu : son retard de traitement (décharge) mène à des déformations définitives. On écarte aussi une infection (dermohypodermite), une thrombose veineuse et une fracture.",
        o=["Oui (réponse attendue).", "À écarter aussi.", "À écarter aussi.", "À écarter aussi.", "À écarter aussi (le Charcot comporte des fractures)."]),
    "ENDO-2023-05-ADULTE-QCM-036": dict(h=_CORO_H[:2] + ["Le diabète efface-t-il la différence entre les sexes ?"], e=_CORO_E,
        o=["Vrai.", "Vrai.", "Faux (réponse attendue) : même fréquence.", "Vrai."]),
    "ENDO-2024-01-ADULTE-QCMM-012": dict(h=_NEPH_H, e=_NEPH_E,
        o=["Vrai.", "Vrai.", "Faux (réponse attendue).", "Faux (réponse attendue) : inférieur à 130/80.", "Vrai."]),
    "ENDO-2024-01-ADULTE-QCM-013": dict(h=_NA_H, e=_NA_E,
        o=["Vrai.", "Vrai.", "Vrai.", "Faux (réponse attendue).", "Vrai."]),
    "ENDO-2024-01-ADULTE-QCM-021": dict(h=_CHARCOT_H, e=_CHARCOT_E,
        o=["Faux (réponse attendue).", "Vrai.", "Vrai.", "Vrai.", "Vrai."]),
    "ENDO-2024-01-ADULTE-QCM-055": dict(h=_CHARCOT_H, e=_CHARCOT_E,
        o=["Vrai.", "Faux (réponse attendue) : décharge par botte plâtrée.", "Vrai.", "Vrai."]),
    "ENDO-2025-01-ADULTE-QCM-023": dict(h=_CHARCOT_H, e=_CHARCOT_E,
        o=["Vrai.", "Vrai.", "Vrai.", "Faux (réponse attendue) : il faut une neuropathie.", "Vrai."]),
    "ENDO-ND-ADULTE-QCM-801": dict(h=_PEDIS_H, e=_PEDIS_E,
        o=["En fait partie.", "En fait partie.", "En fait partie.", "En fait partie.", "N'en fait pas partie (réponse attendue)."]),
    "ENDO-ND-ADULTE-QCMM-802": dict(h=_PEDIS_H, e=_PEDIS_E,
        o=["Pas évalué (réponse attendue).", "Pas évalué (réponse attendue).", "Évaluée.", "Évaluée.", "Évaluée."]),
    "ENDO-ND-ADULTE-QCM-808": dict(h=_NA_H, e=_NA_E,
        o=["Faux (réponse attendue).", "Vrai.", "Vrai.", "Vrai.", "Vrai."]),
    "ENDO-ND-ADULTE-QCM-810": dict(h=_CORO_H, e=_CORO_E,
        o=["Vrai.", "Retenue comme fausse (réponse attendue).", "Vrai.", "Vrai.", "Vrai."]),
    "ENDO-ND-ADULTE-QCM-811": dict(h=_DIAR_H, e=_DIAR_E + " Le lien entre le syndrome de Cushing et la diarrhée n'est pas classique.",
        o=["Cause.", "Pas une cause (réponse attendue).", "Retenue comme cause par la compilation, mais lien peu clair.", "Cause.", "Cause."],
        status="disputed", note="La réponse retenue (néphropathie) est exacte, mais le syndrome de Cushing n'est pas non plus une cause classique de diarrhée : la question comporterait deux intrus. À valider auprès du cours."),
    "ENDO-ND-ADULTE-QCM-853": dict(h=_DIAR_H, e=_DIAR_E + " Les notices des fibrates citent toutefois des troubles digestifs, dont la diarrhée, parmi les effets fréquents.",
        o=["Cause.", "Cause.", "Cause.", "Retenue comme non-cause (réponse attendue), mais les fibrates peuvent donner des troubles digestifs."],
        status="disputed", note="La compilation retient les fibrates comme la proposition fausse. Leurs notices citent pourtant des troubles digestifs (dont la diarrhée) parmi les effets indésirables fréquents. À valider auprès du cours."),
    "ENDO-ND-ADULTE-QCM-859": dict(h=_NEPH_H[:2] + ["Une des propositions décrit au contraire une situation qui protège le rein."], e=_NEPH_E,
        o=["Aggrave.", "Aggrave.", "N'aggrave pas (réponse attendue).", "Aggrave."]),
    "ENDO-ND-ADULTE-QCMM-864": dict(h=["Le dépistage de la rétinopathie se fait dans des conditions précises.", "L'équilibre glycémique influence l'évolution de la rétinopathie.", "Un fond d'œil sans élargir la pupille montre-t-il toute la rétine ?"], e=_RETINO_E,
        o=["Retenue comme vraie par la compilation : lien discuté.", "Vrai.", "Faux (réponse attendue) : après dilatation.", "Vrai.", "Faux (réponse attendue)."],
        status="disputed", note=_RETINO_NOTE),
    "ENDO-ND-ADULTE-QCM-865": dict(h=["Les critères d'hospitalisation sont des signes de gravité générale ou d'ischémie.", "Un sepsis, une ischémie, un déséquilibre important sont graves.", "Une ostéite sans autre signe de gravité peut-elle se traiter en ambulatoire ?"],
        e="Imposent l'hospitalisation d'un ulcère du pied : sepsis et fièvre, ischémie (pouls non perçus), déséquilibre important du diabète, impossibilité de suivre les soins. Une ostéite probable (contact osseux) sans signe de gravité peut, selon la compilation, se prendre en charge en ambulatoire, même si elle est souvent hospitalisée en pratique.",
        o=["Critère.", "Critère.", "Critère.", "Pas un critère à lui seul (réponse attendue)."]),
    "ENDO-ND-ADULTE-QCM-867": dict(h=_DIAR_H, e=_DIAR_E,
        o=["Cause.", "Cause.", "Pas une cause (réponse attendue).", "Cause.", "Cause."]),
    "ENDO-ND-ADULTE-QCM-868": dict(h=_CORO_H, e=_CORO_E,
        o=["Vrai.", "Vrai.", "Retenue comme fausse (réponse attendue).", "Vrai."]),
    "ENDO-ND-ADULTE-QCMM-884": dict(h=_NEPH_H[:2] + ["L'insuline corrige l'hyperglycémie, qui est ce qui abîme le rein."], e=_NEPH_E + " Le furosémide n'aggrave pas la néphropathie en lui-même (attention seulement à la déshydratation).",
        o=["N'aggrave pas (réponse attendue).", "N'aggrave pas (réponse attendue).", "Aggrave.", "Aggrave.", "Aggrave."]),
    "ENDO-ND-ADULTE-QCMM-885": dict(h=["Distingue la micro et la macroangiopathie : laquelle dépend surtout du sucre ?", "Dans la neuropathie autonome, le nerf vague est atteint tôt.", "Le syndrome de Garland est une atteinte des muscles de la cuisse."],
        e="L'hyperglycémie est la cause majeure de la microangiopathie, pas de la macroangiopathie (qui dépend de tous les facteurs de risque). Dans la neuropathie autonome, l'atteinte parasympathique (vague) précède l'orthosympathique, d'où la tachycardie de repos. La pyélonéphrite emphysémateuse est une infection grave propre au diabétique. Le syndrome de Garland est une amyotrophie proximale douloureuse (neuropathie motrice), pas une neuropathie autonome : la proposition qui le dit autonome est elle aussi inexacte.",
        o=["Vrai.", "Faux (réponse attendue).", "Retenue comme vraie par la compilation, mais inexacte : ce n'est pas une neuropathie autonome.", "Vrai.", "Faux (réponse attendue) : la parasympathique d'abord."],
        status="disputed", note="Les deux réponses retenues (B et E) sont fausses, mais la proposition C l'est aussi : le syndrome de Garland est une amyotrophie proximale (neuropathie motrice douloureuse), pas une neuropathie autonome. À valider auprès du cours."),
    "ENDO-ND-ADULTE-QCM-888": dict(h=["Gangrène humide et infection chez une personne âgée qui vit seule.", "La gravité est locale et générale.", "Peut-on la renvoyer à domicile ?"], e=_GANG_E,
        o=["Oui (réponse attendue).", "Non.", "Insuffisant : il faut hospitaliser.", "Non : pas d'amputation d'emblée.", "Pas en urgence : elle se programme pendant l'hospitalisation."]),
    "ENDO-ND-ADULTE-QCM-899": dict(h=["Une proposition porte sur la différence entre hommes et femmes.", "Le risque de rétinopathie dépend de l'ancienneté et de l'équilibre du diabète.", "Le sexe a-t-il une influence notable ?"], e=_RETINO_E,
        o=["Retenue comme vraie par la compilation : lien discuté.", "Faux (réponse attendue).", "Vrai : précise l'ischémie et les néovaisseaux.", "Vrai.", "Vrai."],
        status="disputed", note=_RETINO_NOTE),
    "ENDO-ND-ADULTE-QCM-903": dict(h=_NA_H, e=_NA_E,
        o=["Pas une neuropathie autonome (réponse attendue).", "Neuropathie autonome.", "Neuropathie autonome.", "Neuropathie autonome.", "Neuropathie autonome."]),
    "ENDO-ND-ADULTE-QCM-914": dict(h=_NA_H[:2] + ["Une des propositions est une atteinte ostéo-articulaire liée surtout à la perte de sensibilité."], e=_NA_E + " Le pied de Charcot est lié surtout à la neuropathie sensitive.",
        o=["Ne suggère pas (réponse attendue).", "Suggère.", "Suggère.", "Suggère.", "Suggère."]),
    "ENDO-ND-ADULTE-QCM-920": dict(h=_PEDIS_H[:2] + ["La douleur fait-elle partie des 5 lettres ?"], e=_PEDIS_E,
        o=["Vrai.", "Vrai.", "Faux (réponse attendue) : D = profondeur (depth).", "Vrai.", "Vrai."]),
    "ENDO-ND-ADULTE-QCM-927": dict(h=["Gangrène d'orteil et pouls non perçus : il y a une ischémie.", "La patiente est âgée, vit seule, avec un diabète négligé.", "Peut-elle rentrer chez elle ?"], e=_GANG_E,
        o=["Oui (réponse attendue).", "Insuffisant.", "Pas en urgence : elle se programme pendant l'hospitalisation.", "Non.", "Non."]),
    "ENDO-ND-ADULTE-QCM-928": dict(h=_NEPH_H[:2] + ["Une des propositions décrit un traitement qui corrige ce qui abîme le rein."], e=_NEPH_E,
        o=["Aggrave.", "Aggrave.", "N'aggrave pas (réponse attendue).", "Aggrave.", "Aggrave."]),
})
