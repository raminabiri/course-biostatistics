from collections import Counter
from csv import DictReader
from math import factorial, prod
from pathlib import Path

import numpy as np
from scipy import stats


def conditional_exact_3x3(observed):
    """Enumerate tables with the margins of a small, fixed 3-by-3 table."""
    row1, row2, _ = observed.sum(axis=1)
    columns = observed.sum(axis=0)

    def row_options(total, capacities):
        for a in range(min(total, capacities[0]) + 1):
            for b in range(min(total - a, capacities[1]) + 1):
                c = total - a - b
                if c <= capacities[2]:
                    yield np.array([a, b, c])

    def factorial_product(table):
        return prod(factorial(value) for value in table.flat)

    threshold = factorial_product(observed)
    weights = []
    extreme_weights = []
    for first in row_options(row1, columns):
        for second in row_options(row2, columns - first):
            candidate = np.array([first, second, columns - first - second])
            denominator = factorial_product(candidate)
            weight = 1 / denominator
            weights.append(weight)
            if denominator >= threshold:
                extreme_weights.append(weight)
    return sum(extreme_weights) / sum(weights)


with (Path(__file__).resolve().parents[1] / 'data/M35_practice.csv').open() as stream:
    rows = list(DictReader(stream))
assert len(rows) == len({row['id'] for row in rows}) == 150
counts = Counter((row['group'], row['response']) for row in rows)
large = np.array([[counts[g, r] for r in ('yes', 'partial', 'no')] for g in 'ABC'])
binary = np.column_stack([large[:2, 0], large[:2, 1:].sum(axis=1)])
pearson = stats.chi2_contingency(binary, correction=False)
yates = stats.chi2_contingency(binary, correction=True)
z = (30/50 - 20/50) / np.sqrt(.5*.5*(1/50 + 1/50))
print('L1:', pearson.statistic, pearson.pvalue, yates.statistic, yates.pvalue, z)
fisher = stats.fisher_exact(binary)
barnard = stats.barnard_exact(binary.T)
print('L2:', fisher.statistic, fisher.pvalue, barnard.pvalue)
result = stats.chi2_contingency(large, correction=False)
g = stats.chi2_contingency(large, correction=False, lambda_='log-likelihood')
expected = result.expected_freq
adjusted = (large - expected) / np.sqrt(
    expected * (1 - large.sum(axis=0)/large.sum()) * (1 - large.sum(axis=1)/large.sum())[:, None]
)
small = np.array([[3, 1, 0], [0, 2, 2], [1, 0, 3]])
ffh = conditional_exact_3x3(small)
print('L3:', result.statistic, result.pvalue, g.statistic, g.pvalue, adjusted[0, 0], ffh)
assert np.isclose(pearson.statistic, z*z)
assert np.isclose(ffh, 1/11)
