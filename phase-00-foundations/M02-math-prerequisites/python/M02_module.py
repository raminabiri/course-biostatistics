from math import isclose, log2
from statistics import mean

reference, comparison = 24/200, 8/100
x = [3, 5, 10]
table = [[12, 288], [9, 291]]
linear = [80 - 20*t for t in range(4)]
exponential = [80 * .5**t for t in range(4)]
answers = {
    "absolute_points": 100*(reference-comparison),
    "relative_percent": 100*(reference-comparison)/reference,
    "incidence_per_100": 8/160*100,
    "mean": mean(x),
    "sum_of_squares": sum(v**2 for v in x),
    "square_of_sum": sum(x)**2,
    "second_row": sum(table[1]),
    "first_column": sum(row[0] for row in table),
    "final_linear": linear[-1],
    "final_exponential": exponential[-1],
    "log_ratio": log2(exponential[-1]/exponential[0]),
}
expected = (4, 100/3, 5, 6, 134, 324, 300, 21, 20, 10, -3)
assert all(isclose(a, b) for a, b in zip(answers.values(), expected, strict=True))
print(answers)
