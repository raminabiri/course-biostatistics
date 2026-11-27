import csv
from math import sqrt
from statistics import correlation
with open("data/M75_L2.csv", newline="") as stream:
    x,y,z = zip(*(tuple(map(float,row)) for row in list(csv.reader(stream))[1:]))
r12,r13,r23 = correlation(x,y),correlation(x,z),correlation(y,z)
first = sqrt(r12*r13/r23)
loads = (first,r12/first,r13/first)
assert all(abs(a-b)<1e-10 for a,b in zip(loads,(.8,.7,.6)))
print(loads,[1-a*a for a in loads])
