# M06 در SPSS — Explore، نمرهٔ z و تبدیل

[← ماژول M06](../README.md) | [صفحهٔ مسیر SPSS](../../../tracks/spss.md)

**فایل:** [`M06_solutions.sps`](M06_solutions.sps). خط `CD` را تغییر دهید.

## بخش آموزشی

### Explore: ابزار اصلی این ماژول

`Analyze > Descriptive Statistics > Explore` ← Dependent List: متغیرها ← دکمهٔ **Statistics**: Descriptives، **Outliers**، **Percentiles** ← دکمهٔ **Plots**: Boxplots (و در صورت تمایل Histogram) ← OK.

| جدول خروجی | چه دارد؟ |
|---|---|
| **Descriptives** | میانگین، **5% Trimmed Mean**، میانه، SD، IQR، **Skewness و Kurtosis با Std. Error** |
| **Percentiles** | ردیف **Weighted Average** (تعریف ۶) و ردیف **Tukey's Hinges** (روش میانهٔ نیمه‌ها) |
| **Extreme Values** | ۵ مقدار بزرگ‌تر و ۵ مقدار کوچک‌تر، با شمارهٔ سطر |
| **Boxplot** | ○ = مقدار دور (۱٫۵ تا ۳ برابر طول جعبه از لبه)، **\*** = بسیار دور (بیش از ۳ برابر)؛ شمارهٔ سطر کنار هر نقطه |

**نکته:** جعبهٔ نمودار SPSS بر پایهٔ Tukey's Hinges است؛ پس حصارهایی که با چارک‌های Weighted Average حساب می‌کنید ممکن است کمی با نمودار فرق کنند.

### نمرهٔ z

`Analyze > Descriptive Statistics > Descriptives` ← متغیر ← تیک **Save standardized values as variables** ← SPSS متغیر `Zsodium` می‌سازد.

### تبدیل

`Transform > Compute Variable` ← `log_lac = LG10(lactate)`. میانگین هندسی: `Analyze > Compare Means > Means` ← Options ← Geometric Mean.

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

Syntax کامل: [`M06_solutions.sps`](M06_solutions.sps).

<details>
<summary><b>حل ع۱، ع۲ و ع۵</b></summary>

Explore روی `lactate sodium los age` با Statistics (Descriptives، Percentiles، Outliers) و Boxplots ← از جدول‌ها: پنج‌عددی (Minimum، Weighted Average 25/50/75، Maximum)، Skewness، Kurtosis و 5% Trimmed Mean. همهٔ اعداد جدول جواب‌ها.

</details>

<details>
<summary><b>حل ع۳</b></summary>

از جدول Percentiles (Weighted Average): lactate ← 2.7 + 1.5 × (2.7 − 1.025) = **5.21**. جدول Extreme Values دو مقدار بالاتر را نشان می‌دهد: **6.5 و 5.5**. برای los: 7 + 1.5 × 4 = **13**؛ Extreme Values پنج مقدار بزرگ‌تر را نشان می‌دهد (41، 28، 23، 20، 17) و مقدار ششم (17 دوم) را با `COUNT` در Syntax یا مرتب‌سازی می‌بینید.

</details>

<details>
<summary><b>حل ع۴</b></summary>

Descriptives با Save standardized values ← در Data View، `Zsodium` بیمار ۱۶۸ = **5.20** و ۱۲۴ = **−2.72**. سپس `Data > Select Cases` ← If `sodium ~= 168` ← Descriptives (Mean، SD) ← 138.64، 4.10 ← z(124) = **−3.57**.

</details>

<details>
<summary><b>حل ع۶</b></summary>

Compute `log_lac = LG10(lactate)` ← Descriptives (Mean، SD، Skewness) ← 0.2231، 0.2610، 0.16 ← میانگین هندسی 10^0.2231 = **1.67** (یا Means ← Geometric Mean)؛ SD هندسی 10^0.261 = **1.82**.

</details>

<details>
<summary><b>حل ع۷</b></summary>

Descriptives (Mean، SD، Skewness) یک بار روی همه و یک بار با Select Cases `sodium ~= 168`. جدول جواب‌ها.

</details>

## خطاهای رایج

| مشکل | علت | راه‌حل |
|---|---|---|
| Explore برای بعضی متغیرها نتیجه نداد | Explore فقط سطرهای **کامل در همهٔ متغیرها** را به کار می‌برد (Listwise) | Options ← **Exclude cases pairwise** |
| حصار دستی با نمودار جعبه‌ای نمی‌خواند | جعبه با Tukey's Hinges | طبیعی است (درس ۶.۱) |
| `LG10` برای صفر گمشده داد | log صفر تعریف نشده | درس ۶.۴ |
