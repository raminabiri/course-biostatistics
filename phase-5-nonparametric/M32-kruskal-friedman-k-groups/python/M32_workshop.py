from itertools import combinations
from pathlib import Path
import csv
import numpy as np
from scipy import stats

with (Path(__file__).resolve().parents[1]/"data/practice.csv").open() as file:
    rows=list(csv.DictReader(file))
g=[np.array([float(r["value"]) for r in rows if r["design"]=="independent" and int(r["group"])==i]) for i in (1,2,3)]
pairs=list(combinations(range(3),2))
n=np.array([len(x) for x in g])
N=n.sum()
rank=stats.rankdata(np.concatenate(g))
split=np.split(rank,np.cumsum(n)[:-1])
means=np.array([x.mean() for x in split])
ss=sum(np.sum((v-v.mean())**2) for v in split)
def holm(p):
    order=np.argsort(p)
    result=np.empty(len(p))
    result[order]=np.minimum(1,np.maximum.accumulate(np.array(p)[order]*np.arange(len(p),0,-1)))
    return result
pd=[2*stats.norm.sf(abs(means[i]-means[j])/np.sqrt(N*(N+1)/12*(1/n[i]+1/n[j]))) for i,j in pairs]
pc=[2*stats.t.sf(abs(means[i]-means[j])/np.sqrt(ss/(N-3)*(1/n[i]+1/n[j])),N-3) for i,j in pairs]
kw=stats.kruskal(*g)
print("L1:",kw.statistic,kw.pvalue,"Dunn Holm:",holm(pd),"Conover Holm:",holm(pc))
J=sum(np.sum(g[i][:,None]<g[j]) for i,j in pairs)
mu=(N*N-n@n)/4
var=(N*(N-1)*(2*N+5)-np.sum(n*(n-1)*(2*n+5)))/72
print("L2:",J,stats.norm.sf((J-mu)/np.sqrt(var)))
blocked=np.array([float(r["value"]) for r in rows if r["design"]=="blocked"]).reshape(-1,3)
fr=stats.friedmanchisquare(*blocked.T)
n,k=blocked.shape
q=stats.rankdata(np.ptp(blocked,axis=1))
rank=stats.rankdata(blocked,axis=1)
score=q[:,None]*(rank-(k+1)/2)
a=np.sum(score**2)
b=np.sum(score.sum(axis=0)**2)/n
f=(n-1)*b/(a-b)
print("L3:",fr.statistic,fr.pvalue,fr.statistic/(n*(k-1)),f,stats.f.sf(f,k-1,(n-1)*(k-1)))

rank_mean=rank.mean(axis=0)
difference=np.array([abs(rank_mean[i]-rank_mean[j]) for i,j in pairs])
pn=stats.studentized_range.sf(difference/np.sqrt(k*(k+1)/(12*n)),k,np.inf)
df=(n-1)*(k-1)
ms=np.sum((rank-rank_mean)**2)/df
pc=2*stats.t.sf(difference/np.sqrt(2*ms/n),df)
print("L3 Nemenyi:",pn,"blocked Conover Holm:",holm(pc))
