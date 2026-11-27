import csv
with open("data/M79_L1.csv") as f:
    p=[float(r["p"]) for r in csv.DictReader(f)]
order=sorted(range(len(p)),key=p.__getitem__)
q=[0.0]*len(p)
minimum=1
for rank in range(len(p),0,-1):
    i=order[rank-1]
    minimum=min(minimum,len(p)*p[i]/rank)
    q[i]=minimum
assert abs(q[0]-.004)<1e-10 and sum(x<=.05 for x in q)==2
print(q)
