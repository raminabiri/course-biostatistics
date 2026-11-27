from math import ceil, log
from statistics import NormalDist
z = NormalDist().inv_cdf
events = (z(.975)+z(.8))**2/(.25*log(.75)**2)
total = ceil(ceil(events)/.4)
equivalence = 2*(10/3)**2*(z(.95)+z(.9))**2
print(events,total,equivalence)
assert (ceil(events),total,ceil(equivalence))==(380,950,191)
