import csv
from pathlib import Path

from math import comb

path = Path(__file__).resolve().parents[1] / "data" / "M64_response.csv"
with path.open(newline="") as stream:
    row = next(csv.DictReader(stream))
successes, total, prior_a, prior_b = (
    int(row[key]) for key in ("responded", "total", "prior_a", "prior_b")
)
a = prior_a + successes
b = prior_b + total - successes
def cdf(x):
    # For positive integer beta shapes, this CDF equals a binomial tail.
    n = a + b - 1
    return sum(comb(n, k) * x**k * (1 - x)**(n - k) for k in range(a, n + 1))


def quantile(probability):
    low, high = 0.0, 1.0
    for _ in range(50):
        middle = (low + high) / 2
        if cdf(middle) < probability:
            low = middle
        else:
            high = middle
    return (low + high) / 2


lower, upper = quantile(0.025), quantile(0.975)
assert a == 9 and b == 5
assert abs(cdf(lower) - 0.025) < 1e-12
assert abs(cdf(upper) - 0.975) < 1e-12
print(a, b, a / (a + b), lower, upper)
