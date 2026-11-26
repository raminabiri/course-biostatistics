<div dir="rtl">

# M06 در GraphPad Prism — Descriptive statistics، Identify outliers و Transform

[← ماژول M06](../README.md) | [صفحهٔ مسیر Prism](../../../tracks/prism.md)

**نسخه:** Prism 10 و 11.

## بخش آموزشی

| کار | Prism | نکته |
|---|---|---|
| پنج‌عددی، چولگی، کشیدگی | `Descriptive statistics` ← Basics + Advanced (Skewness، Kurtosis، Geometric mean، **Geometric SD factor**) | چارک‌ها با روش n + 1 (تعریف ۶)؛ چولگی همان G1 (مثل Excel)؛ کشیدگی اضافی |
| نمودار جعبه‌ای | نمودار جدول Column ← Change graph type ← **Box & whiskers** | Prism ۵ روش برای سبیل‌ها دارد؛ روش **Tukey** نقاط بیرون از حصار را جدا نشان می‌دهد |
| شناسایی مقدار دور | `Analyze > Column analyses > Identify outliers` | روش‌های **ROUT** و **Grubbs** (M16)؛ قاعدهٔ توکی را مستقیم ندارد |
| نمرهٔ z | `Transform` ← User-defined: `Y = (Y - میانگین)/SD` (اعداد از Descriptive statistics) | |
| لگاریتم | `Transform` ← **Y = Log(Y)** | |
| میانگین پیراسته | **ندارد** | از Excel یا نرم‌افزار دیگر |

**SD هندسی در Prism:** Prism آن را «Geometric SD factor» می‌نامد و دقیقاً همان ضریب «×/÷» درس ۶.۴ است.

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

<details>
<summary><b>حل ع۱ و ع۲</b></summary>

جدول Column با ستون‌های `age`، `sodium`، `lactate`، `los` ← Descriptive statistics با Basics و Advanced ← Minimum، 25% Percentile (**1.025** برای lactate)، Median، 75% Percentile، Maximum، Skewness، Kurtosis.

</details>

<details>
<summary><b>حل ع۳</b></summary>

از Q1 و Q3 خروجی، حصار را با ماشین‌حساب بسازید (lactate: **5.21**؛ los: **13**) و مقادیر بالاتر را در جدول داده (پس از مرتب‌سازی در Excel) بشمارید: **2** و **6**. نمودار Box & whiskers با گزینهٔ **Tukey** همین مقادیر را به‌صورت نقطه نشان می‌دهد.

</details>

<details>
<summary><b>حل ع۴</b></summary>

Transform روی ستون سدیم ← User-defined: `Y = (Y - 139.13)/5.56` ← در جدول نتیجه: **5.20** (۱۶۸) و **−2.72** (۱۲۴). برای بدون ۱۶۸: خانهٔ ۱۶۸ را **Exclude** کنید (M01) ← Descriptive statistics خودکار به‌روز می‌شود: 138.64، 4.10 ← z(124) = **−3.57**.

</details>

<details>
<summary><b>حل ع۵</b></summary>

Mean (**6.55**) و Median (**4**) از Descriptive statistics. میانگین پیراسته در Prism نیست؛ در Excel: `=TRIMMEAN(E2:E61,0.1)` ← **5.52**.

</details>

<details>
<summary><b>حل ع۶</b></summary>

Descriptive statistics روی lactate با Advanced: Geometric mean **1.67**، Geometric SD factor **1.82**. Transform ← Y = Log(Y) ← Descriptive statistics روی نتیجه: Mean **0.2231**، SD **0.2610**، Skewness **0.16**.

</details>

<details>
<summary><b>حل ع۷</b></summary>

Descriptive statistics روی سدیم، یک بار با همه و یک بار با ۱۶۸ **Excluded**؛ اعداد جدول جواب‌ها. مزیت Prism: Exclude قابل‌برگشت است و تصمیم شما در جدول دیده می‌شود.

</details>

## درس‌های عملی جداگانه

- [1 — چارک و قرارداد محاسبه](L01.md)
- [2 — دیدن چولگی و نقش مقدارهای دور](L02.md)
- [3 — حصار و بررسی مقدار دور](L03.md)
- [4 — تبدیل و برگشت](L04.md)

</div>
