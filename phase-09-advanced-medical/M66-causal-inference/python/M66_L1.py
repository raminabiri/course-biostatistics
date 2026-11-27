import csv
with open("data/M66_L1.csv", newline="") as stream:
    rows = [tuple(map(int, row)) for row in list(csv.reader(stream))[1:]]
nt, nc, yt, yc = zip(*(row[1:] for row in rows))
e = [t/(t+c) for t,c in zip(nt,nc)]
def weighted(scores, weights):
    return sum(y*w for y,w in zip(scores,weights))/sum(weights)
raw = weighted(yt,nt)-weighted(yc,nc)
adjusted = weighted(yt,[t/p for t,p in zip(nt,e)])-weighted(yc,[c/(1-p) for c,p in zip(nc,e)])
assert (raw,adjusted)==(-2,4)
print(raw,adjusted,2/.5,(16-10)-(12-9))
