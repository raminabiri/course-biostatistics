<div dir="rtl">

# M06 در Python — چارک، چولگی، مقادیر دور و تبدیل

[← ماژول M06](../README.md) | [صفحهٔ مسیر Python](../../../tracks/python.md)

**فایل:** [`M06_solutions.py`](M06_solutions.py) (با pandas 2.3 و scipy اجرا و کنترل شده). نیاز: `scipy` (در محیط conda دوره هست).

## بخش آموزشی

| کار | Python | نکته |
|---|---|---|
| چارک‌ها | `np.percentile(x, [25,50,75], method="weibull")` | `weibull` = تعریف ۶ (SPSS/Prism)؛ پیش‌فرض `linear` = تعریف ۷ |
| چولگی، کشیدگی | `x.skew()`، `x.kurt()` (pandas) | **G1، G2** ✔ مثل SPSS |
| — | `stats.skew(x, bias=False)` (scipy) | بدون `bias=False` فرمول دیگری (g1) |
| نمرهٔ z | `(x - x.mean()) / x.std()` | `stats.zscore` پیش‌فرض ddof=0 دارد! |
| میانگین پیراسته | `stats.trim_mean(x, 0.05)` | ۵٪ از هر طرف |
| لگاریتم | `np.log10`، `np.log`، `np.log2` | |
| نمودار جعبه‌ای | `plt.boxplot(x)` یا `d.boxplot()` | M08 |

> **دو دام scipy:** `stats.skew` و `stats.kurtosis` بدون `bias=False`، و `stats.zscore` بدون `ddof=1`، با SPSS و Excel نمی‌خوانند. pandas این مشکل را ندارد.

## تمرین‌های عملی (ع۱ تا ع۷)

این تمرین‌ها در هر پنج مسیر **یکسان‌اند**. داده: `data/M06_icu.csv`.

| شماره | سطح | تمرین | درس |
|---|---|---|---|
| ع۱ | ۱ | خلاصهٔ پنج‌عددی `lactate` و `sodium`. نرم‌افزار شما چارک را با کدام تعریف حساب می‌کند؟ | ۶.۱ |
| ع۲ | ۱ | چولگی و کشیدگی `age`، `sodium`، `lactate` و `los`. کدام‌ها متقارن‌اند؟ | ۶.۲ |
| ع۳ | ۲ | حصار بالای توکی و تعداد مقادیر دور برای `lactate` و `los` (با تعریف ۶ چارک). | ۶.۳ |
| ع۴ | ۲ | نمرهٔ z سدیم ۱۶۸ و ۱۲۴؛ چند مقدار \|z\| > 3 دارند؟ z سدیم ۱۲۴ را پس از کنار گذاشتن ۱۶۸ دوباره حساب کنید. | ۶.۳ |
| ع۵ | ۲ | میانگین، میانه و میانگین ۵٪ پیراستهٔ `los`؛ میانگین ۵٪ پیراستهٔ `lactate`. | ۶.۳ |
| ع۶ | ۳ | log₁₀ لاکتات: چولگی، میانگین و SD لگاریتم، میانگین هندسی، SD هندسی، بازهٔ «÷/×». | ۶.۴ |
| ع۷ | ۳ | تحلیل حساسیت سدیم: n، میانگین، SD و چولگی با و بدون بیمار ۱۶۸. کدام را گزارش می‌کنید؟ | ۶.۲، ۶.۳ |

<details>
<summary><b>جواب‌های نهایی (فقط برای کنترل، پس از حل)</b></summary>

| | جواب |
|---|---|
| ع۱ | lactate: **0.5، 1.025، 1.6، 2.7، 6.5** (تعریف ۶: SPSS، Prism، Excel `.EXC`) — با تعریف ۷ (R، Python، Excel `QUARTILE`): Q1 = **1.075**؛ sodium: **124، 136، 139، 142، 168** (هر دو تعریف) |
| ع۲ | چولگی: age **−0.02**، sodium **2.11**، lactate **1.43**، los **3.04**؛ کشیدگی: age **−0.32**، sodium **12.06**، lactate **2.10**، los **10.98** ← فقط age متقارن (سدیم به‌خاطر یک مقدار) |
| ع۳ | lactate: حصار **5.21**، **2** مقدار دور (5.5، 6.5)؛ los: حصار **13**، **6** مقدار دور (17، 17، 20، 23، 28، 41) |
| ع۴ | z(168) = **5.20**؛ z(124) = **−2.72**؛ \|z\| > 3: **1**؛ بدون ۱۶۸: z(124) = **−3.57** (پوشاندن) |
| ع۵ | los: میانگین **6.55**، میانه **4**، پیراسته **5.52**؛ lactate پیراسته **1.88** |
| ع۶ | چولگی پس از لگاریتم **0.16**؛ میانگین log **0.2231**، SD log **0.2610**؛ میانگین هندسی **1.67**؛ SD هندسی **1.82**؛ بازه **0.92 تا 3.05** |
| ع۷ | همه: n **60**، **139.13**، SD **5.56**، چولگی **2.11**؛ بدون ۱۶۸: n **59**، **138.64**، SD **4.10**، چولگی **−0.53** ← گزارش اصلی با **همهٔ** بیماران (میانه ۱۳۹، Q1–Q3: ۱۳۶–۱۴۲)، با ذکر بیمار ۱۶۸ و تحلیل حساسیت |

</details>

### حل تمرین‌ها

کد کامل: [`M06_solutions.py`](M06_solutions.py).

<details>
<summary><b>حل ع۱ و ع۲</b></summary>

```python
d = pd.read_csv("../data/M06_icu.csv")
x = d["lactate"]
np.r_[x.min(), np.percentile(x, [25, 50, 75], method="weibull"), x.max()]
v = ["age", "sodium", "lactate", "los"]
pd.DataFrame({"skew": d[v].skew(), "kurt": d[v].kurt()}).round(2)
```

</details>

<details>
<summary><b>حل ع۳</b></summary>

```python
def tukey(x, method="weibull"):
    q1, q3 = np.percentile(x, [25, 75], method=method)
    return q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)

lo, hi = tukey(d["lactate"]); sorted(d.loc[d["lactate"] > hi, "lactate"])   # [5.5, 6.5]
lo, hi = tukey(d["los"]);     sorted(d.loc[d["los"] > hi, "los"])           # 6 مقدار
```

</details>

<details>
<summary><b>حل ع۴</b></summary>

```python
s = d["sodium"]; z = (s - s.mean()) / s.std()
z[s == 168], z[s == 124], (z.abs() > 3).sum()        # 5.20, -2.72, 1
s2 = s[s != 168]; (124 - s2.mean()) / s2.std()       # -3.57
```

</details>

<details>
<summary><b>حل ع۵ و ع۶</b></summary>

```python
stats.trim_mean(d["los"], 0.05)                      # 5.52
lx = np.log10(d["lactate"])
lx.skew(), 10 ** lx.mean(), 10 ** lx.std()           # 0.16 1.67 1.82
```

</details>

<details>
<summary><b>حل ع۷</b></summary>

```python
for name, x in [("all", s), ("without_168", s2)]:
    print(name, len(x), x.mean(), x.std(), x.skew())
```

</details>

## خطاهای رایج

| مشکل | علت | راه‌حل |
|---|---|---|
| چولگی ۱٫۳۹ به‌جای ۱٫۴۳ | `stats.skew` با bias=True | `.skew()` pandas یا `bias=False` |
| z کمی بزرگ‌تر از SPSS | `stats.zscore` با ddof=0 | `stats.zscore(x, ddof=1)` |
| `method=` خطا داد | numpy قدیمی (< 1.22) | به‌روزرسانی یا `interpolation="weibull"` در نسخه‌های قدیمی |

## درس‌های عملی جداگانه

- [1 — چارک و قرارداد محاسبه](L01.md)
- [2 — دیدن چولگی و نقش مقدارهای دور](L02.md)
- [3 — حصار و بررسی مقدار دور](L03.md)
- [4 — تبدیل و برگشت](L04.md)

</div>
