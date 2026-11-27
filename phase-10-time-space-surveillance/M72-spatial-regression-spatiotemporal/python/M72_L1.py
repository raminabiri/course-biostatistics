import csv
with open("data/M72_L1.csv", newline="") as stream:
    rows = list(csv.DictReader(stream))
b = 3/(1-.25)
spatial = (1+.5*b,b,3+.5*b)
last = 10
smooth = []
for row in rows:
    last = .25*int(row["requests"])+.75*last
    smooth.append(last)
signals = [int(row["week"]) for row,value in zip(rows,smooth) if value>13]
assert spatial==(3,4,5) and signals==[4]
print(spatial,smooth,signals)
