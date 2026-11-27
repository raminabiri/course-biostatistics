from math import comb, exp, factorial, isclose
p = (comb(5,2)*.2**2*.8**3, exp(-2)*2**3/factorial(3),
     comb(4,1)*.4**2*.6**3, comb(5,2)*comb(15,2)/comb(20,4))
assert all(isclose(a,b) for a,b in zip(p,(.2048,.1804470443154836,.13824,1050/4845)))
print(p)
