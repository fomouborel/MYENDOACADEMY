# Cours « Obésité et nutrition » : compléments rédigés « à valider » pour les questions importées.
# h = 3 indices progressifs ; e = explication ; o = une remarque par proposition (dans l'ordre) ; p = piège (facultatif).

_ANDRO_H = ["« Androïde » décrit la répartition des graisses, pas l'aspect masculin.",
            "Quelle mesure simple reflète la graisse abdominale ?",
            "Le seuil de la femme est plus bas que celui de l'homme."]
_ANDRO_E = "L'obésité androïde est une accumulation de graisse abdominale et viscérale, mesurée par le tour de taille. Chez la femme, les archives retiennent un tour de taille supérieur à 88 cm : c'est le seuil de la définition américaine (NCEP-ATP III). Les recommandations européennes (2015) retiennent 80 cm chez la femme et 94 cm chez l'homme. Un IMC supérieur à 40 définit l'obésité de classe 3 ; l'hirsutisme et les « traits masculins » n'ont rien à voir."
_ANDRO_O = ["Non : c'est l'obésité de classe 3, pas la répartition.",
            "Non : sans rapport.",
            "Non : seuil européen de l'homme.",
            "Non : « androïde » décrit la répartition des graisses.",
            "Oui (réponse attendue) : seuil américain chez la femme (80 cm selon les recommandations européennes)."]

_GENET_H = ["Les formes à un seul gène ou syndromiques sont rares.",
            "L'obésité commune résulte de nombreux petits effets génétiques.",
            "Ils s'expriment dans un environnement favorable."]
_GENET_E = "La grande majorité des obésités sont polygéniques : de nombreux gènes, chacun avec un petit effet, augmentent la susceptibilité, et s'expriment dans un environnement favorable (alimentation dense en énergie, sédentarité). Les obésités monogéniques (MC4R, leptine) et syndromiques (Prader-Willi) sont rares. Les perturbateurs endocriniens sont étudiés comme facteurs favorisants, pas comme cause de la plupart des obésités."

_SU_H = ["Un des médicaments stimule la sécrétion d'insuline, hormone du stockage.",
         "Il expose aussi aux hypoglycémies, que le patient corrige en mangeant.",
         "Les autres sont neutres ou font maigrir."]
_SU_E = "Les sulfamidés hypoglycémiants stimulent la sécrétion d'insuline et exposent aux hypoglycémies : ils font prendre du poids. La metformine et les gliptines (inhibiteurs de la DPP-4) sont neutres ; les glifozines (inhibiteurs du SGLT2) et les analogues du GLP-1 font maigrir."

_BAR_COMPL_H = ["Le bypass court-circuite une partie de l'estomac et de l'intestin.",
                "Pense aux carences et à l'arrivée rapide des aliments dans l'intestin.",
                "Une proposition décrit au contraire une complication de l'obésité, que la perte de poids améliore."]

_METAB_BASE_H = ["Le métabolisme de base est l'énergie dépensée au repos.",
                 "Une personne obèse a plus de masse à entretenir, y compris de la masse maigre.",
                 "Sa dépense de repos est-elle plus haute ou plus basse en valeur absolue ?"]

_AMAIGR_E = "Font maigrir : l'hyperthyroïdie, le phéochromocytome, le diabète déséquilibré (glycosurie) et la maladie d'Addison. Font grossir : l'hypothyroïdie, le Cushing, l'insulinome (hypoglycémies répétées, stockage par l'insuline) et l'insuline trop dosée."

EXPL = {
    # ═════════════ Définitions et causes ═════════════
    "ENDO-2022-05-ADULTE-QCM-009": dict(h=_ANDRO_H, e=_ANDRO_E, o=_ANDRO_O),
    "ENDO-2023-05-ADULTE-QCM-024": dict(h=_ANDRO_H, e=_ANDRO_E, o=_ANDRO_O),
    "ENDO-ND-ADULTE-QCM-704": dict(h=_ANDRO_H, e=_ANDRO_E, o=_ANDRO_O),
    "ENDO-2022-05-ADULTE-QCM-010": dict(h=_GENET_H, e=_GENET_E,
        o=["Non : rare.", "Oui (réponse attendue).", "Non : rare.", "Non : la susceptibilité génétique joue presque toujours.", "Non : facteur favorisant étudié, pas la cause principale."]),
    "ENDO-2023-05-ADULTE-QCM-032": dict(h=_GENET_H, e=_GENET_E + " La proposition D a été retranscrite avec un doute.",
        o=["Non : rare.", "Non : rare.", "Oui (réponse attendue).", "Non (proposition retranscrite avec doute).", "Non : facteur favorisant étudié."]),
    "ENDO-ND-ADULTE-QCM-705": dict(
        h=_METAB_BASE_H,
        e="Les personnes obèses ont un métabolisme de base augmenté en valeur absolue : elles ont plus de masse à entretenir, y compris de la masse maigre. Le reste est exact : l'obésité se définit par un IMC de 30 ou plus ; un aliment à haute densité énergétique est riche en graisses et rassasie peu ; la chirurgie bariatrique peut faire entrer un diabète de type 2 en rémission.",
        o=["Vrai.", "Vrai.", "Vrai.", "Faux (réponse attendue) : il est augmenté."]),
    "ENDO-ND-ADULTE-QCMM-708": dict(
        h=["Deux propositions sont fausses : une définition et une idée reçue.",
           "Le surpoids commence à 25, l'obésité à 30.",
           "Le métabolisme de base d'une personne obèse est-il vraiment diminué ?"],
        e="Deux propositions sont fausses. L'obésité se définit par un IMC de 30 ou plus (25 à 29,9 est un surpoids). Et le métabolisme de base est augmenté, pas diminué, chez la personne obèse. Le reste est exact : risque plus élevé de lithiase vésiculaire ; l'efficacité d'un régime dépend de la compliance ; le bypass peut donner un dumping syndrome et une carence en B12.",
        o=["Faux (réponse attendue) : c'est le surpoids.", "Vrai.", "Faux (réponse attendue) : il est augmenté.", "Vrai.", "Vrai."]),
    "ENDO-ND-ADULTE-QCMM-711": dict(
        h=["Deux propositions sont fausses : une définition et une affirmation sur les régimes.",
           "Le surpoids commence à 25, l'obésité à 30.",
           "À long terme, est-ce la composition du régime ou l'adhésion qui compte ?"],
        e="Deux propositions sont fausses. L'obésité se définit par un IMC de 30 ou plus. Et à long terme, un régime pauvre en glucides n'est pas plus efficace qu'un régime pauvre en graisses : c'est l'adhésion qui compte. Le reste est exact : lithiases vésiculaires plus fréquentes, métabolisme de base augmenté, rémission possible du diabète après chirurgie bariatrique.",
        o=["Faux (réponse attendue).", "Vrai.", "Faux (réponse attendue) : résultats comparables à long terme.", "Vrai.", "Vrai."]),

    # ═════════════ Variations de poids endocriniennes ═════════════
    "ENDO-2024-01-ADULTE-QCMM-903": dict(
        h=["Deux maladies font au contraire grossir.",
           "Une maladie ralentit la dépense d'énergie.",
           "Une tumeur provoque des hypoglycémies répétées."],
        e="Le phéochromocytome et la maladie d'Addison font maigrir. Deux propositions sont fausses : l'hypothyroïdie (dépense d'énergie ralentie) et l'insulinome (hypoglycémies corrigées en mangeant, stockage par l'insuline) font grossir. " + _AMAIGR_E,
        o=["Amaigrissement.", "Faux (réponse attendue) : fait grossir.", "Faux (réponse attendue) : fait grossir.", "Amaigrissement."]),
    "ENDO-ND-ADULTE-QCMM-706": dict(
        h=["Deux maladies font grossir.",
           "Une tumeur provoque des hypoglycémies répétées.",
           "Une autre redistribue les graisses et augmente l'appétit."],
        e="Correction discutée sur la forme : la consigne est au singulier (« laquelle »), mais deux réponses sont marquées, toutes deux exactes. L'insulinome et le Cushing font grossir ; le diabète décompensé et le phéochromocytome font maigrir. " + _AMAIGR_E,
        o=["Ne fait pas maigrir (réponse attendue).", "Fait maigrir.", "Fait maigrir.", "Ne fait pas maigrir (réponse attendue)."]),
    "ENDO-ND-ADULTE-QCM-707": dict(
        h=["Quatre propositions accélèrent la dépense d'énergie ou font perdre des calories.",
           "Un cancer thyroïdien modifie-t-il la fonction de la glande ?",
           "Ce cancer évolue lentement, chez un patient en euthyroïdie."],
        e="Le carcinome papillaire de la thyroïde ne fait pas maigrir : il ne modifie pas la fonction thyroïdienne et évolue lentement. L'hyperthyroïdie, l'insuffisance surrénale, le phéochromocytome et le diabète déséquilibré peuvent faire maigrir.",
        o=["Ne fait pas maigrir (réponse attendue).", "Fait maigrir.", "Fait maigrir.", "Fait maigrir.", "Fait maigrir."]),
    "ENDO-ND-ADULTE-QCM-709": dict(
        h=["Quatre propositions font grossir.",
           "Une tumeur sécrète des catécholamines.",
           "Les catécholamines accélèrent-elles ou ralentissent-elles la dépense d'énergie ?"],
        e="Le phéochromocytome fait maigrir : les catécholamines accélèrent la dépense d'énergie. L'hypothyroïdie, l'insulinome, le diabète de type 1 traité de façon trop intensive (hypoglycémies, resucrages) et une tumeur surrénalienne sécrétant du cortisol font grossir.",
        o=["Fait grossir.", "Ne fait pas grossir (réponse attendue).", "Fait grossir.", "Fait grossir.", "Fait grossir."]),

    # ═════════════ Traitement ═════════════
    "ENDO-2023-05-ADULTE-QCM-018": dict(h=_SU_H, e=_SU_E,
        o=["Favorable.", "Défavorable (réponse attendue) : prise de poids.", "Favorable.", "Neutre.", "Neutre."]),
    "ENDO-ND-ADULTE-QCM-702": dict(h=_SU_H, e=_SU_E,
        o=["Neutre.", "Favorable.", "Défavorable (réponse attendue) : prise de poids.", "Neutre.", "Favorable."]),
    "ENDO-ND-ADULTE-QCMM-701": dict(
        h=["Deux médicaments font grossir : l'un stimule l'insuline, l'autre retient l'eau et stocke les graisses.",
           "Les glitazones agissent sur le tissu adipeux.",
           "Les autres sont neutres ou font maigrir."],
        e="Deux médicaments augmentent l'excès de poids : les sulfamidés hypoglycémiants (sécrétion d'insuline, hypoglycémies) et la pioglitazone (rétention d'eau, augmentation de la graisse sous-cutanée). Les gliptines et la metformine sont neutres ; les analogues du GLP-1 font maigrir.",
        o=["Augmente le poids (réponse attendue).", "Augmente le poids (réponse attendue).", "Neutre.", "Neutre.", "Favorable."]),
    "ENDO-2025-01-RADIO-QCM-903": dict(
        h=["Énoncé abrégé : il s'agit vraisemblablement des seuils de prise en charge, notamment médicamenteuse.",
           "Les médicaments de l'obésité sont indiqués à partir d'un IMC de 30, ou de 27 avec complications.",
           "Une proposition descend sous ce seuil."],
        e="Énoncé abrégé (« pour excès de poids »), vraisemblablement les seuils de prise en charge, notamment médicamenteuse. Les traitements de l'obésité s'envisagent à partir d'un IMC de 30, ou de 27 avec une complication liée au poids ; au-delà de 35 ou 40, la chirurgie peut aussi se discuter. Un IMC de 25 à 26,9, même avec des complications, est en dessous de ces seuils.",
        o=["Vrai.", "Vrai : IMC de 27 ou plus avec complications.", "Vrai.", "Faux (réponse attendue) : sous le seuil de 27.", "Vrai."]),
    "ENDO-ND-ADULTE-QCM-710": dict(
        h=["Une proposition contient un calcul : refais-le.",
           "Charge glycémique = index glycémique × quantité de glucides (g) / 100.",
           "Pain : 200 g × 50 % = 100 g de glucides ; fromage blanc : 200 g × 10 % = 20 g."],
        e="La charge glycémique se calcule ainsi : index glycémique × quantité de glucides / 100. Pain : 200 g × 50 % = 100 g de glucides, × 0,75 = 75. Fromage blanc sucré : 200 g × 10 % = 20 g, × 0,50 = 10. Total : 85, et non 95 : la proposition est fausse. Le reste est exact : 40 à 50 % de glucides, édulcorants pratiquement sans calories aux doses utilisées, définition de l'index glycémique, l'alcool compte dans les calories.",
        o=["Vrai.", "Vrai en pratique : apport calorique négligeable aux doses utilisées.", "Vrai.", "Faux (réponse attendue) : le résultat est 85.", "Vrai : 7 kcal par gramme."]),
    "ENDO-ND-ADULTE-QCM-601": dict(
        h=_BAR_COMPL_H,
        e="Le bypass gastrique peut donner une ostéopénie (malabsorption du calcium et de la vitamine D), une carence en vitamine B12, des hypoglycémies après les repas et une lithiase vésiculaire (perte de poids rapide). Le syndrome d'apnées du sommeil, au contraire, est une complication de l'obésité que la perte de poids améliore.",
        o=["Ne fait pas partie (réponse attendue) : s'améliore.", "Complication.", "Complication.", "Complication.", "Complication."]),
    "ENDO-ND-ADULTE-QCM-603": dict(
        h=_BAR_COMPL_H,
        e="Le bypass gastrique peut donner un dumping syndrome, une carence en vitamine B12, une lithiase vésiculaire et une ostéoporose (malabsorption du calcium et de la vitamine D). L'insuffisance hépatique ne fait pas partie des complications attendues : la perte de poids améliore au contraire la stéatose hépatique.",
        o=["Ne fait pas partie (réponse attendue).", "Complication.", "Complication.", "Complication.", "Complication."]),
    "ENDO-ND-ADULTE-QCMM-602": dict(
        h=["On raisonne en IMC, pas en poids.",
           "Un trouble du comportement alimentaire sévère est une contre-indication.",
           "Cette question a une correction discutée : lis l'explication après avoir répondu."],
        e="Correction discutée. La compilation retient « IMC de plus de 35 avec apnées du sommeil et diabète mal contrôlé » et « IMC de plus de 40 », conformément aux critères historiques de 1991. Depuis 2022, les sociétés savantes (ASMBS et IFSO) recommandent la chirurgie dès un IMC de 35, même sans complication : « IMC de plus de 35 » serait aussi une indication. Le poids seul (« plus de 100 kg ») n'est pas un critère, et une boulimie sévère est une contre-indication tant qu'elle n'est pas stabilisée.",
        o=["Non : on raisonne en IMC.",
           "Indication depuis 2022 (non retenue par la compilation).",
           "Oui (réponse attendue).",
           "Oui (réponse attendue).",
           "Non : un trouble du comportement alimentaire sévère contre-indique la chirurgie."]),

    # ═════════════ Syndrome métabolique ═════════════
    "ENDO-ND-ADULTE-QCM-547": dict(
        h=["Méfie-toi du mot « toujours ».",
           "Le diagnostic repose sur 3 critères parmi 5.",
           "Le HDL-cholestérol est-il augmenté ou diminué ?"],
        e="Le syndrome métabolique se définit par au moins 3 critères parmi 5 : tour de taille, triglycérides élevés, HDL-cholestérol bas, pression artérielle élevée, glycémie à jeun élevée. Un des critères est donc une diminution du HDL. Il n'est pas « toujours » associé à une HTA ou à une stéatose ; le score va de 0 à 5 ; et la relation avec l'insulinorésistance est directe.",
        o=["Faux : 3 critères sur 5 suffisent.", "Faux : fréquente, pas constante.", "Faux : de 0 à 5.", "Vrai (réponse attendue).", "Faux : relation directe."]),
    "ENDO-ND-ADULTE-QCM-624": dict(
        h=["Une proposition donne une mauvaise définition de l'obésité.",
           "Le surpoids commence à 25.",
           "À partir de quel IMC parle-t-on d'obésité ?"],
        e="L'obésité se définit par un IMC de 30 ou plus (25 à 29,9 est un surpoids). Le reste est exact : un syndrome métabolique à 5 sur 5 comporte plus d'insulinorésistance qu'à 3 sur 5 ; un HDL inférieur à 40 mg/dL chez l'homme est un critère ; la chirurgie bariatrique donne de bons résultats en cas de diabète associé à une obésité importante. La 5e proposition n'a pas été retranscrite.",
        o=["Vrai.", "Vrai : critère du syndrome métabolique.", "Faux (réponse attendue) : 30 ou plus.", "Vrai.", "Proposition non retranscrite."]),
    "ENDO-ND-ADULTE-QCM-626": dict(
        h=["Méfie-toi du mot « toujours ».",
           "Les atteintes rénales du syndrome métabolique sont-elles constantes ?",
           "Pense à la différence entre microalbuminurie et protéinurie franche."],
        e="Un syndrome métabolique à 5 sur 5 comporte un HDL bas (moins de 40 mg/dL chez l'homme), une insulinorésistance plus importante qu'à 3 sur 5, souvent une hyperferritinémie métabolique, et peut s'associer à des ovaires polykystiques. Il n'y a pas « toujours » de protéinurie franche : une microalbuminurie est possible, mais pas constante.",
        o=["Vrai.", "Vrai.", "Vrai : hyperferritinémie métabolique.", "Faux (réponse attendue).", "Vrai : insulinorésistance commune."]),
    "ENDO-ND-ADULTE-QCM-569": dict(
        h=["Chez le diabétique et en cas de syndrome métabolique, l'ischémie est souvent silencieuse.",
           "Les lésions coronaires sont plus diffuses et récidivent plus souvent.",
           "Cette question a une correction discutée : lis l'explication après avoir répondu."],
        e="Correction discutée. Chez les coronariens qui ont un syndrome métabolique, l'ischémie est souvent asymptomatique (silencieuse), les lésions sont plus diffuses et le risque de resténose de stent est plus élevé. La proposition retenue comme fausse, « épreuve de cycloergomètre asymptomatique », est ambiguë : le patient peut ne rien ressentir pendant l'effort, mais l'épreuve peut révéler l'ischémie (modifications de l'électrocardiogramme). La proposition sur l'absence de différence entre les sexes vient du cours ; elle n'est pas détaillée ici.",
        o=["Vrai selon le cours.", "Vrai : ischémie silencieuse.", "Réponse retenue, formulation ambiguë.", "Vrai.", "Vrai."]),
    "ENDO-ND-ADULTE-QCMM-619": dict(
        h=["Le mode de vie vient toujours en premier.",
           "Une classe d'hypolipémiants n'est pas un traitement de première intention.",
           "Cette question a une correction discutée : lis l'explication après avoir répondu."],
        e="Correction discutée. Devant un syndrome métabolique complet avec diabète de type 2 et obésité, on commence par l'activité physique et un régime hypocalorique ; une statine se discute selon le risque cardiovasculaire. Un fibrate n'est pas un traitement de première intention (réservé aux hypertriglycéridémies importantes). La compilation retient aussi le biguanide comme à ne pas débuter d'emblée. Or la metformine est le traitement habituel de première intention du diabète de type 2 en l'absence d'insuffisance rénale : la réponse est discutable, et la consigne est au singulier.",
        o=["À faire.", "À faire.", "À discuter selon le risque cardiovasculaire.", "Pas d'emblée (réponse attendue).", "Retenu par la compilation, discutable : traitement de première intention habituel."]),
}
