<div dir="rtl">

# کارگاه گام‌به‌گام M16

این کارگاه ادامهٔ [شروع M01](../../phase-0-foundations/M01-data-and-variables/START.md) است. [فیلم و مرجع هر پنج مسیر](references.md#software-media) برای مرور در دسترس است.

- **Excel.** کارپوشهٔ خالی باز کنید. هر فرمول را با علامت = وارد کنید و Enter بزنید. اگر جداکنندهٔ آرگومان در نصب شما نقطه‌ویرگول است، ویرگول بین آرگومان‌ها را عوض کنید. کارپوشه را با File → Save As ذخیره کنید.
- **SPSS.** برای قطعه‌های Syntax از File → New → Syntax استفاده کنید. کد را وارد کنید و Run → All را بزنید. برای حفظ پروژهٔ باز، تمرین را در یک مجموعهٔ تازه انجام دهید. جدول را در Output و متغیر محاسبه‌شده را در Data View بخوانید.
- **Prism.** از File → New Project شروع کنید. نوع جدول و چگونگی ورود داده در تمرین آمده است. Analyze را بزنید و نتیجه را در Results بخوانید. پروژه را از File → Save As ذخیره کنید.
- **R.** در RStudio ابتدا پوشهٔ همین ماژول را از Session → Set Working Directory → Choose Directory انتخاب کنید. سپس فایل [M16_workshop.R](r/M16_workshop.R) را باز کنید و Source را بزنید. نمودار Q-Q در figures ذخیره می‌شود. برای اجرای ترمینالی در پوشهٔ ماژول، `Rscript --vanilla r/M16_workshop.R`. پاسخ در Console دیده می‌شود.
- **Python.** در VS Code پوشهٔ ماژول را باز کنید و فایل [M16_workshop.py](python/M16_workshop.py) را با Run Python File اجرا کنید. اگر SciPy لازم است، در همان مفسر M01 و از Terminal → New Terminal، فرمان `python -m pip install scipy` را اجرا کنید. در سیستمی که M01 را با python3 اجرا کردید همان نام را به کار ببرید. سپس `python python/M16_workshop.py` را اجرا کنید. پاسخ در Terminal چاپ می‌شود. برای نگهداری آن، می‌توانید در پایان فرمان `> output.txt` بگذارید تا متن در همان پوشه ذخیره شود.

<a id="lesson-1"></a>

## تمرین 16.1

**خروجی برای مقایسه.** در A، W≈۰٫۸۱۵ و P≈۰٫۰۱۴.

### Excel

`data/M16_groups.csv` را با Data → From Text/CSV وارد کنید. A و B هر کدام یک ستون ۱۲ عددی‌اند. در C2 تا C13 دادهٔ A را با `=SMALL($A$2:$A$13,ROW()-1)` مرتب کنید. در D2 تا D13 نمرهٔ `=NORM.S.INV((ROW()-1.5)/12)` را بسازید. D را X و C را Y در Scatter بگذارید.

### SPSS

CSV را با File → Import Data → CSV Data و با عنوان ستون در سطر اول باز کنید. در Analyze → Descriptive Statistics → Explore، A را در Dependent List بگذارید. در Plots، Normality plots with tests را انتخاب کنید. جدول Tests of Normality هم W و هم P را دارد. پاورقی اصلاح آزمون KS را بخوانید.

### Prism

در جدول Column، A و B را جدا وارد کنید. از Analyze، آزمون Normality and lognormality را بیابید و Shapiro–Wilk را بزنید. جواب A را در Results بخوانید. برای Q-Q، دو ستون جفت نظری و مشاهده‌شده را مانند مسیر Excel در XY رسم کنید.

### R

سطر L1 را اجرا کنید. shapiro.test دادهٔ ستون A را می‌خواند. آمار و P را با عدد کنترل بسنجید.

### Python

سطر L1، shapiro را از scipy.stats اجرا می‌کند. کد داده را از CSV در ماژول می‌خواند.

<a id="lesson-2"></a>

## تمرین 16.2

**خروجی برای مقایسه.** Brown–Forsythe حدود F=۱٫۲۸۵ و P=۰٫۲۶۹.

### Excel

در برگهٔ داده، در E2 بنویسید `=ABS(A2-MEDIAN($A$2:$A$13))` و در F2 همین فرمول را با B2 و محدودهٔ B وارد کنید. تا سطر ۱۳ بکشید. در Data → Data Analysis، گزینهٔ ANOVA: Single Factor را روی E2:F13 با Grouped by Columns اجرا کنید. اگر Data Analysis نیست در File → Options → Add-ins، Analysis ToolPak را فعال کنید.

### SPSS

برای جدول بلند، یک فایل تازه با دو ستون group و value بسازید. نسخهٔ طولی آماده در `data/M16_long.csv` است. در Analyze → Compare Means → One-Way ANOVA، value را Dependent و group را Factor بگذارید. در Options، Homogeneity of variance test را فعال کنید. اگر جدول نسخهٔ شما Based on Median را نشان می‌دهد، همان ردیف را بخوانید. برای بازتولید دقیق، Compute Variable فاصلهٔ مطلق را با میانهٔ ۵۳ برای A و ۵۰ برای B بسازید و ANOVA را روی فاصله‌ها اجرا کنید.

### Prism

با جدول Column دو گروه را در Analyze و One-way ANOVA وارد کنید. در خروجی مقایسهٔ پراکندگی، سطر Brown–Forsythe برای برابری واریانس‌ها را پیدا کنید. آزمون Brown–Forsythe برای برابری میانگین‌ها جدول دیگری است.

### R

در L2، فاصله تا میانه در هر گروه محاسبه و ANOVA روی آن اجرا می‌شود. bartlett.test یک نتیجهٔ جدا چاپ می‌کند.

### Python

در L2، levene با center="median" همان آزمون را اجرا می‌کند. نتیجهٔ Bartlett جدا چاپ می‌شود.

<a id="lesson-3"></a>

## تمرین 16.3

**خروجی برای مقایسه.** G≈۲٫۷۴۶، آستانه≈۲٫۴۱۲.

### Excel

A2:A13 را نگه دارید. میانگین را با AVERAGE، SD را با STDEV.S و دورترین فاصله را با `=MAX(MAX(A2:A13)-AVERAGE(A2:A13),AVERAGE(A2:A13)-MIN(A2:A13))` بگیرید. فاصله را بر SD تقسیم کنید. برای q در خانه‌ای جدا `=T.INV(1-0.05/(2*12),10)` بگذارید و در عبارت آستانهٔ درس جای‌گذاری کنید.

### SPSS

در فایل یک‌ردیفی نمونهٔ M14، ستون تازه q را با `IDF.T(1-.05/(2*12),10)` بسازید. از Explore میانگین و SD A را بردارید و در `ABS(68-m)/s` جای‌گذاری کنید. آستانه را با عبارت `11/SQRT(12)*SQRT(q**2/(10+q**2))` حساب کنید.

### Prism

در Column، Analyze → Identify outliers را بزنید. Grubbs را با α=۰٫۰۵ برای A اجرا کنید. برای مقایسه، روی همان داده تحلیل جدا با ROUT و Q=۱٪ انجام دهید. جدول پرت‌ها و دادهٔ اصلی را نگه دارید. خروجی دو روش را جدا تفسیر کنید.

### R

در L3، فرمول G و آستانه مستقیماً از داده و qt حساب می‌شوند.

### Python

در L3، std(ddof=1) همان SD نمونه‌ای است. t.ppf آستانه را می‌سازد.

<a id="lesson-4"></a>

## تمرین 16.4

**خروجی برای مقایسه.** Welch دوطرفه برای دو گروه مستقل دادهٔ تمرین، P≈۰٫۲۱۹.

### Excel

با جدول پهن و دادهٔ کامل، `=T.TEST(A2:A13,B2:B13,2,3)` را وارد کنید. آرگومان ۲ دوطرفه و ۳ مستقل با واریانس نامساوی است. اثر را با `=AVERAGE(A2:A13)-AVERAGE(B2:B13)` گزارش کنید.

### SPSS

CSV بلند را باز کنید. در Analyze → Compare Means → Independent-Samples T Test، value را Test Variable و group را Grouping Variable بگذارید و A و B را تعریف کنید. ردیف Equal variances not assumed را برای Welch بخوانید.

### Prism

در Column با دو گروه، از Analyze → t tests (and nonparametric tests) آزمون غیرزوجی دوطرفه را انتخاب کنید. گزینهٔ Welch برای واریانس‌های نامساوی را فعال کنید. اختلاف و P را کنار هم بخوانید.

### R

سطر L4، t.test را با var.equal=FALSE اجرا می‌کند. ترتیب داده‌ها جهت اختلاف را تعیین می‌کند.

### Python

سطر L4، ttest_ind را با equal_var=False اجرا می‌کند. خروجی شامل t، df و P است.

</div>
