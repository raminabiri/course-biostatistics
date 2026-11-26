<div dir="rtl">

# M01 در Python — pandas، نوع category، دادهٔ گمشده و تغییر ساختار

> **اگر از صفر آغاز می‌کنید، [نخستین جدول را اینجا بسازید](START.md).** این صفحه برای کارهای پس از آشنایی نخست است.

← ماژول M01 | صفحهٔ مسیر Python

**پیش‌نیاز:** درس‌های نظری ۱.۱ تا ۱.۴ و نصب Python + pandas (صفحهٔ مسیر).
**فایل‌ها:** `M01_walkthrough.py` (آموزش گام‌به‌گام) و `M01_solutions.py` (حل تمرین‌ها). هر دو با Python 3 و pandas 2.3 اجرا و خروجی‌ها کنترل شده‌اند. در این گام روی pandas 2.3.3 اجرا شده‌اند؛ سازگاری با نسخه‌های دیگر باید در همان محیط سنجیده شود.
**اجرا:** از داخل پوشهٔ `python/` (چون مسیر داده `../data/` است): `python M01_walkthrough.py`، یا سلول‌به‌سلول در VS Code (هر `# %%` یک سلول).

---

## مقدمهٔ خیلی کوتاه Python/pandas برای تازه‌کارها

```python
x = 5  # نگه‌داشتن مقدار با یک نام
v = [3, 7, 2]  # نگه‌داشتن مقدار با یک نام
import pandas as pd  # آماده‌کردن ابزار لازم
d["age"]                  # ستون age از جدول (DataFrame) به نام d
d["age"].mean()  # به‌دست‌آوردن میانگین
```

در pandas یک **DataFrame** همان جدول دادهٔ مرتب است: هر ستون یک متغیر، هر سطر یک رکورد.

---

## بخش آموزشی (فایل `M01_walkthrough.py`)

### گام ۱ — خواندن داده (درس ۱.۱)

```python
uti = pd.read_csv("../data/M01_uti.csv")  # خواندن فایل و ساخت جدول
print(uti.shape)  # شمار سطر و ستون
print(uti.dtypes)  # دیدن نوع ستون‌ها
```

`dtypes` نشان می‌دهد pandas هر ستون را چه دیده است: `sex` و `ward` ← `int64` (عدد!)، `organism` ← `object` (متن؛ در pandas 3 به‌صورت `str` نمایش داده می‌شود)، `crp` ← `float64` با ‎-99 به‌عنوان یک عدد واقعی.

### گام ۲ — تعیین نوع متغیر با `category` (درس ۱.۲)

| مفهوم آماری | ابزار pandas |
|---|---|
| اسمی | `.astype("category")` |
| ترتیبی | `pd.Categorical(x, categories=[...], ordered=True)` |
| کمّی | `float64` / `int64` — همان‌طور بماند |

```python
uti["ward"] = pd.Categorical(  # تعریف رده‌های داده
    uti["ward"].map({1: "Internal", 2: "Surgery", 3: "ICU"}),  # پیوند کد با نام رده
    categories=["Internal", "Surgery", "ICU"])  # تعیین رده‌ها و ترتیب آن‌ها
uti["severity"] = pd.Categorical(  # تعریف رده‌های داده
    uti["severity"].map({1: "Mild", 2: "Moderate", 3: "Severe"}),  # پیوند کد با نام رده
    categories=["Mild", "Moderate", "Severe"], ordered=True)  # تعیین رده‌ها و ترتیب آن‌ها
```

- `.map({کد: برچسب})` همان **برچسب مقدار** SPSS است.
- `categories=[...]` ترتیب نمایش سطوح را تعیین می‌کند؛ بدون آن، pandas آن‌ها را الفبایی مرتب می‌کند.
- `ordered=True` به pandas می‌گوید Mild < Moderate < Severe.

### گام ۳ — کد گمشده ← `NA` (درس ۱.۴)

```python
print(uti["crp"].describe())  # نمایش نتیجه در خروجی
uti["crp"] = uti["crp"].replace(-99, pd.NA).astype("Float64")  # تبدیل کد ویژه به گمشده
print(uti.isna().sum())  # شناخت خانه‌های گمشده
```

- خانهٔ خالی `wbc` را `read_csv` خودش `NaN` کرده است.
- `Float64` (با F بزرگ) نوع عددی pandas است که `pd.NA` را درست نگه می‌دارد.
- برخلاف R، متدهای pandas مثل `.mean()` **به‌طور پیش‌فرض گمشده‌ها را کنار می‌گذارند** (`skipna=True`). راحت است، ولی یعنی pandas به شما هشدار نمی‌دهد که داده گمشده دارد؛ پس همیشه `isna().sum()` را خودتان نگاه کنید.

### گام ۴ — کد عددی ≠ عدد

```python
raw = pd.read_csv("../data/M01_uti.csv")  # خواندن فایل و ساخت جدول
print(raw["ward"].mean())  # به‌دست‌آوردن میانگین
print(uti["ward"].value_counts(sort=False))  # شمار هر رده
```

پس از تبدیل به `category`، `uti["ward"].mean()` خطا می‌دهد: pandas از شما در برابر این اشتباه محافظت می‌کند.

### گام ۵ — پهن به بلند با `melt` (درس ۱.۳)

```python
wide = pd.read_csv("../data/M01_crp_wide.csv")  # خواندن فایل و ساخت جدول
long = wide.melt(id_vars="id", var_name="day", value_name="crp")  # تبدیل جدول پهن به بلند
long["day"] = long["day"].str.replace("crp_d", "").astype(int)  # برداشتن پیشوند و ساخت روز عددی
print(long.shape)  # شمار سطر و ستون
```

`id_vars`: ستونی که ثابت می‌ماند؛ بقیهٔ ستون‌ها زیر هم می‌روند. نام ستون‌ها (`crp_d0`، ...) در ستون `day` قرار می‌گیرد و با `str.replace` به عدد روز تبدیل می‌شود. (عکس آن: `long.pivot(index="id", columns="day", values="crp")`.)

### گام ۶ — ذخیره با نگه‌داشتن نوع ستون‌ها

```python
uti.to_pickle("M01_uti_labeled.pkl")  # ذخیرهٔ جدول همراه نوع ستون
uti = pd.read_pickle("M01_uti_labeled.pkl")  # بازخوانی جدول ذخیره‌شده
```

`to_csv` همهٔ category ها را به متن تبدیل می‌کند و ترتیب `severity` از دست می‌رود؛ pickle همه‌چیز را نگه می‌دارد. (برای اشتراک‌گذاری بین زبان‌ها، قالب Parquet با کتابخانهٔ `pyarrow` هم مناسب است.)

---

## تمرین‌های عملی (ع۱ تا ع۷)

این تمرین‌ها در هر پنج مسیر **یکسان‌اند**. پیش از نگاه به حل، خودتان کد بنویسید.

| شماره | تمرین |
|---|---|
| ع۱ | `M01_uti.csv` را بخوانید. داده چند سطر و چند ستون دارد؟ |
| ع۲ | `sex`، `ward`، `organism`، `cipro_res` را category و `severity` را category ترتیبی کنید. نوع همهٔ ستون‌ها را نمایش دهید. |
| ع۳ | میانگین CRP را **پیش** و **پس** از تبدیل ‎-99 به `NA` حساب کنید. پس از تبدیل، CRP و WBC هر کدام چند مقدار معتبر دارند؟ |
| ع۴ | میانگین کد `ward` را حساب کنید و توضیح دهید چرا بی‌معناست. سپس جدول فراوانی `ward` و `organism` را بسازید. |
| ع۵ | چند بیمار **زن** به سیپروفلوکساسین **مقاوم** بودند؟ |
| ع۶ | `M01_crp_wide.csv` را به قالب بلند تبدیل کنید. چند سطر به دست می‌آید؟ |
| ع۷ | دادهٔ برچسب‌دار را با pickle ذخیره و دوباره بخوانید. آیا category ها مانده‌اند؟ |

### حل تمرین‌ها

کد کامل: `M01_solutions.py`

[پاسخ 1](../solutions/python-P01.md)

[پاسخ 2](../solutions/python-P02.md)

[پاسخ 3](../solutions/python-P03.md)

[پاسخ 4](../solutions/python-P04.md)

[پاسخ 5](../solutions/python-P05.md)

[پاسخ 6](../solutions/python-P06.md)

[پاسخ 7](../solutions/python-P07.md)

---

## خطاهای جاری در Python

| پیام / مشکل | علت | راه‌حل |
|---|---|---|
| `FileNotFoundError: ../data/M01_uti.csv` | اسکریپت از پوشهٔ دیگری اجرا شده | با `cd` به پوشهٔ `python/` بروید؛ در VS Code تنظیم «Execute in File Dir» را فعال کنید |
| همهٔ مقادیر پس از `.map()` به `NaN` تبدیل شدند | کلیدهای دیکشنری با نوع داده نمی‌خواند (برای نمونه `"1"` در برابر `1`) | `uti["sex"].unique()` را ببینید |
| `TypeError` هنگام `.mean()` روی ستون category | متغیر کیفی میانگین ندارد | درست است! از `value_counts()` به کار ببرید |
| میانگین بدون هشدار حساب شد با اینکه داده گمشده داشت | pandas به‌طور پیش‌فرض `skipna=True` است | همیشه `isna().sum()` را گزارش کنید |

## درس‌های عملی خودآموز

- [1 — شناخت سطر و ستون](L01.md)
- [2 — خواندن نوع متغیر و کدها](L02.md)
- [3 — فرد و نوبت در جدول پهن و بلند](L03.md)
- [4 — گمشدگی و شمار معتبر](L04.md)

</div>
