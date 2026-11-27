from collections import Counter
from itertools import product
from math import isclose,sqrt
from statistics import mean,pstdev
def means(n):
    return [mean(values) for values in product((0,4),repeat=n)]
a,b=means(2),means(4)
assert Counter(a)=={0:1,2:2,4:1} and b.count(2)==6
assert isclose(pstdev(a),sqrt(2)) and pstdev(b)==1
print(Counter(a),pstdev(a),pstdev(b),b.count(2)/len(b))
