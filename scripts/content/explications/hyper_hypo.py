# Cours 2 (Hyperthyroïdie) et 3 (Hypothyroïdie) : compléments rédigés « à valider » pour les questions importées.
# h = 3 indices progressifs ; e = explication ; o = une remarque par proposition (dans l'ordre) ; p = piège (facultatif).

_NN = dict(
    h=["Chaque jour sans hormones compte pour le cerveau du nourrisson.",
       "Faut-il connaître la cause exacte (imagerie) avant de traiter ?",
       "On confirme par une prise de sang, puis on agit sans délai."],
    e="Une TSH très élevée au dépistage néonatal est une urgence : on convoque l'enfant, on prélève pour confirmer (TSH et T4L sériques), puis on commence la L-thyroxine immédiatement, sans attendre l'imagerie, qui précisera la cause plus tard. Chaque jour de retard compte pour le développement cérébral.",
)
_NN_OPTS = ["Non : trop lent.",
            "Non : trop lent.",
            "Insuffisant : le traitement doit commencer tout de suite.",
            "Oui (réponse attendue).",
            "Non : l'imagerie ne doit pas retarder le traitement."]

_ES = dict(
    h=["Le médicament est l'hormone elle-même.",
       "Que se passe-t-il si on en donne trop ?",
       "L'effet indésirable reproduit une maladie thyroïdienne."],
    e="La L-thyroxine est l'hormone naturelle : son effet indésirable principal est le surdosage, c'est-à-dire une hyperthyroïdie iatrogène (palpitations, fibrillation auriculaire, ostéoporose chez le sujet âgé). Leucopénie, hépatite et dysgueusie sont des effets indésirables des antithyroïdiens de synthèse.",
    o=["Non : effet des ATS.",
       "Non : effet des ATS (surtout le PTU).",
       "Oui (réponse attendue).",
       "Non : effet des ATS.",
       "Non."],
)

_BASEDOW_ATS_E = "Deux propositions sont fausses. Au 1er trimestre de grossesse (et en projet de grossesse), on préfère le PTU, car le thiamazole (Strumazol) est associé à un risque de malformations. Et le traitement d'une hypothyroïdie vise une TSH dans les normes, pas une TSH freinée : une TSH basse sous L-thyroxine signe un surdosage. Les autres propositions sont exactes : environ la moitié des patients rechutent après un traitement par ATS, l'amiodarone peut donner une hyperthyroïdie de type 1 (surcharge iodée) ou de type 2 (thyroïdite), et l'hypothyroïdie élève le cholestérol LDL."
_BASEDOW_ATS_H = ["Deux propositions concernent un traitement : l'une pendant la grossesse, l'autre dans l'hypothyroïdie.",
                  "Au 1er trimestre, un des deux ATS est associé à un risque de malformations.",
                  "Sous L-thyroxine, vise-t-on une TSH normale ou freinée ?"]
_BASEDOW_ATS_P = "Une TSH freinée n'est visée que dans certains cancers thyroïdiens à risque de récidive, jamais dans une simple hypothyroïdie."

_PEDIA_H = ["Méfie-toi du mot « toujours » : dans quelle proposition est-il le plus défendable ?",
            "Une hypothyroïdie patente non traitée chez le jeune enfant ralentit la croissance.",
            "Une prise de poids avec une croissance normale oriente rarement vers une hypothyroïdie."]
_PEDIA_A = "Discutable : le retentissement scolaire d'une hypothyroïdie infraclinique n'est pas établi."

EXPL = {
    # ───────────── Hyperthyroïdie : Basedow ─────────────
    "ENDO-2023-05-ADULTE-QCMM-031": dict(
        h=_BASEDOW_ATS_H, e=_BASEDOW_ATS_E, p=_BASEDOW_ATS_P,
        o=["Vrai : environ la moitié des patients.",
           "Faux (réponse attendue) : PTU au 1er trimestre.",
           "Vrai : types 1 et 2.",
           "Vrai : cholestérol LDL élevé.",
           "Faux (réponse attendue) : on vise une TSH normale ; une TSH basse est un surdosage."]),
    "ENDO-ND-ADULTE-QCMM-234": dict(
        h=_BASEDOW_ATS_H, e=_BASEDOW_ATS_E, p=_BASEDOW_ATS_P,
        o=["Vrai : environ la moitié des patients.",
           "Faux (réponse attendue) : PTU au 1er trimestre.",
           "Vrai : types 1 et 2.",
           "Vrai : cholestérol LDL élevé.",
           "Faux (réponse attendue) : on vise une TSH dans les normes, pas une TSH freinée."]),

    # ───────────── Hyperthyroïdie : diagnostic ─────────────
    "ENDO-ND-ADULTE-QCM-226": dict(
        h=["Regarde d'abord la TSH : est-elle freinée, comme dans la plupart des hyperthyroïdies ?",
           "Une TSH non freinée avec des signes d'hyperthyroïdie oriente vers l'hypophyse.",
           "Des céphalées évoquent une masse dans la région de la selle turcique."],
        e="Énoncé incohérent. Dans presque toutes les hyperthyroïdies (Basedow, thyroïdites, prise exogène), la TSH est freinée. Une TSH élevée ou normale avec des signes d'hyperthyroïdie oriente vers un adénome thyréotrope (qui sécrète de la TSH), d'autant plus qu'il y a des céphalées (effet de masse). Dans ce cas, la T4L et la T3L sont élevées : les « T4 et T3 normales » de l'énoncé sont probablement une erreur de retranscription. Aucune correction officielle n'existe.",
        o=["Réponse retenue : seule cause proposée où la TSH n'est pas freinée.",
           "Non : TSH freinée, anticorps anti-récepteur de la TSH positifs.",
           "Non : TSH freinée.",
           "Non : TSH freinée.",
           "Non : TSH freinée (c'est la même maladie que la thyroïdite subaiguë)."]),
    "ENDO-ND-ADULTE-QCM-208": dict(
        h=["Une proposition concerne l'anticorps qui caractérise la maladie de Basedow.",
           "Les anti-TPO sont fréquents dans plusieurs maladies auto-immunes de la thyroïde.",
           "Quel anticorps cible le récepteur de la TSH ?"],
        e="Pour affirmer ou exclure une maladie de Basedow, on dose les anticorps anti-récepteur de la TSH (TRAK, TSI), spécifiques. Les anti-TPO sont présents dans Basedow comme dans Hashimoto et les thyroïdites auto-immunes : ils ne permettent pas d'exclure le diagnostic. Le reste est exact : il s'agit bien d'une hyperthyroïdie ; une Tg basse doit faire rechercher une prise d'hormones exogènes, mais les anticorps anti-Tg peuvent fausser le dosage ; un goitre diffus est habituel dans Basedow, sans être constant.",
        o=["Vrai : TSH effondrée, T4 et T3 élevées.",
           "Vrai : les anti-Tg interfèrent avec le dosage de la Tg.",
           "Vrai le plus souvent : goitre diffus habituel, mais pas constant.",
           "Vrai : une hyperthyroïdie factice est à rechercher.",
           "Faux (réponse attendue) : on dose les anticorps anti-récepteur de la TSH."],
        p="Toujours interpréter une Tg avec le dosage des anticorps anti-Tg."),
    "ENDO-ND-ADULTE-QCM-218": dict(
        h=["Combien de nodules la patiente présente-t-elle ?",
           "Un adénome toxique est un nodule unique.",
           "L'évolution est lente, sans douleur ni fièvre."],
        e="Plusieurs nodules, une hyperthyroïdie qui s'installe progressivement sur des mois, sans douleur : c'est le tableau du goitre multinodulaire toxique. L'adénome toxique est un nodule unique ; De Quervain est douloureux, fébrile et inflammatoire, d'installation rapide. La Tg élevée est compatible avec un goitre. L'énoncé est incertain : le transcripteur doute qu'il s'agisse de la même question, et une proposition « Basedow » semble avoir été fondue dans l'énoncé.",
        o=["Oui (réponse attendue) : nodules multiples, installation progressive.",
           "Non : nodule unique.",
           "Non : douleur, fièvre, syndrome inflammatoire."]),

    # ───────────── Hyperthyroïdie : iatrogène ─────────────
    "ENDO-ND-ADULTE-QCM-211": dict(
        h=["L'amiodarone contient beaucoup d'iode et inhibe la conversion de T4 en T3.",
           "Elle peut donner une hypothyroïdie, ou une hyperthyroïdie par deux mécanismes.",
           "Crée-t-elle des nodules, ou révèle-t-elle une glande déjà malade ?"],
        e="L'amiodarone, très riche en iode, peut donner une hypothyroïdie (effet Wolff-Chaikoff persistant, surtout sur une thyroïdite auto-immune) ou une hyperthyroïdie : type 1 par surcharge iodée sur une glande déjà anormale (goitre multinodulaire, Basedow latent), type 2 par thyroïdite destructrice. Elle inhibe aussi la désiodase : T4L un peu augmentée et T3L un peu diminuée, même chez un patient en euthyroïdie. Elle ne crée pas de goitre multinodulaire : elle peut rendre toxique un goitre qui existait déjà.",
        o=["Vrai : type 1.",
           "Vrai : surtout sur thyroïdite auto-immune.",
           "Faux (réponse attendue) : elle révèle un goitre préexistant, elle ne le crée pas.",
           "Vrai : inhibition de la désiodase.",
           "Vrai : type 2."]),

    # ───────────── Hypothyroïdie congénitale et enfant ─────────────
    "ENDO-2022-05-PEDIA-QCM-900": dict(
        h=_NN["h"],
        e=_NN["e"] + " Note : la première « proposition » est en réalité la fin de l'énoncé, coupée à la retranscription.",
        o=["Fragment de l'énoncé, retranscrit par erreur comme une proposition."] + _NN_OPTS[:3] + ["Oui (réponse attendue).", _NN_OPTS[4]]),
    "ENDO-2025-01-PEDIA-QCM-900": dict(
        h=_NN["h"],
        e=_NN["e"] + " Note : la dernière « proposition » est un commentaire du transcripteur.",
        o=_NN_OPTS + ["Commentaire du transcripteur, pas une proposition."]),
    "ENDO-ND-PEDIA-QCM-162": dict(h=_NN["h"], e=_NN["e"], o=_NN_OPTS),
    "ENDO-2022-05-PEDIA-QCM-901": dict(
        h=["Méfie-toi des mots « toujours » et « exclure ».",
           "Une proposition est fausse à coup sûr : un goitre peut accompagner une hyperthyroïdie.",
           "Cette question a des réponses différentes selon les années : lis l'explication après avoir répondu."],
        e="Correction discutée. La compilation de mai 2022 retient C (« lors d'une prise de poids importante, il faut toujours vérifier une hypothyroïdie »), mais la couche surlignée de la même compilation et la session de mai 2023 retiennent B (« une hypothyroïdie décompensée chez le petit enfant aura toujours un problème de croissance »). Sur le fond, B est la plus défendable : une hypothyroïdie patente non traitée chez le jeune enfant retentit sur la croissance. C est discutable : une prise de poids avec une croissance normale oriente rarement vers une hypothyroïdie, même si la TSH est souvent dosée en pratique. D est fausse (la maladie de Basedow associe goitre et hyperthyroïdie). Pour A, le retentissement scolaire d'une hypothyroïdie infraclinique n'est pas établi. Aucune correction officielle n'existe (voir la leçon Hypothyroïdie congénitale).",
        o=[_PEDIA_A,
           "La plus défendable sur le fond (retenue en mai 2023 et dans la couche surlignée).",
           "Réponse retenue en mai 2022 (rouge), discutable : « toujours » est excessif.",
           "Faux : la maladie de Basedow associe goitre et hyperthyroïdie.",
           "Proposition non retranscrite."]),
    "ENDO-2023-05-PEDIA-QCM-061": dict(
        h=_PEDIA_H,
        e="La réponse retenue ici est B : une hypothyroïdie patente (TSH élevée, T4 basse) non traitée chez le jeune enfant retentit sur la croissance. C'est la plus défendable sur le fond. Correction discutée : la même question a la réponse C (« prise de poids, toujours vérifier une hypothyroïdie ») en rouge en mai 2022 et dans la compilation 2016-2021. Or une prise de poids avec une croissance normale oriente rarement vers une hypothyroïdie. Pour A, le retentissement scolaire d'une hypothyroïdie infraclinique n'est pas établi. Aucune correction officielle n'existe.",
        o=[_PEDIA_A,
           "Vrai (réponse attendue) : la plus défendable.",
           "Retenue d'autres années, discutable : « toujours » est excessif."]),
    "ENDO-ND-PEDIA-QCM-161": dict(
        h=_PEDIA_H,
        e="Deux propositions ont été fusionnées à la retranscription : la proposition B contient à la fois « l'hypothyroïdie décompensée aura toujours un problème de croissance » et « lors d'une prise de poids importante, il faut toujours vérifier une hypothyroïdie ». La compilation marquait en rouge la seconde partie, la session de mai 2023 retient la première. Sur le fond, la première est la plus défendable : une hypothyroïdie patente non traitée chez le jeune enfant retentit sur la croissance. Un goitre n'exclut pas une hyperthyroïdie (Basedow). Aucune correction officielle n'existe.",
        o=[_PEDIA_A,
           "Réponse attendue (proposition fusionnée) : sa première partie est la plus défendable.",
           "Faux : la maladie de Basedow associe goitre et hyperthyroïdie."]),

    # ───────────── Hypothyroïdie : diagnostic ─────────────
    "ENDO-2022-05-ADULTE-QCM-037": dict(
        h=["Une proposition porte sur la cause, une sur l'évolution, une sur la gravité, deux sur le traitement.",
           "Pour les deux propositions de traitement, demande-toi si la dose et le moment sont corrects.",
           "Cette question a deux corrections différentes selon les compilations : lis l'explication après avoir répondu."],
        e="Correction discutée. La compilation 2016-2024 retient D (en rouge, avec la mention « pas sûre ») ; la compilation 2016-2025 retient E. Sur le fond, E est la plus défendable comme fausse : chez une femme traitée, on augmente la L-thyroxine dès que la grossesse est confirmée (d'environ 20 à 30 %), et non à la fin du 1er trimestre. D est plutôt exacte : une TSH à 12 sous traitement signe un sous-dosage, corrigé par paliers de 12,5 à 25 µg (valeurs à valider, voir la leçon L-thyroxine). A, B et C sont exactes : la cause la plus fréquente est auto-immune (Hashimoto), une thyroïdite auto-immune peut débuter par une phase d'hyperthyroïdie transitoire, et une hypothyroïdie sévère peut donner une hyponatrémie. Aucune correction officielle n'existe.",
        o=["Vrai : Hashimoto.",
           "Vrai : phase de relargage transitoire possible.",
           "Vrai : hypothyroïdie sévère.",
           "Réponse retenue (rouge, « pas sûre ») : en réalité plutôt exacte, un sous-dosage se corrige par paliers.",
           "Retenue par l'autre compilation, et la plus défendable comme fausse : on augmente dès le début de la grossesse."]),
    "ENDO-ND-ADULTE-QCM-202": dict(
        h=["Une carence en iode prive la thyroïde de sa matière première.",
           "Pense aux conséquences chez l'enfant, chez la femme enceinte et sur le volume de la glande.",
           "Relis la proposition sur la grossesse : le préfixe retranscrit est douteux."],
        e="Correction discutée. Une carence sévère en iode donne une hypothyroïdie, un goitre (souvent euthyroïdien), un retard intellectuel chez l'enfant exposé pendant la grossesse ou la petite enfance, et une hypothyroxinémie chez la femme enceinte. La réponse retenue est B (hyperthyroïdie), car ce n'est pas l'effet direct du manque d'iode. Deux nuances : dans une carence ancienne, des nodules autonomes peuvent apparaître et donner une hyperthyroïdie (goitre multinodulaire toxique), surtout chez la personne âgée ; et si la proposition D disait vraiment « hyperthyroxinémie », c'est elle qui serait fausse. Le transcripteur pensait d'ailleurs à « hypothyroxinémie ». Aucune correction officielle n'existe.",
        o=["Vrai.",
           "Réponse retenue : pas un effet direct, mais possible à long terme par des nodules autonomes.",
           "Vrai : surtout par carence pendant la grossesse et la petite enfance.",
           "Formulation douteuse : « hypothyroxinémie » serait vraie, « hyperthyroxinémie » fausse.",
           "Vrai : goitre souvent euthyroïdien."]),

    # ───────────── Hypothyroïdie : traitement ─────────────
    "ENDO-2024-01-PHARMA-QCM-089": dict(_ES),
    "ENDO-2026-01-PHARMA-QCM-053": dict(_ES),
    "ENDO-ND-PHARMA-QCM-005": dict(_ES),
    "ENDO-2025-01-ADULTE-QCM-032": dict(
        h=["Interprète la TSH par rapport à la norme donnée : où se situe-t-elle ?",
           "Chez une personne très âgée, un léger excès d'hormones est mal toléré (cœur, os, amaigrissement).",
           "Sans thyroïde, arrêter le traitement n'est pas une option ; on ajuste par paliers."],
        e="La TSH est à la limite inférieure de la norme, la T4L et la T3L dans le haut de la norme, et la patiente de 83 ans maigrit : c'est un léger surdosage. Chez le sujet très âgé, on accepte généralement une TSH plus haute que chez l'adulte jeune (valeur cible à préciser avec le cours), car l'excès d'hormones expose à la fibrillation auriculaire et à l'ostéoporose. On diminue donc d'un palier (100 → 75 µg), puis on recontrôle. Insister sur la prise à jeun augmenterait plutôt l'absorption ; un bêtabloquant masquerait le problème ; augmenter la dose aggraverait le surdosage ; arrêter est impossible après une thyroïdectomie totale. La compilation note une hésitation avec A, peu défendable sur le fond.",
        o=["Peu défendable : une prise mieux faite augmenterait l'absorption, donc le surdosage.",
           "Non : traite le symptôme, pas le surdosage.",
           "Non : aggraverait le surdosage.",
           "Oui (réponse attendue) : baisse d'un palier.",
           "Non : sans thyroïde, l'arrêt mène à l'hypothyroïdie."],
        p="Chez le sujet âgé, une TSH à la limite basse de la norme peut déjà correspondre à un surdosage."),
}
