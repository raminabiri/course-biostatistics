# =============================================================
# ماژول M05 — شاخص‌های مرکزی و پراکندگی | مسیر Python | حل تمرین‌های عملی
# اجرا از داخل همین پوشه:  python M05_solutions.py
# =============================================================
import numpy as np
import pandas as pd

d = pd.read_csv("../data/M05_lipid.csv")
cols = ["sbp", "ldl", "hscrp"]

# %% ع۱: شاخص‌های مرکزی
print("mean\n", d[cols].mean().round(2))        # 130.19 131.08 3.11
print("median\n", d[cols].median())             # 130.0 136.5 1.75
print("mode cigs:", d["cigs"].mode().tolist())  # [0]

# %% ع۲: پراکندگی  (pandas: ddof=1 پیش‌فرض است، مثل بقیهٔ نرم‌افزارها)
for v in ["sbp", "ldl"]:
    x = d[v]
    print(v, "sd", round(x.std(), 2), "var", round(x.var(), 2),
          "min", x.min(), "max", x.max(), "range", x.max() - x.min())
print("np.std (ddof=0!):", round(np.std(d["ldl"]), 2), " ddof=1:", round(np.std(d["ldl"], ddof=1), 2))

# %% ع۳: ضریب تغییرات
print("CV%\n", (100 * d[cols].std() / d[cols].mean()).round(1))   # 8.7 24.3 143.9

# %% ع۴: SEM و دو بازهٔ «± 2»
sem = d["ldl"].sem()                             # = std / sqrt(n)
print("SEM ldl", round(sem, 2), " SEM sbp", round(d["sbp"].sem(), 2))   # 4.60 1.63
m, s = d["ldl"].mean(), d["ldl"].std()
print("individuals:", round(m - 2 * s, 1), round(m + 2 * s, 1))          # 67.4 194.8
print("mean:", round(m - 2 * sem, 1), round(m + 2 * sem, 1))             # 121.9 140.3

# %% ع۵: خلاصه به تفکیک جنس
print(d.groupby("sex")[["sbp", "ldl", "hdl"]].agg(["count", "mean", "std"]).round(2))

# %% ع۶: hsCRP چوله
x = d["hscrp"]
print("mean", round(x.mean(), 2), "median", x.median(),
      "geo", round(np.exp(np.log(x).mean()), 2))                         # 3.11 1.75 1.85
print("Q1,Q3 default (linear = R type 7):", np.percentile(x, [25, 75]))           # 1.00 3.32
print("Q1,Q3 weibull (= SPSS/Prism):", np.percentile(x, [25, 75], method="weibull"))  # 1.00 3.38

# %% ع۷: دادهٔ پرصفر
smk = d.loc[d["cigs"] > 0, "cigs"]
print("smokers", len(smk), round(100 * (d["cigs"] > 0).mean(), 2), "%")  # 15, 31.25
print("median", smk.median(), "mean", smk.mean())                        # 15, 16
