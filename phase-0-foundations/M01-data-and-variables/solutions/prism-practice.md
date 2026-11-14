# پاسخ‌های مسیر prism

<a id="answer-1"></a>

## پاسخ 1

مراحل گام ۱. **جواب: ۳۰ سطر و ۱۲ ستون.** شمارهٔ سطرها در ستون خاکستری سمت چپ جدول دیده می‌شود.

<a id="answer-2"></a>

## پاسخ 2

**بخش اول — جای هر متغیر در Prism:**

| متغیر | نوع (درس ۱.۲) | جای معمول در Prism |
|---|---|---|
| sex، ward، organism، cipro_res | کیفی اسمی | عنوان ستون یا سطر (گروه)؛ در جدول Contingency، سطر/ستون |
| severity | کیفی ترتیبی | عنوان ستون/سطر **به ترتیب** Mild، Moderate، Severe |
| pain | ترتیبی (عددی) | مقدار داخل خانه، یا گروه |
| age، temp، crp، wbc، los | کمّی | مقدار داخل خانه؛ یا X در جدول XY |
| id | شناسه | Row title |

**بخش دوم — جدول CRP بر اساس بخش** (گام ۲): پس از مرتب‌سازی بر اساس `ward`:

| ستون | تعداد مقدار |
|---|---|
| Internal | 12 |
| Surgery | 12 (شامل دو مقدار ‎-99 بیماران ۷ و ۱۹) |
| ICU | 6 |

این همان جدول فراوانی `ward` است: ۱۲، ۱۲، ۶. توجه کنید دو ‎-99 در ستون Surgery هستند؛ پیش از هر تحلیلی باید Exclude شوند.

<a id="answer-3"></a>

## پاسخ 3

1. New Data Table ← Column ← یک ستون با عنوان `CRP`، ۳۰ مقدار.
2. Analyze ← Column analyses ← Descriptive statistics:
   **Number of values = 30، Mean = 35.10** (Minimum = ‎-99 ← علامت خطر).
3. به جدول برگردید، دو خانهٔ ‎-99 (سطرهای ۷ و ۱۹) را انتخاب و **Exclude** کنید.
4. به صفحهٔ نتایج برگردید؛ خودکار به‌روز شده است:
   **Number of values = 28، Mean = 44.68**.
5. برای `wbc`: ۳۰ سطر بچسبانید (سطر ۱۲ خالی است) ← **Number of values = 29**.

<a id="answer-4"></a>

## پاسخ 4

1. یک جدول Column با ستون `ward_code` (۳۰ کد) ← Descriptive statistics ← **Mean = 1.800**. Prism نمی‌داند این‌ها کدند؛ ۱٫۸ هیچ بخش واقعی‌ای نیست (درس ۱.۲، دام ۱).
2. Analyze ← Column analyses ← **Frequency distribution** ← Bin width = **1** (و مرکز اولین بین = 1) ← Tabulate: **Number of values**:

| Bin center | Frequency |
|---|---|
| 1 (Internal) | 12 |
| 2 (Surgery) | 12 |
| 3 (ICU) | 6 |

3. **organism** متنی است و Frequency distribution فقط عدد می‌پذیرد. راه ساده در Prism: داده را در Excel بر اساس `organism` مرتب کنید و `age` هر گروه را در یک جدول Column با سه ستون (E. coli، Klebsiella، Proteus) بچسبانید (سن گمشده ندارد). در Descriptive statistics، Number of values هر ستون:
   **E. coli = 17، Klebsiella = 9، Proteus = 4**.
   (یا مستقیم در Excel با `COUNTIF`. این یکی از محدودیت‌های Prism برای کار با دادهٔ کیفی خام است.)

<a id="answer-5"></a>

## پاسخ 5

جدول Contingency **شمارش** می‌خواهد، نه دادهٔ خام. پس:

1. در Excel با PivotTable (Rows = sex، Columns = cipro_res، Values = Count of id) یا مرتب‌سازی، شمارش‌ها را پیدا کنید.
2. Prism: New Data Table ← **Contingency** ← Create.
3. Row titles: Female، Male | Column titles: Susceptible، Resistant | خانه‌ها:

| | Susceptible | Resistant |
|---|---|---|
| Female | 13 | **7** |
| Male | 6 | 4 |

**جواب: ۷ بیمار زن مقاوم بودند.** همین جدول در M35 با کای‌دو و آزمون دقیق فیشر تحلیل می‌شود.

<a id="answer-6"></a>

## پاسخ 6

مراحل گام ۵. **۸ سطر (بیمار) × ۳ ستون (روز) = ۲۴ مقدار.** سطر اول: Row title = 1؛ مقادیر 94.8، 46.2، 12.1.

**چرا قالب بلند لازم نیست؟** در Prism «جفت بودن» با **قرار گرفتن در یک سطر** نشان داده می‌شود. همین ساختار برای ANOVA تکراری (M22) و نمودار «before–after» کافی است. ۲۴ مقدار همان ۲۴ سطر قالب بلند در SPSS/R/Python است. اگر به قالب بلند نیاز دارید (برای نمونه برای مدل آمیخته در R)، تبدیل را در نرم‌افزار دیگری انجام دهید.

روش جایگزین: جدول **XY** با X = 0، 3، 7 و هر بیمار یک زیرستون Y (Subcolumn). برای رسم منحنی هر بیمار مفید است.

<a id="answer-7"></a>

## پاسخ 7

`File > Save As` ← `M01.prism`. پس از باز کردن دوباره، همهٔ جدول‌ها، عنوان‌ها، خانه‌های Exclude شده (آبی، کج) و نتایج تحلیل‌ها سر جایشان هستند. **بله، می‌مانند.** اگر داده را به CSV صادر کنید، اطلاعات Exclude از دست می‌رود.

