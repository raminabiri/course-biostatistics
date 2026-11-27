import csv
from collections import Counter
from math import comb
from pathlib import Path
from statistics import median
from scipy import stats

def ks_permutation(a, b):
    n1, n2 = len(a),len(b)
    left,right = Counter(a),Counter(b)
    blocks = sorted(left.keys() | right.keys())
    i = j = gap = 0
    for value in blocks:
        i += left[value]
        j += right[value]
        gap = max(gap,abs(i*n2-j*n1))
    if not gap:
        return 0,1.0
    paths = {0:1}
    total = 0
    for value in blocks:
        m = left[value]+right[value]
        total += m
        new = Counter()
        for used, count in paths.items():
            for take in range(m+1):
                x = used+take
                y = total-x
                if x<=n1 and y<=n2 and abs(x*n2-y*n1)<gap:
                    new[x] += count*comb(m,take)
        paths = new
    all_paths = comb(n1+n2,n1)
    return gap/(n1*n2),(all_paths-paths.get(n1,0))/all_paths

def report(file, method):
    path = Path(__file__).resolve().parents[1]/"data"/file
    with path.open(newline="",encoding="utf-8") as source:
        rows = list(csv.DictReader(source))
    a,b = ([float(r["value"]) for r in rows if r["group"]==g] for g in "AB")
    w = stats.mannwhitneyu(a,b,method=method,use_continuity=False)
    D,p = ks_permutation(a,b)
    cutoff = median(a+b)
    up1,up2 = sum(x>cutoff for x in a),sum(x>cutoff for x in b)
    table = [[up1,len(a)-up1],[up2,len(b)-up2]]
    print(file)
    print("L1: U of A and P:",w.statistic,w.pvalue)
    print("L2: conditional KS:",D,p)
    print("L3: HL, median table and Fisher P:",median([x-y for x in a for y in b]),table,
          stats.fisher_exact(table).pvalue)

report("practice.csv","exact")
report("extended.csv","asymptotic")
