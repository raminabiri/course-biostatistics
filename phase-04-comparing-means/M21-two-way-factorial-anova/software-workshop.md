<div dir="rtl">

# کارگاه گام‌به‌گام M21

این کارگاه ادامهٔ [شروع M01](../../phase-00-foundations/M01-data-and-variables/START.md) است. [فیلم و مرجع هر پنج مسیر](references.md#software-media) برای مرور در دسترس است.

- **Excel.** کارپوشهٔ خالی باز کنید. هر فرمول را با علامت = وارد کنید و Enter بزنید. اگر جداکنندهٔ آرگومان در نصب شما نقطه‌ویرگول است، ویرگول بین آرگومان‌ها را عوض کنید. کارپوشه را با File → Save As ذخیره کنید.
- **SPSS.** برای قطعه‌های Syntax از File → New → Syntax استفاده کنید. کد را وارد کنید و Run → All را بزنید. برای حفظ پروژهٔ باز، تمرین را در یک مجموعهٔ تازه انجام دهید. جدول را در Output و متغیر محاسبه‌شده را در Data View بخوانید.
- **Prism.** از File → New Project شروع کنید. نوع جدول و چگونگی ورود داده در تمرین آمده است. Analyze را بزنید و نتیجه را در Results بخوانید. پروژه را از File → Save As ذخیره کنید.
- **R.** در RStudio پوشهٔ ماژول را از Session → Set Working Directory → Choose Directory انتخاب کنید، سپس فایل [M21_workshop.R](r/M21_workshop.R) را باز کنید و Source را بزنید. برای اجرای ترمینالی در پوشهٔ ماژول، `Rscript --vanilla r/M21_workshop.R`. پاسخ در Console دیده می‌شود.
- **Python.** در VS Code پوشهٔ ماژول را باز کنید و فایل [M21_workshop.py](python/M21_workshop.py) را با Run Python File اجرا کنید. اگر SciPy لازم است، در همان مفسر M01 و از Terminal → New Terminal، فرمان `python -m pip install scipy` را اجرا کنید. در سیستمی که M01 را با python3 اجرا کردید همان نام را به کار ببرید. سپس `python python/M21_workshop.py` را اجرا کنید. پاسخ در Terminal چاپ می‌شود. برای نگهداری آن، می‌توانید در پایان فرمان `> output.txt` بگذارید تا متن در همان پوشه ذخیره شود.

[دادهٔ ساختگی](data/practice.csv). در Excel از Data → From Text/CSV و در SPSS از Import Data → CSV Data کمک بگیرید. سرستون‌ها را از ردیف اول بخوانید و جداکننده را ویرگول بگذارید.

<a id="lesson-1"></a>

## تمرین 21.1

**خروجی مرجع R و Python.** تعامل A×B در C=0، F=8 و P=0.012109.

### Excel

C=0 را جدا کنید. برای هر ترکیب A و B یک مجموعه با پنج تکرار بسازید. ToolPak → ANOVA: Two-Factor With Replication و Rows per sample=5. جدول Interaction را بخوانید.

### SPSS

در GLM → Univariate، value را Dependent و a و b را Fixed Factors بگذارید. با Select Cases، c=0 و Model=Full factorial را اجرا کنید.

### Prism

در Grouped، سطح‌های A را سطر و B را مجموعه‌داده بگذارید و تکرارها را کنار هم وارد کنید. Two-way ANOVA معمولی و Interaction را بخوانید.

### R

اسکریپت R را اجرا کنید. خط L1 خروجی همین درس را نشان می‌دهد. تعریف گروه‌ها، مدل و توزیع مرجع درون فایل آمده است.

### Python

اسکریپت Python را اجرا کنید. خط L1 را با عدد کنترل مقایسه کنید. این فایل به SciPy و NumPy متکی است.

<a id="lesson-2"></a>

## تمرین 21.2

**خروجی مرجع R و Python.** اختلاف ساده A1−A0 در B=1 و C=0 برابر ۷.

### Excel

با AVERAGEIFS میانگین هر خانه را به دست آورید. میانگین A=1 منهای A=0 را در B=1 و C=0 حساب کنید.

### SPSS

در GLM، Estimated Marginal Means برای a*b و مقایسهٔ a در سطح‌های b را تعیین کنید. نوع SS را در Options ثبت کنید.

### Prism

در Multiple Comparisons، مقایسهٔ سطرها در هر ستون را تعیین کنید و جهت A1−A0 را کنترل کنید.

### R

اسکریپت R را اجرا کنید. خط L2 خروجی همین درس را نشان می‌دهد. تعریف گروه‌ها، مدل و توزیع مرجع درون فایل آمده است.

### Python

اسکریپت Python را اجرا کنید. خط L2 را با عدد کنترل مقایسه کنید. این فایل به SciPy و NumPy متکی است.

<a id="lesson-3"></a>

## تمرین 21.3

**خروجی مرجع R و Python.** تعامل سه‌طرفه F=0.4 و P=0.531583.

### Excel

میانگین هشت خانه را با AVERAGEIFS بسازید و اختلاف دو اختلاف را در هر C محاسبه کنید. ToolPak آزمون سه‌طرفه نمی‌دهد.

### SPSS

هر سه عامل را در GLM → Univariate وارد کنید و Full factorial را بزنید. a*b*c را بخوانید.

### Prism

در نسخهٔ دارای Three-way ANOVA، سه عامل و تکرارهای مستقل هر خانه را مطابق جدول طراحی وارد کنید. اگر نسخه این تحلیل را ندارد، دو برش A×B در C را رسم و آزمون سه‌طرفه را از مسیر R اجرا کنید.

### R

اسکریپت R را اجرا کنید. خط L3 خروجی همین درس را نشان می‌دهد. تعریف گروه‌ها، مدل و توزیع مرجع درون فایل آمده است.

### Python

اسکریپت Python را اجرا کنید. خط L3 را با عدد کنترل مقایسه کنید. این فایل به SciPy و NumPy متکی است.

</div>
