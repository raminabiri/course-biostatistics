<div dir="rtl">

# M05 در Excel — توابع آماری و Descriptive Statistics

[← ماژول M05](../README.md) | [صفحهٔ مسیر Excel](../../../tracks/excel.md)

**فایل‌ها:** [`M05_excel_practice.xlsx`](M05_excel_practice.xlsx) (داده + برگهٔ `answers`) و [`M05_excel_solutions.xlsx`](M05_excel_solutions.xlsx) (۳۶ جواب با فرمول؛ با LibreOffice محاسبه و با R و Python مقایسه شده).

## بخش آموزشی

### توابع

| شاخص | تابع Excel | نکته |
|---|---|---|
| میانگین / میانه / نما | `AVERAGE`، `MEDIAN`، `MODE` (یا `MODE.SNGL`) | |
| SD / واریانس نمونه | `STDEV` (یا `STDEV.S`)، `VAR` (یا `VAR.S`) | n − 1 ✔؛ `STDEV.P` بر n تقسیم می‌کند (برای «کل جامعه») |
| کمینه، بیشینه | `MIN`، `MAX` | |
| چارک (روش R/Python) | `QUARTILE(range,1)` یا `QUARTILE.INC` | تعریف ۷ |
| چارک (روش SPSS/Prism) | `QUARTILE.EXC(range,1)` | تعریف ۶ |
| SEM | `=STDEV(r)/SQRT(COUNT(r))` | تابع آماده ندارد |
| میانگین هندسی | `GEOMEAN` | |
| شرطی | `AVERAGEIF`، `COUNTIF`، `MEDIAN(IF(...))` (آرایه‌ای) | |

### SD به تفکیک گروه

Excel تابع `STDEVIF` ندارد. سه راه:
1. **PivotTable**: `sex` در Rows، `sbp` در Values ← Value Field Settings ← **StdDev** (همان STDEV.S).
2. فرمول آرایه‌ای (Microsoft 365): `=STDEV.S(FILTER(D2:D49, B2:B49="F"))`.
3. فرمول سازگار با همهٔ نسخه‌ها (در فایل حل):
```
=SQRT(SUMPRODUCT((B2:B49="F")*(D2:D49-AVERAGEIF(B2:B49,"F",D2:D49))^2)/(COUNTIF(B2:B49,"F")-1))
```

### ابزار Descriptive Statistics

`Data > Data Analysis > Descriptive Statistics` ← Input Range: ستون‌های D تا H با سرستون ← تیک **Labels in first row** و **Summary statistics** ← OK. جدولی با میانگین، Standard Error (همان SEM)، میانه، نما، SD، واریانس، کشیدگی، چولگی، دامنه، کمینه، بیشینه و … می‌سازد. این جدول **ایستا**ست: اگر داده عوض شود، به‌روز نمی‌شود.

## تمرین‌های عملی (ع۱ تا ع۷)

این تمرین‌ها در هر پنج مسیر **یکسان‌اند**. داده: `data/M05_lipid.csv`.

| شماره | سطح | تمرین | درس |
|---|---|---|---|
| ع۱ | ۱ | میانگین و میانهٔ `sbp`، `ldl` و `hscrp`؛ نمای `cigs`. | ۵.۱ |
| ع۲ | ۱ | SD، واریانس، کمینه، بیشینه و دامنهٔ `sbp` و `ldl`. | ۵.۲ |
| ع۳ | ۱ | ضریب تغییرات (CV) `sbp`، `ldl` و `hscrp`. کدام نسبتاً پراکنده‌تر است؟ | ۵.۲ |
| ع۴ | ۲ | SEM برای `ldl` و `sbp`. برای `ldl` دو بازه بسازید: میانگین ± ۲SD و میانگین ± ۲SEM. هر کدام دربارهٔ چه چیزی است؟ | ۵.۳ |
| ع۵ | ۲ | به تفکیک جنس: n، میانگین و SD برای `sbp`، `ldl`، `hdl`. | ۵.۴ |
| ع۶ | ۲ | برای `hscrp`: میانگین، میانه، میانگین هندسی، و چارک اول و سوم. نرم‌افزار شما چارک را با کدام روش حساب می‌کند؟ | ۵.۴ |
| ع۷ | ۳ | `cigs`: تعداد و درصد سیگاری‌ها (> ۰)؛ میانه و میانگین مصرف **در سیگاری‌ها**. یک جملهٔ گزارش بنویسید. | ۵.۱ |

<details>
<summary><b>جواب‌های نهایی (فقط برای کنترل، پس از حل)</b></summary>

| | جواب |
|---|---|
| ع۱ | sbp: **130.19** / **130.00**؛ ldl: **131.08** / **136.50**؛ hscrp: **3.11** / **1.75**؛ نمای cigs: **0** |
| ع۲ | sbp: SD **11.32**، واریانس **128.11**، **99** تا **155** (دامنه **56**)؛ ldl: SD **31.85**، واریانس **1014.42**، **57** تا **202** (دامنه **145**) |
| ع۳ | sbp **8.7٪**، ldl **24.3٪**، hscrp **143.9٪** ← hsCRP بسیار پراکنده‌تر |
| ع۴ | SEM: ldl **4.60**، sbp **1.63**؛ ldl ± 2SD: **67.4 تا 194.8** (افراد)؛ ldl ± 2SEM: **121.9 تا 140.3** (میانگین) |
| ع۵ | زنان (n = **16**): sbp **127.94** (9.28)، ldl **140.75** (30.29)، hdl **57.44** (10.81)؛ مردان (n = **32**): sbp **131.31** (12.19)، ldl **126.25** (31.96)، hdl **45.84** (8.98) |
| ع۶ | میانگین **3.11**، میانه **1.75**، هندسی **1.85**؛ Q1 = **1.00**؛ Q3 = **3.375** (SPSS، Prism، Excel `QUARTILE.EXC`) یا **3.325** (پیش‌فرض R و Python، Excel `QUARTILE.INC`) |
| ع۷ | **15** سیگاری (**31.3٪**)؛ در سیگاری‌ها میانه **15** و میانگین **16** نخ در روز ← «۱۵ بیمار (۳۱٫۳٪) سیگاری بودند و میانهٔ مصرف آن‌ها ۱۵ نخ در روز بود.» |

</details>

### حل تمرین‌ها

همهٔ فرمول‌ها در برگهٔ `solutions` فایل حل.

<details>
<summary><b>حل ع۱ تا ع۳</b></summary>

```
=AVERAGE(D2:D49)   =MEDIAN(D2:D49)          → 130.19, 130
=MODE(H2:H49)                               → 0
=STDEV(E2:E49)     =VAR(E2:E49)             → 31.85, 1014.42
=MAX(E2:E49)-MIN(E2:E49)                    → 145
=100*STDEV(G2:G49)/AVERAGE(G2:G49)          → 143.9 (CV hscrp)
```

</details>

<details>
<summary><b>حل ع۴</b></summary>

```
=STDEV(E2:E49)/SQRT(COUNT(E2:E49))                    → 4.60
=AVERAGE(E2:E49)-2*STDEV(E2:E49)                      → 67.38
=AVERAGE(E2:E49)+2*STDEV(E2:E49)/SQRT(COUNT(E2:E49))  → 140.28
```

</details>

<details>
<summary><b>حل ع۵</b></summary>

```
=COUNTIF(B2:B49,"F")                      → 16
=AVERAGEIF(B2:B49,"F",D2:D49)             → 127.94
SD: فرمول SUMPRODUCT بالا                  → 9.28
```
یا PivotTable با Count، Average و StdDev.

</details>

<details>
<summary><b>حل ع۶</b></summary>

```
=GEOMEAN(G2:G49)                → 1.85
=QUARTILE(G2:G49,3)             → 3.325   (مثل R و Python)
=QUARTILE.EXC(G2:G49,3)         → 3.375   (مثل SPSS و Prism)
```

</details>

<details>
<summary><b>حل ع۷</b></summary>

```
=COUNTIF(H2:H49,">0")                     → 15
=100*COUNTIF(H2:H49,">0")/COUNT(H2:H49)   → 31.25
=AVERAGEIF(H2:H49,">0")                   → 16
```
میانه با شرط: ستون کمکی `I2: =IF(H2>0,H2,"")` و `=MEDIAN(I2:I49)` ← **15** (یا در Microsoft 365: `=MEDIAN(FILTER(H2:H49,H2:H49>0))`).

</details>

## خطاهای رایج

| مشکل | علت | راه‌حل |
|---|---|---|
| SD کمی کوچک‌تر از بقیهٔ نرم‌افزارها | `STDEV.P` به‌جای `STDEV.S` | `STDEV` یا `STDEV.S` |
| چارک با SPSS فرق دارد | `QUARTILE` (INC) | `QUARTILE.EXC` |
| `#NAME?` در نسخهٔ قدیمی | توابع .S/.EXC از Excel 2010 به بعد | نسخهٔ قدیمی: `STDEV`، `QUARTILE` |
| جدول Data Analysis به‌روز نشد | خروجی ToolPak ایستاست | دوباره اجرا کنید یا از فرمول استفاده کنید |

## درس‌های عملی جداگانه

- [1 — مرکز داده](L01.md)
- [2 — پراکندگی](L02.md)
- [3 — SD در برابر SE](L03.md)
- [4 — انتخاب خلاصه و گزارش](L04.md)

</div>
