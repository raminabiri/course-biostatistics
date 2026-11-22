# =============================================================
# ماژول M07 — جدول فراوانی و جدول توافقی | مسیر Python | حل تمرین‌های عملی
# اجرا از داخل همین پوشه.
# =============================================================
import pandas as pd

d = pd.read_csv("../data/M07_survey.csv")
d["smoking"] = pd.Categorical(d["smoking"], ["never", "former", "current"])
d["age_group"] = d["age_group"].map({1: "18-39", 2: "40-59", 3: "60+"})

# %% ع۱: جدول فراوانی سیگار
n = d["smoking"].value_counts(sort=False)
print(pd.DataFrame({"n": n, "pct": (100 * n / n.sum()).round(1)}))

# %% ع۲: تحصیلات با درصد تجمعی
n = d["education"].value_counts().sort_index()
pct = 100 * n / n.sum()
print(pd.DataFrame({"n": n, "pct": pct.round(1), "cum": pct.cumsum().round(1)}))

# %% ع۳: درصد و درصد معتبر
n = d["flu_vacc"].value_counts(dropna=False)
print(pd.DataFrame({"n": n, "pct": (100 * n / len(d)).round(1)}))
print("valid %:", (100 * d["flu_vacc"].value_counts(normalize=True)).round(1).to_dict())

# %% ع۴: جنس × سیگار
print(pd.crosstab(d["sex"], d["smoking"], margins=True))
print((100 * pd.crosstab(d["sex"], d["smoking"], normalize="index")).round(1))

# %% ع۵: گروه سنی × واکسن
print(pd.crosstab(d["age_group"], d["flu_vacc"]))
print("row % yes:", (100 * pd.crosstab(d["age_group"], d["flu_vacc"], normalize="index")["yes"]).round(1).to_dict())
print("col % yes:", (100 * pd.crosstab(d["age_group"], d["flu_vacc"], normalize="columns")["yes"]).round(1).to_dict())

# %% ع۶: سلامت ضعیف (۴–۵)
d["poor_health"] = (d["self_health"] >= 4).astype("Int64").where(d["self_health"].notna())
print(d["poor_health"].value_counts().to_dict(), round(100 * d["poor_health"].mean(), 1))   # {0:143,1:52} 26.7
print((100 * pd.crosstab(d["region"], d["poor_health"], normalize="index")[1]).round(1).to_dict())  # rural 24.7, urban 28.0

# %% ع۷: مقایسهٔ سیگار فعلی
p = d.assign(cur=d["smoking"] == "current").groupby("sex")["cur"].mean()
print("pct:", (100 * p).round(1).to_dict())                           # F 8.6  M 34.6
print("diff pp:", round(100 * (p["M"] - p["F"]), 1), " ratio:", round(p["M"] / p["F"], 2))   # 26.0  4.02
odds = p / (1 - p)
print("odds ratio:", round(odds["M"] / odds["F"], 2))                 # 5.62
