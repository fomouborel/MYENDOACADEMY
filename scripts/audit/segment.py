import re, json, sys
S=sys.argv[1]
# (file, start_line, end_line, session, section, discipline, teacher, numbered_reset)
SECT = [
 ("A",2,405,"2024-01","Janvier 2024","MIXTE",None),
 ("A",406,457,"2024-01","Janvier 2024 – questions Lysy non numérotées","PEDIA","Lysy"),
 ("A",458,1018,"2023-05","Mai 2023","MIXTE",None),
 ("A",1019,1236,"2022-05","Mai 2022 – Adulte","ADULTE",None),
 ("A",1237,1373,"2022-05","Mai 2022 – Pédiatrie","PEDIA","Lysy"),
 ("A",1374,1387,"2022-05","Mai 2022 – Radiologie","RADIO",None),
 ("A",1388,1388,"2022-05","Mai 2022 – Anapath","ANAPATH","Marbaix"),
 ("A",1389,1424,"2022-05","Mai 2022 – Pharmacologie","PHARMA","Horsmans"),
 ("A",1429,2212,"2016-2021","Maiter adulte – Diabète","ADULTE","Maiter"),
 ("A",2213,2444,"2016-2021","Maiter adulte – Thyroïde","ADULTE","Maiter"),
 ("A",2445,2630,"2016-2021","Maiter adulte – Hypophyse","ADULTE","Maiter"),
 ("A",2631,2782,"2016-2021","Maiter adulte – Surrénale","ADULTE","Maiter"),
 ("A",2783,2846,"2016-2021","Maiter adulte – Hypogonadisme/gynécomastie","ADULTE","Maiter"),
 ("A",2847,2886,"2016-2021","Hermans – Syndrome métabolique","ADULTE","Hermans"),
 ("A",2887,2905,"2016-2021","Navez – Chirurgie bariatrique","ADULTE","Navez"),
 ("A",2906,2975,"2016-2021","Thissen – Obésité","ADULTE","Thissen"),
 ("A",2977,3014,"2016-2021","Lysy – Croissance","PEDIA","Lysy"),
 ("A",3015,3035,"2016-2021","Lysy – Puberté","PEDIA","Lysy"),
 ("A",3036,3062,"2016-2021","Lysy – Diabète","PEDIA","Lysy"),
 ("A",3063,3078,"2016-2021","Lysy – Thyroïde","PEDIA","Lysy"),
 ("A",3079,3532,"2016-2021","Beauloye (ancien titulaire) – Pédiatrie","PEDIA","Beauloye"),
 ("A",3534,3590,"2016-2021","Marbaix – Anapath pancréas","ANAPATH","Marbaix"),
 ("A",3591,3612,"2016-2021","Marbaix – Anapath hypophyse","ANAPATH","Marbaix"),
 ("A",3613,3712,"2016-2021","Marbaix – Anapath thyroïde/parathyroïdes/surrénales","ANAPATH","Marbaix"),
 ("A",3713,3910,"2016-2021","Duprez + Coche – Imagerie","RADIO","Duprez/Coche"),
 ("A",3912,4005,"2016-2021","Horsmans – Pharmaco hormones","PHARMA","Horsmans"),
 ("A",4006,4025,"2016-2021","Horsmans – Pharmaco hématopoïèse","PHARMA","Horsmans"),
 ("A",4026,4032,"2016-2021","Horsmans – Pharmaco hypolipémiants","PHARMA","Horsmans"),
 ("A",4033,4058,"2016-2021","Horsmans – Pharmaco immunosuppresseurs","PHARMA","Horsmans"),
 ("A",4059,4074,"2016-2021","Horsmans – Pharmaco phosphocalcique","PHARMA","Horsmans"),
 ("A",4075,4097,"2016-2021","Horsmans – Pharmaco hormones sexuelles","PHARMA","Horsmans"),
 ("E",10,572,"2025-01","Janvier 2025","MIXTE",None),
 ("G",15,134,"2026-01","Janvier 2026 – Preumont","ADULTE","Preumont"),
 ("G",135,142,"2026-01","Janvier 2026 – Loumaye","ADULTE","Loumaye"),
 ("G",143,306,"2026-01","Janvier 2026 – Alexopoulou (+ vrac adulte)","ADULTE","Alexopoulou"),
 ("G",307,382,"2026-01","Janvier 2026 – Lysy","PEDIA","Lysy"),
 ("G",383,407,"2026-01","Janvier 2026 – Radiologie","RADIO",None),
 ("G",408,422,"2026-01","Janvier 2026 – Anapath","ANAPATH",None),
 ("G",423,512,"2026-01","Janvier 2026 – Pharmacologie","PHARMA","Horsmans"),
]
FILES={"A":"A_comp2016-2024","E":"E_retr2025-01","G":"G_retr2026-01"}
PDF={"A":"#Compilation endocrino 2016-2024.pdf","E":"02_Retranscription Janvier 2025 - Secteur Endocrinologie.pdf","G":"Retranscription – Janvier 2026 _ Secteur Endocrinologie (1).pdf"}
lines={k:open(f"{S}/cmp2/{v}.txt").read().replace("\u200b","").replace("\u00a0"," ").split("\n") for k,v in FILES.items()}
FORCE={("A",x) for x in [2652,3002,3616,3626,3640,3731,3800,3809,3815,3821,3826,3831,3838,3844,3849,3851,3856,3919,4013]}
def clean(s): return s.replace("«","").replace("»","").replace("⟦C8db3e2:","").replace("⟦Ca02b93:","").replace("⟦C38761d:","").replace("⟦G:","").replace("⟦B:","").replace("⟦C385623:","").strip()
OPT=re.compile(r"^\s*«?\s*([A-Ja-j]\s*[.)\];:]|[-•●]|\d\s*[.)]\s*[A-Za-zÀ-ÿ]|[A-J]\s*«)")
KW=re.compile(r"\?|:\s*$|fausse|vraie|sauf|concernant|à propos|a propos|quel|qu.est|que faire|diagnostic|indiqu|cochez|choisi|parmi|lequel|laquelle|caractéris|cause|tous ces|toutes ces|association|effet", re.I)
NUM=re.compile(r"^\s*«?\s*(\d{1,3})\s*(?:[.\-)]|\s)\s*(?:\d\s*)?([«A-Za-zÀ-ÿ“\"(\[].*)$")
out=[]
MANUAL={
 ("A","Janvier 2024 – questions Lysy non numérotées"):[406,418,426,431,438,444,449,454],
 ("A","Mai 2022 – Pédiatrie"):[1238,1244,1251,1257,1265,1275,1281,1286,1292,1300,1308,1313,1321,1328,1334,1340,1348,1355,1357,1366],
 ("A","Mai 2022 – Radiologie"):[1375,1381],
 ("A","Mai 2022 – Anapath"):[],
 ("A","Mai 2022 – Pharmacologie"):[1390,1395,1401,1408,1414,1419],
 ("A","Beauloye (ancien titulaire) – Pédiatrie"):[3080,3088,3092,3098,3104,3106,3107,3115,3117,3119,3122,3125,3130,3133,3157,3169,3172,3178,3184,3191,3196,3197,3204,3211,3219,3226,3230,3232,3239,3245,3247,3249,3251,3252,3254,3260,3265,3271,3272,3279,3287,3290,3294,3296,3304,3312,3319,3321,3324,3325,3326,3334,3342,3344,3347,3355,3361,3370,3374,3380,3388,3394,3399,3401,3404,3410,3418,3424,3430,3449,3464,3471,3474,3477,3481,3484,3492,3499,3508,3514,3520,3526],
}
for f,a,b,sess,sect,disc,teach in SECT:
    L=lines[f]; page=None
    # find page at line a
    for i in range(a-1,-1,-1):
        m=re.match(r"=====PAGE (\d+)",L[i]); 
        if m: page=int(m.group(1)); break
    last=0; cur=None; stem_open=False; man=MANUAL.get((f,sect))
    for i in range(a-1,b):
        raw=L[i]
        m=re.match(r"=====PAGE (\d+)",raw)
        if m: page=int(m.group(1)); continue
        t=clean(raw)
        if not t: continue
        if man is not None:
            if i+1 in man:
                cur={"src":f,"pdf":PDF[f],"session":sess,"section":sect,"disc":disc,"teacher":teach,"page":page,"num":None,"stem":[t],"lines":[],"marked":[],"line":i+1}
                out.append(cur)
                if "«" in raw: cur["marked"].append(t)
            elif cur is not None:
                cur["lines"].append(t)
                if "«" in raw: cur["marked"].append(t)
            continue
        mn=NUM.match(raw)
        is_start=False; num=None
        mx=re.match(r"^\s*«?\s*(\d{1,3})\s*[.)\-]\s*(\S.*)$",raw)
        if mx and int(mx.group(1))==last+1 and last>0 and not re.match(r"^\d+\s*[’']",clean(mx.group(2))):
            mn=mx
        if mn:
            n=int(mn.group(1)); rest=clean(mn.group(2))
            if (n>=last and n-last<=40 and not (n<=6 and last>=1 and len(rest)<70 and not KW.search(rest))) or (len(rest)>=25 and KW.search(rest) and n>last-1):
                is_start=True; num=n
            elif last==0:
                is_start=True; num=n
            elif cur is not None and len(cur["lines"])>=3 and len(rest)>=12 and KW.search(rest) and n!=last:
                is_start=True; num=n
        if not is_start and re.match(r"^\s*-\s*\S",raw) and t.endswith("?") and len(t)>30 and not (cur and stem_open):
            is_start=True; t=t.lstrip("- ")
        if not is_start and not OPT.match(raw) and not (cur and stem_open):
            if ((len(t)>=22 and KW.search(t)) or (len(t)>=8 and re.search(r"[:?]\s*$",t))) and not re.match(r"^(Prévu|Conseils|Horsman|Anapath 100|Thissen 1|Lysy :|N’hésitez|QCM à|\[Sorry|Je crois|->|=>|Propositions pour)",t):
                is_start=True
        if (f,i+1) in FORCE:
            is_start=True
            mm=re.match(r"^\s*(\d{1,3})",raw); num=int(mm.group(1)) if mm else None
            mn=re.match(r"^\s*\d{1,3}\s*[.)]?\s*(.*)$",raw); mn=re.match(r"^(\s*)(.*)$",clean(mn.group(1)))
        if is_start:
            cur={"src":f,"pdf":PDF[f],"session":sess,"section":sect,"disc":disc,"teacher":teach,"page":page,"num":num,"stem":[t if num is None else clean(mn.group(2))],"lines":[],"marked":[],"line":i+1}
            out.append(cur); stem_open=True
            if num is not None: last=num
            if "«" in raw: cur["marked"].append(t)
            continue
        if cur is None: continue
        if stem_open and len(clean(L[i-1]))>=75 and not OPT.match(raw):
            cur["stem"].append(t)
        else:
            stem_open=False; cur["lines"].append(t)
        if "«" in raw: cur["marked"].append(t)
json.dump(out,open(f"{S}/inv_raw.json","w"),ensure_ascii=False,indent=0)
print(len(out))
from collections import Counter
print(Counter(q["session"] for q in out))
