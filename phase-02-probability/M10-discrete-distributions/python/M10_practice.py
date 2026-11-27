from math import comb, exp

n, p = 5, 0.2
print("L1: exactly two =", comb(n, 2) * p**2 * (1-p)**(n-2))
print("L1: at least two =", 1 - (1-p)**n - n*p*(1-p)**(n-1))
print("L2: zero calls =", exp(-2))
print("L2: one failure before the second success =", 2 * 0.5**3)
print("L3: two marked =", comb(3, 2) * comb(7, 2) / comb(10, 4))
