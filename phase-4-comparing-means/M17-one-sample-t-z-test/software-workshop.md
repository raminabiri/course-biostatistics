# کارگاه گام‌به‌گام M17

این کارگاه ادامهٔ [شروع M01](../../phase-0-foundations/M01-data-and-variables/START.md) است. [فیلم و مرجع هر پنج مسیر](references.md#software-media) برای مرور در دسترس است.

- **Excel.** کارپوشهٔ خالی باز کنید. هر فرمول را با علامت = وارد کنید و Enter بزنید. اگر جداکنندهٔ آرگومان در نصب شما نقطه‌ویرگول است، ویرگول بین آرگومان‌ها را عوض کنید. کارپوشه را با File → Save As ذخیره کنید.
- **SPSS.** برای قطعه‌های Syntax از File → New → Syntax استفاده کنید. کد را وارد کنید و Run → All را بزنید. برای حفظ پروژهٔ باز، تمرین را در یک مجموعهٔ تازه انجام دهید. جدول را در Output و متغیر محاسبه‌شده را در Data View بخوانید.
- **Prism.** از File → New Project شروع کنید. نوع جدول و چگونگی ورود داده در تمرین آمده است. Analyze را بزنید و نتیجه را در Results بخوانید. پروژه را از File → Save As ذخیره کنید.
- **R.** در RStudio فایل [M17_workshop.R](r/M17_workshop.R) را باز کنید و Source را بزنید. برای اجرای ترمینالی در پوشهٔ ماژول، `Rscript --vanilla r/M17_workshop.R`. پاسخ در Console دیده می‌شود.
- **Python.** در VS Code پوشهٔ ماژول را باز کنید و فایل [M17_workshop.py](python/M17_workshop.py) را با Run Python File اجرا کنید. اگر SciPy لازم است، در همان مفسر M01 و از Terminal → New Terminal، فرمان `python -m pip install scipy` را اجرا کنید. در سیستمی که M01 را با python3 اجرا کردید همان نام را به کار ببرید. سپس `python python/M17_workshop.py` را اجرا کنید. پاسخ در Terminal چاپ می‌شود. برای نگهداری آن، می‌توانید در پایان فرمان `> output.txt` بگذارید تا متن در همان پوشه ذخیره شود.

[دادهٔ تمرین](data/values.csv). فایل CSV را در Excel با Data → From Text/CSV باز و جداکننده را Comma بگذارید. در SPSS از File → Import Data → CSV Data استفاده کنید. در Prism اعداد را در جدول انتخابی Paste کنید. سرستون‌ها را جدا از دادهٔ عددی وارد کنید.

<a id="lesson-1"></a>

## تمرین 17.1

**خروجی مرجع R و Python.** t=2.412091 و P دوطرفه=0.046631.

### Excel

در ستون A داده قرار دارد. در B2، `=(AVERAGE(A2:A9)-50)/(STDEV.S(A2:A9)/SQRT(COUNT(A2:A9)))` را وارد کنید.

### SPSS

Analyze → Compare Means → One-Sample T Test. متغیر value را در Test Variable و ۵۰ را در Test Value بگذارید. در خروجی t و df را بخوانید.

### Prism

جدول Column با یک ستون بسازید. Analyze → t tests، آزمون One-sample t test و مرجع ۵۰ را بزنید.

### R

اسکریپت R را اجرا کنید و خط L1 را با خروجی همین تمرین تطبیق دهید. تنظیم آزمون در فراخوانی با نام کامل نوشته شده است.

### Python

اسکریپت Python را اجرا کنید و خط L1 را بخوانید. آرگومان alternative جهت را تعیین می‌کند.

<a id="lesson-2"></a>

## تمرین 17.2

**خروجی مرجع R و Python.** z=1.414214 و P راست=0.078650.

### Excel

در B3، `=(AVERAGE(A2:A9)-50)/(8/SQRT(COUNT(A2:A9)))` و در B4، `=1-NORM.S.DIST(B3,TRUE)` را بزنید.

### SPSS

در Transform → Compute Variable، z را با `(54-50)/(8/SQRT(8))` و p_right را با `1-CDF.NORMAL(z,0,1)` بسازید.

### Prism

در Prism 11 یک XY جدا بسازید. Y=54 را با کاربر `Y=1-NORMDIST(Y,50,8/sqrt(8),"left")` تبدیل کنید. Results دنبالهٔ راست است.

### R

اسکریپت R را اجرا کنید و خط L2 را با خروجی همین تمرین تطبیق دهید. تنظیم آزمون در فراخوانی با نام کامل نوشته شده است.

### Python

اسکریپت Python را اجرا کنید و خط L2 را بخوانید. آرگومان alternative جهت را تعیین می‌کند.

<a id="lesson-3"></a>

## تمرین 17.3

**خروجی مرجع R و Python.** فاصلهٔ اختلاف [0.078714, 7.921286].

### Excel

در B5، `=T.INV.2T(0.05,7)*STDEV.S(A2:A9)/SQRT(8)` را بگذارید. فاصله ۴ ± B5 است.

### SPSS

در Options آزمون تک‌نمونه‌ای CI را ۹۵ بگذارید. کران‌های Confidence Interval of the Difference را در Output بخوانید.

### Prism

در آزمون تک‌نمونه‌ای، جهت را Two-tailed و سطح CI را ۹۵٪ بگذارید و کران‌های اختلاف را بخوانید.

### R

اسکریپت R را اجرا کنید و خط L3 را با خروجی همین تمرین تطبیق دهید. تنظیم آزمون در فراخوانی با نام کامل نوشته شده است.

### Python

اسکریپت Python را اجرا کنید و خط L3 را بخوانید. آرگومان alternative جهت را تعیین می‌کند.
