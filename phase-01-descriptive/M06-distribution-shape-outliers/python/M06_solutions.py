# =============================================================
# ماژول M06 — شکل توزیع، دادهٔ پرت و تبدیل | مسیر Python | حل تمرین‌های عملی
# اجرا از داخل همین پوشه. نیاز: pandas، numpy، scipy
# =============================================================
import numpy as np
import pandas as pd
from scipy import stats

d = pd.read_csv("../data/M06_icu.csv")


def five(x, method):
    return np.r_[x.min(), np.percentile(x, [25, 50, 75], method=method), x.max()]


# %% ع۱: خلاصهٔ پنج‌عددی
print("lactate weibull (SPSS/Prism):", five(d["lactate"], "weibull"))   # 0.5 1.025 1.6 2.7 6.5
print("lactate linear  (default)   :", five(d["lactate"], "linear"))    # 0.5 1.075 1.6 2.7 6.5
print("sodium weibull:", five(d["sodium"], "weibull"))                  # 124 136 139 142 168

# %% ع۲: چولگی و کشیدگی (pandas = G1/G2؛ scipy فقط با bias=False)
v = ["age", "sodium", "lactate", "los"]
print(pd.DataFrame({"skew": d[v].skew(), "kurt": d[v].kurt()}).round(2).T)
print("scipy default (g1):", round(stats.skew(d["lactate"]), 3),
      " bias=False (G1):", round(stats.skew(d["lactate"], bias=False), 3))


# %% ع۳: حصارهای توکی
def tukey(x, method="weibull"):
    q1, q3 = np.percentile(x, [25, 75], method=method)
    iqr = q3 - q1
    return q1 - 1.5 * iqr, q3 + 1.5 * iqr


lo, hi = tukey(d["lactate"])
print("lactate fences", round(lo, 2), round(hi, 2), sorted(d.loc[d["lactate"] > hi, "lactate"]))  # 5.5 6.5
lo, hi = tukey(d["los"])
print("los fences", lo, hi, sorted(d.loc[d["los"] > hi, "los"]))     # 17 17 20 23 28 41

# %% ع۴: نمرهٔ z و پوشاندن
s = d["sodium"]
z = (s - s.mean()) / s.std()
print("z168", round(z[s == 168].iloc[0], 2), "z124", round(z[s == 124].iloc[0], 2),
      "n|z|>3", (z.abs() > 3).sum())                               # 5.20 -2.72 1
s2 = s[s != 168]
print("z124 without 168:", round((124 - s2.mean()) / s2.std(), 2))  # -3.57

# %% ع۵: میانگین ۵٪ پیراسته (از هر طرف ۵٪)
print("los mean", round(d["los"].mean(), 2), "median", d["los"].median(),
      "trim5", round(stats.trim_mean(d["los"], 0.05), 2))           # 6.55 4 5.52
print("lactate trim5", round(stats.trim_mean(d["lactate"], 0.05), 2))  # 1.88

# %% ع۶: تبدیل لگاریتمی لاکتات
lx = np.log10(d["lactate"])
print("skew log", round(lx.skew(), 2), "mean log", round(lx.mean(), 4), "sd log", round(lx.std(), 4))
gm, gsd = 10 ** lx.mean(), 10 ** lx.std()
print("geo mean", round(gm, 2), "geo sd", round(gsd, 2), "range", round(gm / gsd, 2), round(gm * gsd, 2))
# 0.16  0.2231  0.2610 | 1.67  1.82 | 0.92  3.05

# %% ع۷: تحلیل حساسیت سدیم
for name, x in [("all", s), ("without_168", s2)]:
    print(name, len(x), round(x.mean(), 2), round(x.std(), 2), round(x.skew(), 2))
# all 60 139.13 5.56 2.11 | without_168 59 138.64 4.1 -0.53
