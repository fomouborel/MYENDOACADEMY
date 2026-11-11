# Cours « Pharmacologie générale » : compléments rédigés « à valider » pour les questions importées (cours de Horsmans).
# h = 3 indices progressifs ; e = explication ; o = une remarque par proposition (dans l'ordre) ; p = piège (facultatif).

_BIO_H = ["La biodisponibilité est la fraction de la dose qui atteint la circulation générale.",
          "Par voie intraveineuse, le médicament est injecté directement dans le sang.",
          "Y a-t-il une absorption ou un premier passage à franchir ?"]
_BIO_E = "La biodisponibilité est la fraction de la dose qui atteint la circulation générale sous forme active. Par voie intraveineuse, le médicament est injecté directement dans le sang : sans absorption ni premier passage, la biodisponibilité est par définition de 100 %. Par voie orale, elle est souvent plus faible."
_BIO_O = ["Non.", "Non.", "Non.", "Oui (réponse attendue).", "Non."]

_AZA_H = ["L'allopurinol bloque une enzyme qui dégrade les purines.",
          "L'azathioprine est transformée en 6-mercaptopurine, dégradée en partie par cette même enzyme.",
          "Si le médicament actif s'accumule, quel organe à renouvellement rapide en souffre ?"]
_AZA_E = "L'allopurinol inhibe la xanthine oxydase, qui dégrade la 6-mercaptopurine issue de l'azathioprine. Le médicament actif s'accumule et provoque une toxicité médullaire : aplasie, parfois mortelle. On évite l'association ou on réduit très fortement la dose d'azathioprine. L'allopurinol traite au contraire l'hyperuricémie."
_AZA_O = ["Non : l'allopurinol la traite.",
          "Non.",
          "Oui (réponse attendue).",
          "Non.",
          "Non : c'est un effet du cyclophosphamide."]

_B12_H = ["La vitamine B12 a besoin du facteur intrinsèque, sécrété par l'estomac.",
          "Le complexe vitamine-facteur est absorbé plus loin, dans l'intestin grêle.",
          "Pense à la partie terminale de l'intestin grêle."]
_B12_E = "La vitamine B12 se lie au facteur intrinsèque, sécrété par l'estomac ; le complexe est absorbé dans l'iléon terminal. C'est pourquoi une gastrectomie (plus de facteur intrinsèque) ou une maladie ou une résection de l'iléon (maladie de Crohn) donnent une carence. Le fer est absorbé dans le duodénum, les folates dans le jéjunum."

_FOL_H = ["Chaque nutriment de l'hématopoïèse est absorbé à un endroit précis de l'intestin grêle.",
          "La vitamine B12 est absorbée tout au bout, dans l'iléon.",
          "Les folates, eux, sont absorbés dans la partie proximale du grêle."]
_FOL_E = "Les folates sont absorbés dans le jéjunum (intestin grêle proximal). Une malabsorption du grêle, l'alcoolisme ou certains médicaments (méthotrexate, antiépileptiques) favorisent leur carence. La vitamine B12 est absorbée dans l'iléon terminal, avec le facteur intrinsèque ; l'estomac et le côlon n'absorbent pas les folates."
_FOL_O = ["Oui (réponse attendue).", "Non.", "Non : c'est la vitamine B12.", "Non.", "Non."]

_FER_H = ["La question porte sur le fer qu'il faut ABSORBER chaque jour, pas sur l'apport alimentaire.",
          "On perd environ 1 mg de fer par jour, davantage chez la femme réglée.",
          "Il faut compenser les pertes, règles comprises."]
_FER_E = "On perd environ 1 mg de fer par jour (desquamation, sueur, urines), davantage chez la femme réglée. Pour rester à l'équilibre, il faut absorber environ 1 mg par jour chez l'homme et 1,5 mg chez la femme réglée : c'est la réponse retenue. Comme on n'absorbe qu'une petite partie du fer alimentaire, les apports recommandés sont bien plus élevés (environ 11 mg par jour chez l'homme et 16 mg chez la femme non ménopausée selon l'EFSA)."

_CYCLO_H = ["La ciclosporine est métabolisée par le CYP3A4.",
            "Cherche les inhibiteurs (taux augmentés) et les inducteurs (taux diminués) du CYP3A4.",
            "Cette question a une correction discutée : lis l'explication après avoir répondu."]
_CYCLO_E = "Correction discutée. La ciclosporine est métabolisée par le CYP3A4 : le jus de pamplemousse et la cimétidine (inhibiteurs) augmentent ses taux ; la rifampicine et les antiépileptiques inducteurs les diminuent ; l'amlodipine passe aussi par le CYP3A4. La réponse retenue, l'ézétimibe (Ezetrol), est le seul médicament proposé qui n'agit pas sur le CYP3A4. Mais la notice de l'ézétimibe signale une interaction avec la ciclosporine : l'exposition des deux médicaments augmente et il faut surveiller les taux de ciclosporine. « N'interagit pas » n'est donc pas exact au sens strict."

_SIRO_H = ["Le sirolimus, comme la ciclosporine, passe par le CYP3A4.",
           "Sa biodisponibilité est faible à cause d'un important premier passage.",
           "Cette question a une correction discutée : lis l'explication après avoir répondu."]
_SIRO_E = "Correction discutée. Le sirolimus subit un important effet de premier passage (biodisponibilité d'environ 14 %), il est métabolisé par le CYP3A4 et éliminé surtout par voie hépatique et fécale (91 % dans les selles). Il est absorbé rapidement (pic en 1 à 2 heures) : « absorption intestinale lente » est faux, c'est la réponse retenue. Mais « élimination rénale » est aussi inexacte : 2,2 % seulement de la dose passent dans les urines."

EXPL = {
    # ═════════════ Pharmacocinétique ═════════════
    "ENDO-2023-05-PHARMA-QCM-100": dict(h=_BIO_H, e=_BIO_E, o=_BIO_O),
    "ENDO-2026-01-PHARMA-QCM-051": dict(h=_BIO_H, e=_BIO_E, o=_BIO_O),
    "ENDO-2022-05-PHARMA-QCM-901": dict(
        h=["Distingue les médicaments qui inhibent les cytochromes de ceux qui les induisent.",
           "Un antiépileptique ancien est connu pour accélérer le métabolisme de nombreux médicaments.",
           "Le cotrimoxazole contient du triméthoprime."],
        e="La carbamazépine n'est pas un inhibiteur du CYP2C8 : c'est un inducteur enzymatique puissant. Le triméthoprime (et donc le cotrimoxazole, qui en contient), le déférasirox et le clopidogrel (par son métabolite glucuronide) inhibent le CYP2C8.",
        o=["Pas un inhibiteur (réponse attendue) : c'est un inducteur.",
           "Inhibiteur.",
           "Inhibiteur : contient du triméthoprime.",
           "Inhibiteur.",
           "Inhibiteur : par son métabolite glucuronide."]),

    # ═════════════ Fer, B12, folates ═════════════
    "ENDO-2023-05-PHARMA-QCM-090": dict(h=_B12_H, e=_B12_E,
        o=["Non : les folates.", "Oui (réponse attendue).", "Non.", "Non : l'estomac sécrète le facteur intrinsèque, il n'absorbe pas la vitamine.", "Non : même raison."]),
    "ENDO-ND-PHARMA-QCM-012": dict(h=_B12_H, e=_B12_E,
        o=["Non : les folates.", "Oui (réponse attendue).", "Non.", "Non : l'estomac sécrète le facteur intrinsèque, il n'absorbe pas la vitamine.", "Non : même raison."]),
    "ENDO-2024-01-ADULTE-QCM-902": dict(h=_FOL_H, e=_FOL_E, o=_FOL_O),
    "ENDO-ND-PHARMA-QCM-013": dict(h=_FOL_H, e=_FOL_E, o=_FOL_O),
    "ENDO-2026-01-PHARMA-QCM-045": dict(h=_FER_H, e=_FER_E,
        o=["Non : trop peu.", "Besoin de l'homme ; la réponse retenue est 1,5 mg.", "Oui (réponse attendue).", "Non : trop.", "Non : trop."]),
    "ENDO-ND-PHARMA-QCM-011": dict(h=_FER_H, e=_FER_E,
        o=["Non : trop peu.", "Non : trop peu.", "Oui (réponse attendue).", "Non : trop.", "Non : trop."]),
    "ENDO-2024-01-PHARMA-QCM-084": dict(
        h=["La question porte sur la dose quotidienne de vitamine B12.",
           "Les besoins se comptent en microgrammes.",
           "Cette question a une correction discutée : lis l'explication après avoir répondu."],
        e="Correction discutée. La compilation retient 1 µg par jour, ordre de grandeur ancien du besoin minimal, probablement celui du cours. Les apports recommandés actuels chez l'adulte sont plus élevés : 4 µg par jour selon l'EFSA (2015). Les réserves du foie couvrent plusieurs années, ce qui explique qu'une carence d'apport soit lente à apparaître.",
        o=["Non : trop peu.",
           "Non : trop peu.",
           "Réponse retenue (ordre de grandeur ancien du besoin minimal).",
           "Plus proche des apports recommandés actuels (4 µg selon l'EFSA).",
           "Non : au-delà des apports recommandés."]),

    # ═════════════ Immunosuppresseurs ═════════════
    "ENDO-2023-05-PHARMA-QCM-088": dict(h=_AZA_H, e=_AZA_E, o=_AZA_O),
    "ENDO-2025-01-PHARMA-QCM-100": dict(h=_AZA_H, e=_AZA_E, o=_AZA_O),
    "ENDO-2026-01-PHARMA-QCM-055": dict(h=_AZA_H, e=_AZA_E, o=_AZA_O),
    "ENDO-ND-PHARMA-QCM-033": dict(h=_AZA_H, e=_AZA_E, o=_AZA_O),
    "ENDO-2023-05-PHARMA-QCM-099": dict(
        h=["L'azathioprine est un analogue des purines.",
           "Elle n'est pas un substrat classique des cytochromes P450.",
           "Une enzyme au déficit génétique connu expose à une aplasie sous ce traitement."],
        e="L'azathioprine est transformée en 6-mercaptopurine, dégradée par la thiopurine méthyltransférase (TPMT) et par la xanthine oxydase. Un déficit génétique en TPMT expose à une aplasie à dose normale : on peut mesurer son activité avant de traiter. Les cytochromes P450 et la glycoprotéine P (et non une « glycopeptide P ») ne sont pas les voies principales.",
        o=["Non.", "Non.", "Non.", "Non : ce n'est pas une enzyme de métabolisme.", "Oui (réponse attendue)."]),
    "ENDO-2023-05-PHARMA-QCM-097": dict(h=_CYCLO_H, e=_CYCLO_E,
        o=["Interagit : inhibe le CYP3A4.", "Interagit : induit le CYP3A4.", "Interagit (antiépileptiques inducteurs).", "Réponse retenue, discutable : interaction décrite dans la notice.", "Interagit : substrat du CYP3A4."]),
    "ENDO-2024-01-PHARMA-QCM-088": dict(h=_CYCLO_H, e=_CYCLO_E,
        o=["Interagit : inhibe le CYP3A4.", "Interagit : induit le CYP3A4.", "Interagit (antiépileptiques inducteurs).", "Réponse retenue, discutable : interaction décrite dans la notice.", "Interagit : substrat du CYP3A4."]),
    "ENDO-ND-PHARMA-QCM-031": dict(h=_CYCLO_H, e=_CYCLO_E,
        o=["Interagit : inhibe le CYP3A4.", "Interagit : induit le CYP3A4.", "Interagit (antiépileptiques inducteurs).", "Réponse retenue, discutable : interaction décrite dans la notice.", "Interagit : substrat du CYP3A4."]),
    "ENDO-2025-01-PHARMA-QCM-096": dict(h=_CYCLO_H, e=_CYCLO_E,
        o=["Interagit : inhibe les cytochromes.", "Interagit : inhibe le CYP3A4.", "Interagit : induit le CYP3A4.", "Réponse retenue, discutable : interaction décrite dans la notice."]),
    "ENDO-ND-PHARMA-QCM-032": dict(
        h=["La ciclosporine passe par le CYP3A4 et la glycoprotéine P.",
           "Par où est-elle surtout éliminée : la bile ou l'urine ?",
           "Cette question a une correction discutée : lis l'explication après avoir répondu."],
        e="Correction discutée. La réponse retenue est que le « premier passage hépatique important » serait faux. Or la ciclosporine a une biodisponibilité faible et variable, avec un effet de premier passage notable dans l'intestin et le foie (CYP3A4, glycoprotéine P). Son absorption est lente et variable, son métabolisme passe par le CYP3A4, et son élimination est surtout biliaire : 3 à 6 % seulement dans les urines. « Élimination rénale » est donc au moins aussi inexacte. Aucune correction officielle n'existe.",
        o=["Réponse retenue, discutable : premier passage notable.",
           "Vrai.",
           "Vrai : absorption lente et variable.",
           "Inexacte aussi : élimination surtout biliaire.",
           "Vrai."]),
    "ENDO-2023-05-PHARMA-QCM-094": dict(h=_SIRO_H, e=_SIRO_E,
        o=["Vrai : biodisponibilité d'environ 14 %.", "Vrai.", "Faux (réponse retenue) : absorption rapide.", "Inexacte aussi : 2,2 % dans les urines.", "Vrai."]),
    "ENDO-ND-PHARMA-QCM-034": dict(h=_SIRO_H, e=_SIRO_E,
        o=["Vrai : biodisponibilité d'environ 14 %.", "Vrai.", "Faux (réponse retenue) : absorption rapide.", "Inexacte aussi : 2,2 % dans les urines.", "Vrai.", "Vrai : pic en 1 à 2 heures."]),

    # ═════════════ Hypolipémiants ═════════════
    "ENDO-ND-PHARMA-QCM-021": dict(
        h=["Le cholestérol vient de deux sources : la fabrication par le foie et l'absorption par l'intestin.",
           "Les statines agissent sur une enzyme du foie.",
           "Quel médicament bloque l'absorption intestinale ?"],
        e="Les statines inhibent l'HMG-CoA réductase, enzyme clé de la fabrication du cholestérol dans le foie : le LDL-cholestérol baisse. Elles sont métabolisées par le foie (souvent par le CYP3A4) et ont de nombreuses interactions. L'inhibition de l'absorption intestinale du cholestérol est le mécanisme de l'ézétimibe, pas des statines.",
        o=["Faux (réponse attendue) : c'est l'ézétimibe.", "Vrai.", "Vrai.", "Vrai : souvent par le CYP3A4.", "Vrai."]),
}
