"""Génère content/questions/*.json à partir d'une spécification compacte (saisie manuelle phase 4).
Les énoncés et propositions des questions d'archives reproduisent la retranscription originale.
Usage : python3 scripts/content/build_questions.py"""
import json, os, collections
ROOT = os.path.join(os.path.dirname(__file__), "..", "..", "content", "questions")
SRC = {"A": "#Compilation endocrino 2016-2024.pdf", "E": "02_Retranscription Janvier 2025 - Secteur Endocrinologie.pdf", "G": "Retranscription – Janvier 2026 _ Secteur Endocrinologie (1).pdf"}
COMP = "complement"
L = "ABCDEFGHIJ"
files = collections.OrderedDict()

def Q(file, id, ref, src, session, disc, teacher, page, num, instruction, stem, options, expected, chapter, sub, lessons,
      hints, expl, per=None, pitfall=None, tags=(), diff=2, clinical=False, dup=None, comments=(), labs=(), former=False,
      status="proposed", note=None):
    q = {"id": id, "kind": "archive", "format": "mcq", "instruction": instruction, "stem": stem, "labs": list(labs),
         "options": [{"id": L[i], "text": t, **({"explanation": per[i]} if per else {})} for i, t in enumerate(options)],
         "expected": list(expected), "answerStatus": status, "sourceComments": list(comments),
         "provenance": {"session": session, "discipline": disc, "teacher": teacher, "formerTeacher": former,
                        "sourceFile": SRC[src], "page": page, "originalNumber": num, "auditRef": ref},
         "chapter": chapter, "subchapter": sub, "lessonLinks": lessons, "tags": list(tags), "difficulty": diff,
         "clinical": clinical, "hints": hints, "explanation": {"text": expl, "status": COMP, "sources": []}}
    if note: q["answerNote"] = note
    if pitfall: q["pitfall"] = pitfall
    if dup: q["duplicateGroup"] = dup
    files.setdefault(file, []).append(q)

def VF(file, n, chapter, sub, lessons, statement, truth, expl, hints, tags=()):
    files.setdefault(file, []).append({
        "id": f"ENDO-EX-{chapter}-VF-{n:03d}", "kind": "exercise", "format": "true-false", "stem": statement, "labs": [],
        "options": [], "expected": ["VRAI" if truth else "FAUX"], "answerStatus": "authored", "sourceComments": [],
        "chapter": chapter, "subchapter": sub, "lessonLinks": lessons, "tags": list(tags), "difficulty": 1, "clinical": False,
        "hints": hints, "explanation": {"text": expl, "status": COMP, "sources": []}})

# ============================ COURS 1 — PATHOLOGIES THYROÏDIENNES ============================
Q("2024-01", "ENDO-2024-01-ADULTE-QCM-031", "2024-01-Q31", "A", "2024-01", "ADULTE", None, 5, 31, "one-false",
  "Une TSH abaissée peut être observée dans toutes ces situations, sauf une:",
  ["Une hyperthyroïdite débutante", "Au diagnostic d’une thyroïdite silencieuse", "Au premier trimestre d’une grossesse",
   "Dans une insuffisance antéhypophysaire traitée par L-thyroxyne", "Lors d’une carence sévère en iode"], ["E"],
  "thyroide", "explo", ["thyr-explo", "hyper-diagnostic"],
  ["Pour chaque situation, demande-toi si l’hypophyse « reçoit » trop d’hormones, ou si elle est incapable de produire de la TSH.",
   "La TSH baisse quand il y a trop d’hormones thyroïdiennes (rétrocontrôle), au 1er trimestre (hCG) ou quand l’hypophyse est malade.",
   "Une situation fait fabriquer MOINS d’hormones par la thyroïde : que fait alors la TSH ?"],
  "La carence sévère en iode diminue la production d’hormones thyroïdiennes : la TSH a tendance à monter (et un goitre apparaît). Toutes les autres situations peuvent donner une TSH basse.",
  ["Vrai : l’excès d’hormones freine la TSH.", "Vrai : phase de relargage d’hormones, TSH freinée.",
   "Vrai : l’hCG stimule le récepteur de la TSH, la TSH baisse.", "Vrai : l’hypophyse déficitaire ne produit pas de TSH (et la L-thyroxine la freine).",
   "Faux (réponse attendue) : la carence iodée fait plutôt monter la TSH."],
  "Retenir que la TSH ne baisse jamais à cause d’un MANQUE d’hormones d’origine thyroïdienne.", tags=["TSH"], dup="TSH-BASSE")

Q("nd-maiter", "ENDO-ND-ADULTE-QCM-219", "ND-maiter-thyroide-Q19", "A", "ND", "ADULTE", "Maiter", 55, 19, "one-false",
  "Tout ce qui suit entraîne une diminution de TSH sauf :",
  ["Thyroïdite De quervain", "R/ hormone thyroïdienne", "1 er trimestre de grossesse", "Hyperprolactinémie sévère", "Insuffisance antéhypophysaire complète"],
  ["D"], "thyroide", "explo", ["thyr-explo"],
  ["Classe les propositions : excès d’hormones, hCG, atteinte de l’hypophyse… et l’intrus.",
   "Une insuffisance antéhypophysaire empêche la production de TSH ; une thyroïdite en phase initiale libère des hormones.",
   "L’intrus concerne une autre hormone hypophysaire, sans lien direct avec la baisse de la TSH."],
  "Une hyperprolactinémie n’abaisse pas la TSH. Les autres situations la diminuent : relargage d’hormones (De Quervain), traitement par hormones thyroïdiennes, hCG du 1er trimestre, insuffisance hypophysaire.",
  ["Vrai : phase d’hyperthyroïdie transitoire.", "Vrai : rétrocontrôle par l’hormone donnée.", "Vrai : effet de l’hCG.",
   "Faux (réponse attendue) : la prolactine n’abaisse pas la TSH.", "Vrai : pas de production de TSH."],
  tags=["TSH"], dup="TSH-BASSE")

Q("2024-01", "ENDO-2024-01-ADULTE-QCM-026", "2024-01-Q26", "A", "2024-01", "ADULTE", None, 4, 26, "one-false",
  "Face à un nodule thyroïdien, un de ces éléments n’est pas en faveur d’un caractère cancéreux ?",
  ["Âge > 70 ans.", "Sexe masculin.", "Antécédents d’irradiation du cou.", "TSH abaissée.", "Présence de calcifications à l’écho du cou."],
  ["D"], "thyroide", "nodules", ["thyr-nodules"],
  ["Pense à ce que signifie un nodule qui « freine » la TSH.",
   "Un nodule autonome produit des hormones et apparaît « chaud » à la scintigraphie.",
   "Les nodules chauds sont presque toujours bénins."],
  "Une TSH basse oriente vers un nodule autonome (chaud), presque toujours bénin. L’âge avancé, le sexe masculin, l’irradiation cervicale et les (micro)calcifications sont des arguments de suspicion.",
  ["Vrai : les âges extrêmes augmentent le risque.", "Vrai : un nodule chez l’homme est plus suspect.", "Vrai : facteur de risque majeur.",
   "Faux (réponse attendue) : TSH basse = nodule probablement chaud, bénin.", "Vrai : surtout les microcalcifications."],
  "Ne pas confondre « fréquence » (plus de nodules chez la femme) et « suspicion » (plus suspect chez l’homme).", tags=["nodule"], dup="NOD-SUSP")

Q("2023-05", "ENDO-2023-05-ADULTE-QCM-044", "2023-05-Q44", "A", "2023-05", "ADULTE", None, 20, 44, "one-false",
  "Face un nodule thyroïdien, les éléments suivants augmentent la suspicion d’une pathologie cancéreuse, sauf UN, Lequel ?",
  ["Adénopathie cervicale", "Le sexe féminin", "Un ATCD d’irradiation cervicale", "Un nodule dur et fixé", "Des microcalcifications présentes à l’échographie"],
  ["B"], "thyroide", "nodules", ["thyr-nodules"],
  ["Un seul élément concerne le terrain sans augmenter le risque relatif.",
   "Les nodules sont plus FRÉQUENTS dans un sexe mais plus SUSPECTS dans l’autre.",
   "Lequel des deux sexes rend un nodule plus suspect ?"],
  "Le sexe féminin rend les nodules plus fréquents, mais c’est chez l’homme qu’un nodule est plus suspect. Adénopathie, irradiation, nodule dur et fixé et microcalcifications sont des arguments de malignité.",
  ["Vrai : possible métastase ganglionnaire.", "Faux (réponse attendue) : c’est le sexe masculin qui augmente la suspicion.",
   "Vrai : facteur de risque majeur.", "Vrai : signe clinique d’infiltration.", "Vrai : évoque un cancer papillaire."],
  tags=["nodule"], dup="NOD-SUSP")

Q("2023-05", "ENDO-2023-05-ADULTE-QCM-039", "2023-05-Q39", "A", "2023-05", "ADULTE", None, 19, 39, "one-false",
  "Palpation nodule thyroidien unique 4 examens complémentaires à faire, un à NE PAS faire",
  ["dosage TSH", "dosage plasmatique anticorps thyréostimulant (TSI)", "dosage plasmatique calcitonine", "echographie de la zone thyroidienne", "scintigraphie de thyroide à l’iode 123"],
  ["B"], "thyroide", "nodules", ["thyr-nodules"],
  ["Quels examens servent à évaluer un NODULE, et lesquels servent à diagnostiquer une MALADIE diffuse ?",
   "Un des anticorps proposés signe une maladie auto-immune précise de toute la glande.",
   "Les TSI (anticorps stimulant le récepteur de la TSH) sont le marqueur de la maladie de Basedow."],
  "Devant un nodule isolé : TSH (fonction), échographie (risque EU-TIRADS), calcitonine (cancer médullaire) et scintigraphie si la TSH est basse. Les TSI servent au diagnostic de Basedow, pas à l’évaluation d’un nodule.",
  ["Utile : toujours en premier.", "Inutile (réponse attendue) : marqueur de Basedow.", "Utile : dépistage du cancer médullaire.",
   "Utile : examen clé du nodule.", "Utile si la TSH est basse (nodule chaud ?)."],
  tags=["nodule", "anticorps"], dup="NOD-BILAN")

Q("2026-01", "ENDO-2026-01-RADIO-QCM-040", "2026-01-Q40", "G", "2026-01", "RADIO", None, 9, 40, "one-false",
  "Pour classification de EU-TIRADS, parmi ces éléments il y en a 1 faux : (tuyau)",
  ["L'échogénicité", "Spongiforme ou kystique", "Vascularisation", "La forme des contours", "Microcalcifications"],
  ["C"], "thyroide", "nodules", ["thyr-nodules"],
  ["EU-TIRADS repose sur l’aspect du nodule en mode B (noir et blanc).",
   "Les signes de forte suspicion : forme, contours, microcalcifications, hypoéchogénicité marquée.",
   "Un élément proposé nécessite le Doppler couleur."],
  "EU-TIRADS classe le nodule selon son échogénicité, sa structure (spongiforme, kystique), sa forme, ses contours et la présence de microcalcifications. La vascularisation (Doppler) n’entre pas dans la classification.",
  ["Pris en compte.", "Pris en compte : spongiforme ou kystique pur = bénin.", "Non pris en compte (réponse attendue).", "Pris en compte.", "Pris en compte."],
  tags=["EU-TIRADS", "échographie"], dup="EUTIRADS")

Q("nd-duprez-coche", "ENDO-ND-RADIO-QCM-114", "ND-duprez-coche-imagerie-Q114", "A", "ND", "RADIO", "Duprez/Coche", 85, 114, "one-correct",
  "Lequel de ces nodules de la thyroïde il ne faut pas ponctionner",
  ["jeune homme", "calcification", "signe de la comète", "vascularisation anarchique intranodulaire", "nodule froid"],
  ["C"], "thyroide", "nodules", ["thyr-nodules"],
  ["Cherche le signe échographique RASSURANT.",
   "Certains artefacts brillants sont liés à la colloïde épaisse.",
   "Ce signe porte le nom d’un objet céleste à queue lumineuse."],
  "Le signe de la comète (artefact en « queue de comète ») est lié à la colloïde : il est typique d’un nodule colloïde bénin et n’impose pas de ponction. Les autres éléments sont des arguments de suspicion.",
  ["À ponctionner : terrain plus suspect.", "Plutôt suspect (surtout les microcalcifications).", "Ne pas ponctionner (réponse attendue) : signe bénin.",
   "Suspect.", "Un nodule froid n’est pas autonome : il ne bénéficie pas de l’argument « chaud = bénin »."],
  tags=["échographie", "cytoponction"], dup="CYTOPONCTION")

Q("2026-01", "ENDO-2026-01-ADULTE-QCM-017", "2026-01-Q17", "G", "2026-01", "ADULTE", "Alexopoulou", 4, 17, "one-false",
  "Concernant le cancer papillaire de la thyroïde, quelle réponse est fausse ?",
  ["Multifocal", "Dissémination hémathogène des métastases", "Plus fréquent chez la femme", "Bon pronostic", "Provoqué par irradiation cervicale"],
  ["B"], "thyroide", "cancers", ["thyr-cancers"],
  ["Compare les deux cancers différenciés : papillaire et folliculaire.",
   "Ils ne se propagent pas de la même façon.",
   "Le papillaire atteint d’abord les ganglions du cou."],
  "Le cancer papillaire dissémine surtout par voie lymphatique (ganglions cervicaux). La dissémination hématogène est typique du cancer folliculaire. Le papillaire est souvent multifocal, plus fréquent chez la femme, favorisé par l’irradiation et de bon pronostic.",
  ["Vrai.", "Faux (réponse attendue) : voie lymphatique.", "Vrai.", "Vrai.", "Vrai : facteur de risque reconnu."],
  "Papillaire = lymphatique ; folliculaire = hématogène.", tags=["cancer"], dup="CANCERS")

Q("nd-maiter", "ENDO-ND-ADULTE-QCM-227", "ND-maiter-thyroide-Q27", "A", "ND", "ADULTE", "Maiter", 56, 27, "one-true",
  "Concernant les K de la thyroïde (1 vraie)",
  ["K Papillaire est le plus fréquent", "K anaplasique répond à une Radiothérapie poussée", "K à cellules de Hurthle est indifférencié",
   "Tous les cancers de la thyroïde se traite par thyroïdectomie et radiothérapie", "Le cancer folliculaire métastase surtout par voie lymphatique"],
  ["A"], "thyroide", "cancers", ["thyr-cancers"],
  ["Cherche l’affirmation épidémiologique simple.",
   "L’anaplasique est le plus agressif ; le folliculaire voyage par le sang.",
   "Un des cancers représente la grande majorité des cas."],
  "Le cancer papillaire est de loin le plus fréquent. L’anaplasique répond mal aux traitements ; le Hürthle (oncocytaire) est un carcinome différencié ; les traitements dépendent du type ; le folliculaire métastase surtout par voie hématogène.",
  ["Vrai (réponse attendue).", "Faux : très mauvais pronostic, réponse médiocre.", "Faux : carcinome différencié (oncocytaire).",
   "Faux : le traitement dépend du type et du risque.", "Faux : voie hématogène."],
  tags=["cancer"], dup="CANCERS", comments=["Artefact de retranscription « l,; » supprimé en fin de proposition A."])

Q("2022-05", "ENDO-2022-05-ADULTE-QCM-030", "2022-05-Q30", "A", "2022-05", "ADULTE", None, 31, 30, "one-false",
  "A propos de la thyroïdite de Quervain quelle proposition est fausse?",
  ["Il y a un syndrome inflammatoire biologique important", "Le patient peut se plaindre de douleur cervicale parfois intense",
   "A la scintigraphie il a y a une captation intense du traceur", "Traitement le plus souvent par glucocorticoïdes",
   "C’est une thyroïdite granulomateuse d’étiologie virale"],
  ["C"], "thyroide", "thyroidites", ["thyr-thyroidites", "hyper-diagnostic"],
  ["Rappelle-toi d’où viennent les hormones en excès dans une thyroïdite.",
   "Dans une thyroïdite destructrice, la glande ne fabrique pas davantage.",
   "Que montre la scintigraphie quand les cellules thyroïdiennes ne captent plus ?"],
  "Dans la thyroïdite de De Quervain, les follicules sont détruits : les hormones s’échappent, mais la glande ne capte plus le traceur. La scintigraphie est « blanche ». Syndrome inflammatoire, douleur, traitement anti-inflammatoire (AINS ou corticoïdes) et origine virale granulomateuse sont exacts.",
  ["Vrai.", "Vrai.", "Faux (réponse attendue) : scintigraphie blanche.", "Vrai (AINS ou corticoïdes).", "Vrai."],
  tags=["De Quervain", "scintigraphie"], dup="QUERVAIN")

Q("nd-maiter", "ENDO-ND-ADULTE-QCM-231", "ND-maiter-thyroide-Q31", "A", "ND", "ADULTE", "Maiter", 57, 31, "one-correct",
  "Femme avec douleur cervicale, subfébrile, syndrome inflammatoire à la biologie, TSH effondrée, T4l élevée: quel diagnostic envisager en premier lieu?",
  ["Cancer thyroïdien", "Basedow", "Thyroïdite subaiguë de De Quervain", "Crise sur fond chronique de maladie d’Hashimoto", "Hématome de la thyroïde"],
  ["C"], "thyroide", "thyroidites", ["thyr-thyroidites", "hyper-diagnostic"],
  ["Relève les trois éléments clés : douleur, fièvre, inflammation.",
   "Une seule cause d’hyperthyroïdie est à la fois douloureuse et fébrile.",
   "Elle survient souvent après une infection virale."],
  "Douleur cervicale + fébricule + syndrome inflammatoire + hyperthyroïdie = thyroïdite subaiguë de De Quervain. Basedow et Hashimoto sont indolores ; un cancer ou un hématome ne donnent pas ce tableau.",
  ["Non : ni fièvre ni hyperthyroïdie attendues.", "Non : indolore, pas de syndrome inflammatoire.", "Oui (réponse attendue).",
   "Non : Hashimoto est indolore et évolue vers l’hypothyroïdie.", "Non : contexte traumatique ou nodule hémorragique."],
  tags=["De Quervain", "cas clinique"], clinical=True, dup="QUERVAIN")

Q("nd-maiter", "ENDO-ND-ADULTE-QCMM-228", "ND-maiter-thyroide-Q28", "A", "ND", "ADULTE", "Maiter", 56, 28, "two-false",
  "A propos de la thyroïdite silencieuse, quelles sont les 2 fausses propositions?",
  ["Douleur cervicale", "Hyperthyroïdie biologique", "Thyroglobuline indosable", "Scintigraphie blanche", "Présence d’anticorps anti-thyroïdien"],
  ["A", "C"], "thyroide", "thyroidites", ["thyr-thyroidites", "hyper-diagnostic"],
  ["Le nom de la maladie donne déjà une réponse.",
   "Thyroïdite destructrice = relargage du contenu des follicules.",
   "Que devient la thyroglobuline quand des follicules sont détruits ?"],
  "La thyroïdite silencieuse est INDOLORE (d’où son nom) et destructrice : la thyroglobuline est ÉLEVÉE. Elle donne une hyperthyroïdie biologique transitoire, une scintigraphie blanche et des anticorps (anti-TPO) souvent positifs.",
  ["Faux (attendue) : indolore.", "Vrai.", "Faux (attendue) : Tg élevée ; une Tg indosable évoque une prise exogène.", "Vrai.", "Vrai : anti-TPO fréquents."],
  tags=["thyroïdite silencieuse"], dup="SILENCIEUSE")

Q("nd-marbaix", "ENDO-ND-ANAPATH-QCM-117", "ND-marbaix-thyroide-parathyroides-Q17", "A", "ND", "ANAPATH", "Marbaix", 83, 17, "one-true",
  "Dans la maladie d’Hashimoto (1 vraie)",
  ["On voit des infiltrats B et T qui attaquent la glande", "On y trouve des granulomes dirigés contre colloïde",
   "Se caractérise par une hyperplasie de cellules médullaires (plus trop sûre de la formulation)",
   "Elle se caractérise histologiquement par de la fibrose, l’aspect évoque un cancer", "C’est la seule maladie auto-immune de la thyroïde"],
  ["A"], "thyroide", "thyroidites", ["thyr-thyroidites", "hypo-diagnostic"],
  ["Hashimoto est une maladie auto-immune : quelles cellules infiltrent la glande ?",
   "Les granulomes caractérisent une autre thyroïdite.",
   "L’infiltrat est lymphoplasmocytaire, avec des follicules lymphoïdes."],
  "Hashimoto : infiltrat lymphocytaire B et T (avec follicules lymphoïdes et cellules oncocytaires) qui détruit le parenchyme. Les granulomes caractérisent De Quervain ; la fibrose pseudo-tumorale évoque Riedel ; Basedow est une autre maladie auto-immune.",
  ["Vrai (réponse attendue).", "Faux : granulomes = De Quervain.", "Faux : sans rapport (formulation incertaine).", "Faux : thyroïdite de Riedel.", "Faux : Basedow est aussi auto-immun."],
  tags=["Hashimoto", "anatomie pathologique"], dup="HASHI-ANAPATH", comments=["Proposition C : « plus trop sûre de la formulation » (transcripteur)."])

Q("nd-maiter", "ENDO-ND-ADULTE-QCM-235", "ND-maiter-thyroide-Q35", "A", "ND", "ADULTE", "Maiter", 57, 35, "one-false",
  "Toutes ces maladies donnent un goitre sauf une :",
  ["M+ d’Hashimoto", "M+ de Graves/Basedow", "Carence en iode", "Troubles de la dyshormonogenèse", "Prise d’hormones thyroïdiennes"],
  ["E"], "thyroide", "goitre", ["thyr-goitre"],
  ["Un goitre apparaît quand la glande est stimulée ou infiltrée.",
   "Quatre propositions stimulent ou infiltrent la glande.",
   "Une proposition freine la TSH."],
  "La prise d’hormones thyroïdiennes freine la TSH : la glande diminue de volume. Hashimoto (infiltration), Basedow (anticorps stimulants), carence iodée et troubles de l’hormonogenèse (TSH élevée) donnent un goitre.",
  ["Donne un goitre (ferme).", "Donne un goitre diffus.", "Donne un goitre.", "Donne un goitre (TSH élevée).", "Ne donne pas de goitre (réponse attendue)."],
  tags=["goitre"], dup="GOITRE")

# ============================ COURS 2 — HYPERTHYROÏDIE ============================
Q("2022-05", "ENDO-2022-05-ADULTE-QCM-032", "2022-05-Q32", "A", "2022-05", "ADULTE", None, 31, 32, "one-correct",
  "jeune de 20 ans mannequin vient avec des symptômes de l'hyperthyroïdie. T4 est un peu au dessus de la normale, T3 fortement élevée, thyroglobuline indétectable, anticorps négatifs :",
  ["Basedow", "Prise exogène des hormones thyroïdiennes", "Thyroïdite de De Quervain", "Hashimoto", "Nodule chaud"],
  ["B"], "hyper", "diagnostic", ["hyper-diagnostic", "hyper-autres"],
  ["Le contexte (mannequin) et un dosage sont décisifs.",
   "La thyroglobuline est produite par la glande : que signifie qu’elle soit indétectable ?",
   "Si la glande ne libère rien, d’où viennent les hormones en excès ?"],
  "Hormones élevées (surtout T3) avec une thyroglobuline indétectable : la glande est freinée et les hormones viennent de l’extérieur. Il s’agit d’une prise exogène (ici probablement de T3). Basedow, De Quervain et nodule chaud s’accompagnent d’une Tg élevée.",
  ["Non : TRAK positifs, Tg élevée.", "Oui (réponse attendue).", "Non : douleur, Tg élevée.", "Non : évolue vers l’hypothyroïdie.", "Non : Tg élevée."],
  "Toujours vérifier l’absence d’anticorps anti-Tg avant d’interpréter une Tg basse.", tags=["thyroglobuline", "cas clinique"], diff=3, clinical=True, dup="EXOGENE")

Q("nd-maiter", "ENDO-ND-ADULTE-QCM-232", "ND-maiter-thyroide-Q32", "A", "ND", "ADULTE", "Maiter", 57, 32, "one-correct",
  "Femme de 52 ans avec symptômes avec TSH=0, T4 augmentée (=4ng), Ac anti-TG négatifs, Tg augmentée (60; Nle = 40), que peut-on exclure (une bonne réponse)",
  ["Hyperthyroïdie factice", "Goître multinodulaire", "Maladie de Basedow", "Nodule toxique", "Thyroïdite silencieuse"],
  ["A"], "hyper", "diagnostic", ["hyper-diagnostic", "hyper-autres"],
  ["La question demande ce qu’on peut EXCLURE.",
   "Regarde la thyroglobuline et les anticorps anti-Tg.",
   "Quelle cause d’hyperthyroïdie s’accompagne d’une Tg effondrée ?"],
  "La Tg est augmentée, et les anti-Tg sont négatifs (le dosage est fiable) : la glande libère de la Tg. On peut donc exclure une hyperthyroïdie factice (prise exogène), qui l’effondre. Les autres causes s’accompagnent d’une Tg élevée.",
  ["À exclure (réponse attendue).", "Possible.", "Possible.", "Possible.", "Possible (Tg élevée par relargage)."],
  tags=["thyroglobuline", "cas clinique"], diff=3, clinical=True, dup="EXOGENE",
  labs=[{"analyte": "TSH", "value": "0", "unit": "", "referenceOrigin": "énoncé"}, {"analyte": "T4", "value": "4", "unit": "ng", "referenceOrigin": "énoncé (« augmentée (=4ng) »)"},
        {"analyte": "Thyroglobuline", "value": "60", "unit": "", "reference": "40", "referenceOrigin": "énoncé (« Nle = 40 »)"}])

Q("2025-01", "ENDO-2025-01-ADULTE-QCM-030", "2025-01-Q30", "E", "2025-01", "ADULTE", None, 6, 30, "one-correct",
  "Ce qui ne cause pas une hyperthyroïdie (1 bonne réponse)",
  ["basedow", "goitre multinodulaire toxique", "carence en iode", "adénome hypophysaire à TSH", "adénome folliculaire toxique"],
  ["C"], "hyper", "diagnostic", ["hyper-diagnostic"],
  ["Quatre propositions font produire trop d’hormones.",
   "Une proposition prive la thyroïde de sa matière première.",
   "Sans iode, peut-on fabriquer trop d’hormones ?"],
  "La carence en iode diminue la synthèse d’hormones (goitre, voire hypothyroïdie) ; elle ne cause pas directement d’hyperthyroïdie. Basedow, goitre multinodulaire toxique, adénome thyréotrope et adénome toxique sont des causes d’hyperthyroïdie.",
  ["Cause d’hyperthyroïdie.", "Cause d’hyperthyroïdie.", "Ne cause pas d’hyperthyroïdie (réponse attendue).", "Cause rare (TSH non freinée).", "Cause d’hyperthyroïdie."],
  tags=["iode"], dup="ETIO-HYPER")

Q("2025-01", "ENDO-2025-01-ADULTE-QCM-027", "2025-01-Q27", "E", "2025-01", "ADULTE", None, 5, 27, "one-false",
  "Concernant la maladie de Basedow/Graves, 1 réponse fausse",
  ["Présence d’anticorps anti récepteurs à TSH", "Peut causer une exophtalmie", "Peut causer une perturbation des tests hépatiques",
   "Strumazole est plus indiqué que le propylthiouracile (PTU) comme traitement pendant le premier trimestre de grossesse",
   "Après traitement, on observe une rechute dans 50% des cas"],
  ["D"], "hyper", "basedow", ["hyper-basedow", "hyper-traitements"],
  ["Une proposition concerne un choix de médicament pendant la grossesse.",
   "Un des deux ATS est associé à un risque de malformations pendant l’organogenèse.",
   "Lequel préfère-t-on au 1er trimestre ?"],
  "Au 1er trimestre de grossesse (et en projet de grossesse), on préfère le PTU, car le thiamazole (Strumazol) est associé à un risque de malformations ; on revient au thiamazole ensuite. Les autres propositions sont exactes.",
  ["Vrai : TRAK.", "Vrai : orbitopathie.", "Vrai.", "Faux (réponse attendue) : c’est le PTU au 1er trimestre.", "Vrai : environ la moitié des patients."],
  tags=["Basedow", "grossesse", "ATS"], dup="BASEDOW-ATS")

Q("nd-maiter", "ENDO-ND-ADULTE-QCM-222", "ND-maiter-thyroide-Q22", "A", "ND", "ADULTE", "Maiter", 56, 22, "one-false",
  "Concernant le traitement de la maladie de Basedow, laquelle est fausse :",
  ["Le strumazol est le premier traitement dans un Basedow", "Une agranulocytose est une contre-indication stricte à l’utilisation des ATS",
   "Le PTU est le traitement de choix durant le 3ème trimestre de la grossesse", "Les fumeurs sont plus à risque d'exophtalmie basedowienne"],
  ["C"], "hyper", "basedow", ["hyper-basedow", "hyper-traitements"],
  ["Une proposition se trompe de trimestre.",
   "Le PTU est hépatotoxique : on ne le garde pas plus longtemps que nécessaire.",
   "Le PTU est réservé à une période précise de la grossesse."],
  "Le PTU est réservé au projet de grossesse et au 1er trimestre ; au 2e et 3e trimestres, on revient au thiamazole. Le thiamazole est le premier traitement, l’agranulocytose contre-indique les ATS et le tabac favorise l’orbitopathie.",
  ["Vrai.", "Vrai.", "Faux (réponse attendue) : PTU au 1er trimestre.", "Vrai."],
  tags=["Basedow", "ATS", "grossesse"], dup="BASEDOW-ATS")

Q("2026-01", "ENDO-2026-01-ADULTE-QCM-014", "2026-01-Q14", "G", "2026-01", "ADULTE", "Alexopoulou", 4, 14, "one-false",
  "A propos de l’hyperthyroidie sur amiodarone la FAUSSE:",
  ["type 1 due a une patho preexistante", "type 2 due a thyroidite destructive", "Scinti type 2 montre une hyperfixation", "type 1 se traite par ATS", "type 2 se traite par corticoides"],
  ["C"], "hyper", "iatrogene", ["hyper-autres"],
  ["Le type 2 est une thyroïdite.",
   "Que montre la scintigraphie dans toutes les thyroïdites destructrices ?",
   "Une glande détruite ne capte pas le traceur."],
  "Le type 2 est une thyroïdite destructrice : la scintigraphie est blanche (pas d’hyperfixation) et le traitement repose sur les corticoïdes. Le type 1 (surcharge iodée sur glande préalablement malade) se traite par ATS.",
  ["Vrai.", "Vrai.", "Faux (réponse attendue) : scintigraphie blanche.", "Vrai (± perchlorate).", "Vrai."],
  tags=["amiodarone", "scintigraphie"], dup="AMIODARONE")

Q("nd-horsmans", "ENDO-ND-PHARMA-QCM-006", "ND-horsmans-hormones-Q6", "A", "ND", "PHARMA", "Horsmans", 88, 6, "one-false",
  "Concernant les complications des anti-thyroïdiens de synthèse, quelle est la fausse ?",
  ["Œsophagite", "Dysgueusie", "Leucopénie", "Hépatotoxicité"],
  ["A"], "hyper", "basedow", ["hyper-traitements", "hyper-basedow"],
  ["Pense aux effets hématologiques, hépatiques et sensoriels des ATS.",
   "Les ATS sont pris par voie orale mais ne sont pas connus pour léser la muqueuse œsophagienne.",
   "Trois propositions sont des effets indésirables classiques des ATS."],
  "Les ATS peuvent donner une leucopénie (et une agranulocytose), une hépatotoxicité et une dysgueusie. L’œsophagite n’est pas une complication des ATS.",
  ["Faux (réponse attendue).", "Vrai.", "Vrai.", "Vrai (surtout le PTU)."],
  tags=["ATS", "pharmacologie"], dup="ATS-PHARMA")

# ============================ COURS 3 — HYPOTHYROÏDIE ============================
Q("nd-maiter", "ENDO-ND-ADULTE-QCM-209", "ND-maiter-thyroide-Q9", "A", "ND", "ADULTE", "Maiter", 54, 9, "one-correct",
  "Une patiente de 75 ans, avec hypothyroïdie connue suite à une thyroïdectomie totale, est traitée chroniquement par lévothyroxine sodique 125 microgramme/jour le matin. Elle vous consulte pour des palpitations récentes la nuit. Sa biologie récente montre une TSH à 0,20 microU/mL (nl : 0,30-3,5), une T4 libre à 18 pmol/L (nl : 12-22) et une T3 libre à 2,2 pmol/L (nl : 2,0-6,0). Que lui conseillez-vous ? (Une seule bonne réponse)",
  ["Vous poursuivez la même dose de L-Thyroxine mais vous insistez sur la prise au matin à jeun",
   "Vous poursuivez la même dose de L-Thyroxine et lui prescrivez un Beta-Bloquant selectif à faible dose le soir",
   "Vous augmentez la dose de la Thyroxine à 150 microgramme/jour", "Vous diminuez la dose de la Thyroxine à 100 microgramme/jour",
   "Vous diminuez la dose de la Thyroxine à 50 microgramme/jour"],
  ["D"], "hypo", "traitement", ["hypo-traitement"],
  ["Interprète d’abord la TSH par rapport à la norme donnée.",
   "Une TSH basse sous L-thyroxine signifie un léger surdosage, à risque chez une personne âgée (FA, ostéoporose).",
   "On corrige par paliers, sans changement brutal."],
  "TSH basse (0,20) avec T4L haute-normale chez une patiente âgée et symptomatique : léger surdosage. On diminue la dose d’un palier (125 → 100 µg), puis on recontrôle. Un bêtabloquant masquerait le problème ; 50 µg serait une baisse trop brutale.",
  ["Non : la prise n’est pas en cause, la dose est trop forte.", "Non : traiterait le symptôme, pas le surdosage.", "Non : aggraverait le surdosage.",
   "Oui (réponse attendue) : baisse d’un palier.", "Non : baisse excessive, risque d’hypothyroïdie."],
  "Le surdosage est l’effet indésirable principal des hormones thyroïdiennes.", tags=["L-thyroxine", "sujet âgé", "cas clinique"], diff=3, clinical=True, dup="LT4-AGEE",
  labs=[{"analyte": "TSH", "value": "0,20", "unit": "µU/mL", "reference": "0,30-3,5", "referenceOrigin": "énoncé"},
        {"analyte": "T4 libre", "value": "18", "unit": "pmol/L", "reference": "12-22", "referenceOrigin": "énoncé"},
        {"analyte": "T3 libre", "value": "2,2", "unit": "pmol/L", "reference": "2,0-6,0", "referenceOrigin": "énoncé"}])

Q("2024-01", "ENDO-2024-01-ADULTE-QCM-032", "2024-01-Q32", "A", "2024-01", "ADULTE", None, 5, 32, "one-correct",
  "Une dame de 76 ans avec une hypothyroïdie connue depuis thyroïdectomie totale, et traitée par Levothryroxine 75µg par jour, vient en consultation pour palpitations nocturnes. Sa prise de sang indique (j’ai plus les chiffres mais osef): TSH abaissée, T4 limite normale haute, T3 normale. Que faites-vous :",
  ["Maintenir le traitement en insistant bien sur la prise le matin à jeun.", "Maintenir le traitement en ajoutant des bétabloquants",
   "Augmenter le traitement à 100µg par jour", "Diminuer le traitement à 50µg par jour", "Arrêter le traitement"],
  ["D"], "hypo", "traitement", ["hypo-traitement"],
  ["Même raisonnement qu’avec des valeurs : que signifie une TSH abaissée sous traitement ?",
   "Chez une personne âgée, un surdosage expose à la fibrillation auriculaire.",
   "Elle n’a plus de thyroïde : arrêter n’est pas une option."],
  "TSH abaissée et palpitations sous L-thyroxine : léger surdosage. On diminue d’un palier (75 → 50 µg). L’arrêt est dangereux après une thyroïdectomie totale.",
  ["Non.", "Non : masque le surdosage.", "Non : aggrave.", "Oui (réponse attendue).", "Non : plus de thyroïde."],
  tags=["L-thyroxine", "sujet âgé", "cas clinique"], clinical=True, dup="LT4-AGEE",
  comments=["Valeurs biologiques non retranscrites (« j’ai plus les chiffres »)."])

Q("nd-maiter", "ENDO-ND-ADULTE-QCM-205", "ND-maiter-thyroide-Q5", "A", "ND", "ADULTE", "Maiter", 54, 5, "one-false",
  "Quel signe à la biologie ne retrouve-t-on pas en cas d’hypothyroïdie sévère (1 réponse):",
  ["Hypernatrémie", "Hyperprolactinémie", "Anémie normochrome normocytaire", "Hypercholestérolémie", "Augmentation des CPK musculaires"],
  ["A"], "hypo", "diagnostic", ["hypo-diagnostic"],
  ["Une seule anomalie va dans le « mauvais sens ».",
   "L’hypothyroïdie sévère gêne l’élimination de l’eau libre.",
   "Le sodium est-il alors trop haut ou trop bas ?"],
  "L’hypothyroïdie sévère donne une HYPOnatrémie (moindre élimination de l’eau). Elle peut donner une hyperprolactinémie (TRH élevée), une anémie, une hypercholestérolémie et des CPK élevées.",
  ["Non retrouvée (réponse attendue) : c’est une hyponatrémie.", "Retrouvée : la TRH stimule la prolactine.", "Retrouvée.", "Retrouvée.", "Retrouvée : myopathie."],
  tags=["biologie"], dup="HYPO-BIO")

Q("2026-01", "ENDO-2026-01-ADULTE-QCM-022", "2026-01-Q22", "G", "2026-01", "ADULTE", "Alexopoulou", 5, 22, "one-correct",
  "Que doser pour un bon suivi d'une hypothyroïdie centrale ?",
  ["TSH", "T4 libre", "T3 libre", "TRH", "Thyroglobuline"],
  ["B"], "hypo", "traitement", ["hypo-traitement", "hypo-diagnostic"],
  ["Où se situe la maladie dans une hypothyroïdie centrale ?",
   "Si l’hypophyse est malade, la TSH reflète-t-elle encore l’équilibre ?",
   "On suit alors directement l’hormone produite par la thyroïde."],
  "Dans l’hypothyroïdie centrale, la TSH (produite par l’hypophyse malade) n’est plus interprétable : le suivi du traitement se fait sur la T4 libre.",
  ["Non : inutilisable.", "Oui (réponse attendue).", "Non : peu fiable pour le suivi.", "Non : non dosée en pratique.", "Non : marqueur des cancers différenciés."],
  tags=["hypothyroïdie centrale"], dup="HYPO-CENTRALE")

Q("nd-maiter", "ENDO-ND-ADULTE-QCM-214", "ND-maiter-thyroide-Q14", "A", "ND", "ADULTE", "Maiter", 55, 14, "one-false",
  "Concernant la thyroïde, la fausse :",
  ["Hypothyroïdie chez les adultes en BE sont le plus souvent d’origine auto-immune.", "Une cause auto-immune peut aussi bien donner une hyperthyroïdie qu'une hypothyroïdie",
   "TSH est le meilleur marqueur de fonction thyroïdienne", "Scintigraphie n'est pas utile en cas d'hypothyroïdie chez l’adulte",
   "Il faut doubler les doses hormones thyroïdiennes le premier trimestre de grossesse"],
  ["E"], "hypo", "diagnostic", ["hypo-diagnostic", "hypo-grossesse"],
  ["Une proposition contient un chiffre trop fort.",
   "Pendant la grossesse, les besoins augmentent, mais de combien au début ?",
   "Les recommandations parlent d’environ 20 à 30 % (2 comprimés de plus par semaine)."],
  "On augmente la L-thyroxine dès la grossesse confirmée, d’environ 20 à 30 % (deux comprimés de plus par semaine), et non en doublant la dose. Les autres propositions sont exactes.",
  ["Vrai : Hashimoto.", "Vrai : Basedow ou Hashimoto.", "Vrai (si l’hypophyse est normale).", "Vrai.", "Faux (réponse attendue)."],
  tags=["grossesse", "Hashimoto"], dup="HYPO-ADULTE")

Q("2023-05", "ENDO-2023-05-PHARMA-QCM-087", "2023-05-Q87", "A", "2023-05", "PHARMA", "Horsmans", 25, 87, "one-correct",
  "Effet secondaire principal du traitement par hormones thyroïdiennes",
  ["Leucopénie", "Hépatite", "Hyperthyroïdie", "Dysgueusie", "Nausée"],
  ["C"], "hypo", "traitement", ["hypo-traitement"],
  ["Le médicament est l’hormone elle-même.",
   "Que se passe-t-il si on en donne trop ?",
   "L’effet indésirable reproduit une maladie thyroïdienne."],
  "La L-thyroxine est l’hormone naturelle : son effet indésirable principal est le surdosage, c’est-à-dire une hyperthyroïdie iatrogène. Leucopénie, hépatite et dysgueusie sont des effets des ATS.",
  ["Non : effet des ATS.", "Non : effet des ATS (PTU).", "Oui (réponse attendue).", "Non : effet des ATS.", "Non."],
  tags=["pharmacologie", "L-thyroxine"], dup="ES-HT")

Q("2023-05", "ENDO-2023-05-PEDIA-QCM-075", "2023-05-Q75", "A", "2023-05", "PEDIA", "Lysy", 24, 75, "one-correct",
  "Vous obtenez enfin un stage à la maternité tant attendu, mais votre joie disparait quand le centre de depistage vous appelle pour un enfant dont la TSH est à 720 mU/l. Le bébé en question est sorti il y a 7 jours (il en a 12 jours de vie). Quelle est l'attitude recommandée ?",
  ["Prévoir une consultation pour évaluer l'évolution clinique", "Prévoir des examens complémentaires pour évaluer l'enfant.",
   "On amène l'enfant en urgence et on lance des examens complémentaires",
   "On amène l'enfant en urgence, on fait des prélèvements biologiques et on commence le traitement par LThyroxine sans attendre les résultats de l imagerie",
   "On amène l'enfant en urgence et on fait un bilan complet (biologie+imagerie) pour évaluer la condition clinique et ensuite donner de la LThyroxine"],
  ["D"], "hypo", "congenitale", ["hypo-congenitale"],
  ["Chaque jour sans hormones compte pour le cerveau du nourrisson.",
   "Faut-il connaître la cause exacte (imagerie) avant de traiter ?",
   "On confirme par une prise de sang, puis on agit sans délai."],
  "Une TSH très élevée au dépistage est une urgence : on convoque l’enfant, on prélève pour confirmer, puis on commence la L-thyroxine immédiatement, sans attendre l’imagerie (qui précisera la cause plus tard).",
  ["Non : trop lent.", "Non : trop lent.", "Insuffisant : le traitement doit commencer tout de suite.", "Oui (réponse attendue).", "Non : l’imagerie ne doit pas retarder le traitement."],
  tags=["dépistage néonatal", "pédiatrie"], clinical=True, dup="NN-TSH",
  comments=["Dans la retranscription, les propositions sont lettrées f) à j) ; elles sont renumérotées A à E ici."])

Q("2026-01", "ENDO-2026-01-PEDIA-QCM-030", "2026-01-Q30", "G", "2026-01", "PEDIA", "Lysy", 8, 30, "one-correct",
  "Quel est l’inconvénient principal du test Guthrie ?",
  ["Ne peut être effectué que chez les prématurés", "Difficile de faire une PDS à un bébé", "Ne détecte pas une hypothyroïdie centrale", "Trop de FP d’hypothyroïdie", "Doit être effectué toutes les semaines après la naissance"],
  ["C"], "hypo", "congenitale", ["hypo-congenitale"],
  ["Qu’est-ce qui est dosé sur le papier buvard ?",
   "Le test cherche une TSH élevée.",
   "Dans quelle forme d’hypothyroïdie la TSH n’est-elle pas élevée ?"],
  "Le Guthrie dose la TSH : il dépiste les hypothyroïdies primaires, mais pas l’hypothyroïdie centrale, où la TSH n’est pas élevée.",
  ["Faux : réalisé chez tous les nouveau-nés.", "Faux : simple piqûre au talon.", "Vrai (réponse attendue).", "Faux.", "Faux : un seul prélèvement."],
  tags=["dépistage néonatal", "pédiatrie"], dup="GUTHRIE")

Q("nd-beauloye", "ENDO-ND-PEDIA-QCM-218", "ND-beauloye-pediatrie-p72-l3178", "A", "ND", "PEDIA", "Beauloye", 72, None, "one-false",
  "Le test de Guthrie permet de dépister toutes les maladies suivantes sauf une:",
  ["Syndrome de Pendred", "Athyréose", "Dyshormonogenèse", "Hypothyroïdie centrale", "Thyroïde ectopique"],
  ["D"], "hypo", "congenitale", ["hypo-congenitale"],
  ["Quatre propositions sont des atteintes de la thyroïde elle-même.",
   "Une proposition concerne l’hypophyse ou l’hypothalamus.",
   "Le dépistage repose sur une TSH élevée."],
  "Le dépistage par la TSH repère les hypothyroïdies primaires (athyréose, ectopie, dyshormonogenèse, syndrome de Pendred). L’hypothyroïdie centrale, avec une TSH non élevée, lui échappe.",
  ["Dépisté (dyshormonogenèse avec surdité).", "Dépisté.", "Dépisté.", "Non dépisté (réponse attendue).", "Dépisté (cause la plus fréquente)."],
  tags=["dépistage néonatal", "pédiatrie"], dup="GUTHRIE", former=True)

# ============================ EXERCICES CRÉÉS (Vérifier ma compréhension) ============================
H = lambda a, b, c: [a, b, c]
VF("exercices-thyroide", 1, "thyroide", "explo", ["thyr-explo"], "Une forte dose d’iode stimule l’organification et la synthèse des hormones thyroïdiennes (effet Wolff-Chaikoff).", False,
   "L’effet Wolff-Chaikoff est un BLOCAGE transitoire de l’organification par un excès d’iode. La glande normale s’en échappe en quelques jours.",
   H("Pense à ce que fait l’organisme quand il reçoit trop d’iode d’un coup.", "C’est un mécanisme de protection.", "Le mot « stimule » est-il le bon ?"), ["iode"])
VF("exercices-thyroide", 2, "thyroide", "explo", ["thyr-explo"], "La pilule œstroprogestative augmente les hormones thyroïdiennes totales, sans modifier la fraction libre ni la TSH.", True,
   "Les œstrogènes augmentent la TBG (protéine de transport) : les hormones totales montent, la fraction libre et la TSH restent normales.",
   H("Distingue hormones totales et hormones libres.", "Les œstrogènes agissent sur une protéine de transport.", "La TSH dépend de la fraction libre."), ["TSH"])
VF("exercices-thyroide", 3, "thyroide", "nodules", ["thyr-nodules"], "Un nodule « chaud » à la scintigraphie doit être ponctionné en priorité.", False,
   "Un nodule chaud (autonome, TSH basse) est presque toujours bénin : il ne se ponctionne pas.",
   H("Que signifie « chaud » ?", "Ces nodules freinent la TSH.", "Leur risque est l’hyperthyroïdie, pas le cancer."), ["nodule"])
VF("exercices-thyroide", 4, "thyroide", "cancers", ["thyr-cancers"], "Le cancer médullaire de la thyroïde dérive des cellules C et se surveille par la calcitonine et l’ACE.", True,
   "Les cellules C (parafolliculaires) produisent la calcitonine ; le cancer médullaire se surveille par la calcitonine et l’ACE. Il ne capte pas l’iode.",
   H("Quelles cellules produisent la calcitonine ?", "Elles sont situées entre les follicules.", "Le marqueur suit la cellule d’origine."), ["cancer"])
VF("exercices-thyroide", 5, "thyroide", "thyroidites", ["thyr-thyroidites"], "La thyroïdite de De Quervain se traite par antithyroïdiens de synthèse.", False,
   "Dans une thyroïdite destructrice, la glande ne fabrique pas plus : les ATS sont inutiles. On traite par AINS ou corticoïdes, et bêtabloquants si besoin.",
   H("D’où viennent les hormones en excès ?", "Les ATS bloquent la fabrication.", "La glande fabrique-t-elle davantage ici ?"), ["De Quervain"])
VF("exercices-hyper", 1, "hyper", "diagnostic", ["hyper-diagnostic"], "Une scintigraphie « blanche » chez un patient hyperthyroïdien oriente vers une thyroïdite ou une prise d’hormones exogènes.", True,
   "Fixation nulle = la glande ne produit pas les hormones en excès : thyroïdite destructrice (Tg élevée) ou prise exogène (Tg effondrée).",
   H("Que signifie l’absence de fixation ?", "La glande ne fabrique pas activement.", "Deux grandes situations sont possibles."), ["scintigraphie"])
VF("exercices-hyper", 2, "hyper", "diagnostic", ["hyper-diagnostic"], "Pour confirmer une maladie de Basedow, on dose les anticorps anti-TPO.", False,
   "Le marqueur de Basedow est l’anticorps anti-récepteur de la TSH (TRAK/TSI). Les anti-TPO, peu spécifiques, sont surtout ceux d’Hashimoto.",
   H("Quel est le mécanisme de Basedow ?", "Des anticorps stimulent un récepteur.", "Lequel ?"), ["Basedow", "anticorps"])
VF("exercices-hyper", 3, "hyper", "basedow", ["hyper-basedow"], "Le tabac est un facteur de risque d’orbitopathie basedowienne.", True,
   "Le tabac est le principal facteur de risque modifiable de l’orbitopathie ; l’arrêt du tabac est indispensable.",
   H("Pense aux facteurs modifiables.", "L’iode radioactif aggrave l’orbitopathie surtout chez certains patients.", "Lesquels ?"), ["orbitopathie"])
VF("exercices-hyper", 4, "hyper", "iatrogene", ["hyper-autres"], "L’hyperthyroïdie à l’amiodarone de type 2 se traite principalement par corticoïdes.", True,
   "Le type 2 est une thyroïdite destructrice : corticoïdes. Le type 1 (surcharge iodée sur glande malade) se traite par ATS.",
   H("Quel type est une thyroïdite ?", "On traite une thyroïdite par anti-inflammatoires.", "Lesquels ?"), ["amiodarone"])
VF("exercices-hyper", 5, "hyper", "basedow", ["hyper-traitements"], "En cas de fièvre ou de mal de gorge sous ATS, il faut faire une numération sanguine en urgence.", True,
   "C’est la recherche d’une agranulocytose, complication rare mais grave des ATS, qui impose l’arrêt définitif du traitement.",
   H("Pense à la complication la plus grave des ATS.", "Elle touche les globules blancs.", "Elle expose à des infections sévères."), ["ATS"])
VF("exercices-hypo", 1, "hypo", "diagnostic", ["hypo-diagnostic"], "Dans une hypothyroïdie centrale, la TSH est toujours diminuée.", False,
   "La TSH peut être basse, normale, voire un peu élevée (TSH peu active) : c’est l’association T4L basse + TSH non élevée de façon appropriée qui oriente.",
   H("Le mot « toujours » est souvent suspect.", "L’hypophyse malade peut encore sécréter un peu de TSH.", "Que vaut la TSH par rapport à une T4L basse ?"), ["hypothyroïdie centrale"])
VF("exercices-hypo", 2, "hypo", "diagnostic", ["hypo-diagnostic"], "En Belgique, la première cause d’hypothyroïdie de l’adulte est la thyroïdite d’Hashimoto.", True,
   "La cause auto-immune (Hashimoto) est la plus fréquente dans les pays sans carence iodée sévère ; la carence iodée reste la 1re cause dans le monde.",
   H("Pense à la cause la plus fréquente dans un pays bien iodé.", "Elle est auto-immune.", "On la reconnaît aux anticorps anti-TPO."), ["Hashimoto"])
VF("exercices-hypo", 3, "hypo", "traitement", ["hypo-traitement"], "La L-thyroxine se prend le matin à jeun, à distance du calcium et du fer.", True,
   "L’absorption est meilleure à jeun et diminuée par le calcium, le fer, certains antiacides et résines : on espace les prises.",
   H("Pense à ce qui gêne l’absorption intestinale.", "Certains minéraux se lient à la L-thyroxine.", "Le moment de la prise compte."), ["L-thyroxine"])
VF("exercices-hypo", 4, "hypo", "traitement", ["hypo-grossesse"], "Une femme traitée par L-thyroxine doit augmenter sa dose seulement à la fin du premier trimestre de grossesse.", False,
   "L’augmentation (environ 20 à 30 %, soit deux comprimés de plus par semaine) se fait dès le test de grossesse positif, car le fœtus dépend de la T4 maternelle au 1er trimestre.",
   H("Quand le cerveau du fœtus dépend-il le plus de la mère ?", "Sa propre thyroïde ne fonctionne pas encore au début.", "Faut-il attendre ?"), ["grossesse"])
VF("exercices-hypo", 5, "hypo", "congenitale", ["hypo-congenitale"], "Devant un dépistage néonatal positif, on attend l’échographie avant de commencer la L-thyroxine.", False,
   "On convoque l’enfant en urgence, on prélève pour confirmer, puis on traite immédiatement ; l’imagerie précise la cause ensuite.",
   H("Chaque jour compte pour le développement cérébral.", "L’imagerie change-t-elle la décision de traiter ?", "Elle précise seulement la cause."), ["dépistage néonatal", "pédiatrie"])

for name, qs in files.items():
    with open(os.path.join(ROOT, f"{name}.json"), "w", encoding="utf-8") as f:
        json.dump({"source": name, "questions": qs}, f, ensure_ascii=False, indent=2)
print({k: len(v) for k, v in files.items()}, sum(len(v) for v in files.values()))
