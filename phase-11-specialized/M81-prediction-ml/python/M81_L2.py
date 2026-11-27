import csv
from statistics import mean
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
with open("data/M81_L2.csv") as f:
    rows=list(csv.DictReader(f))
train=[r for r in rows if r["center"]=="A"]
test=[r for r in rows if r["center"]=="B"]
def features(rows):
    return [[int(r["age"]),int(r["visits"])] for r in rows]
y=[int(r["event"]) for r in train]
yt=[int(r["event"]) for r in test]
model=make_pipeline(StandardScaler(),LogisticRegression(C=float("inf"),tol=1e-9))
model.fit(features(train),y)
p=model.predict_proba(features(test))[:,1]
base=mean(y)
def brier(probabilities):
    return mean((a-b)**2 for a,b in zip(probabilities,yt))
assert len(p)==60 and mean(p)<mean(yt)
print(base,mean(yt),mean(p),brier([base]*len(yt)),brier(p))
with open("predictions_Python.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["id","event","predicted"])
    writer.writerows(zip((r["id"] for r in test),yt,p))
