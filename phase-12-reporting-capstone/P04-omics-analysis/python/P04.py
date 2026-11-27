import csv
with open("data/P04.csv") as f:
    rows=list(csv.DictReader(f))
with open("data/composition.csv") as f:
    next(f)
    a,b=[[int(x) for x in row[1:]] for row in csv.reader(f)]
values=[float(r["p"]) for r in rows]
order=sorted(range(len(values)),key=values.__getitem__)
q=[1.0]*len(values)
floor=1
for rank,i in reversed(list(enumerate(order,1))):
    floor=min(floor,len(values)*values[i]/rank)
    q[i]=floor
selected=[r["gene"] for r,v in zip(rows,q) if v<=.05 and abs(float(r["log2fc"]))>=1]
distance=sum(abs(x-y) for x,y in zip(a,b))/(sum(a)+sum(b))
assert selected==["G01","G02"] and distance==.25
print(q,selected,distance)
