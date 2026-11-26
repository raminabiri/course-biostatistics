<div dir="rtl">

# کارگاه گام‌به‌گام M20

این کارگاه ادامهٔ [شروع M01](../../phase-0-foundations/M01-data-and-variables/START.md) است. [فیلم و مرجع هر پنج مسیر](references.md#software-media) برای مرور در دسترس است.

- **Excel.** کارپوشهٔ خالی باز کنید. هر فرمول را با علامت = وارد کنید و Enter بزنید. اگر جداکنندهٔ آرگومان در نصب شما نقطه‌ویرگول است، ویرگول بین آرگومان‌ها را عوض کنید. کارپوشه را با File → Save As ذخیره کنید.
- **SPSS.** برای قطعه‌های Syntax از File → New → Syntax استفاده کنید. کد را وارد کنید و Run → All را بزنید. برای حفظ پروژهٔ باز، تمرین را در یک مجموعهٔ تازه انجام دهید. جدول را در Output و متغیر محاسبه‌شده را در Data View بخوانید.
- **Prism.** از File → New Project شروع کنید. نوع جدول و چگونگی ورود داده در تمرین آمده است. Analyze را بزنید و نتیجه را در Results بخوانید. پروژه را از File → Save As ذخیره کنید.
- **R.** در RStudio پوشهٔ ماژول را از Session → Set Working Directory → Choose Directory انتخاب کنید، سپس فایل [M20_workshop.R](r/M20_workshop.R) را باز کنید و Source را بزنید. برای اجرای ترمینالی در پوشهٔ ماژول، `Rscript --vanilla r/M20_workshop.R`. پاسخ در Console دیده می‌شود.
- **Python.** در VS Code پوشهٔ ماژول را باز کنید و فایل [M20_workshop.py](python/M20_workshop.py) را با Run Python File اجرا کنید. اگر SciPy لازم است، در همان مفسر M01 و از Terminal → New Terminal، فرمان `python -m pip install scipy` را اجرا کنید. در سیستمی که M01 را با python3 اجرا کردید همان نام را به کار ببرید. سپس `python python/M20_workshop.py` را اجرا کنید. پاسخ در Terminal چاپ می‌شود. برای نگهداری آن، می‌توانید در پایان فرمان `> output.txt` بگذارید تا متن در همان پوشه ذخیره شود.

[دادهٔ ساختگی](data/practice.csv). در Excel از Data → From Text/CSV و در SPSS از Import Data → CSV Data کمک بگیرید. سرستون‌ها را از ردیف اول بخوانید و جداکننده را ویرگول بگذارید.

<a id="lesson-1"></a>

## تمرین 20.1

**خروجی مرجع R و Python.** F=10.664260، P=0.002179.

### Excel

داده‌های A، B و C را از CSV در سه ستون جدا بگذارید. Data → Data Analysis → ANOVA: Single Factor، ورودی را هر سه ستون و گروه‌بندی را Columns بگذارید.

### SPSS

Analyze → Compare Means → One-Way ANOVA، value را Dependent و group را Factor بگذارید.

### Prism

Column با سه ستون بسازید. Analyze → One-way ANOVA و گزینهٔ Ordinary را بزنید. P کلی را در Results بخوانید.

### R

اسکریپت R را اجرا کنید. خط L1 خروجی همین درس را نشان می‌دهد. تعریف گروه‌ها، مدل و توزیع مرجع درون فایل آمده است.

### Python

اسکریپت Python را اجرا کنید. خط L1 را با عدد کنترل مقایسه کنید. این فایل به SciPy و NumPy متکی است.

<a id="lesson-2"></a>

## تمرین 20.2

**خروجی مرجع R و Python.** Welch: F=9.266389، P=0.009547. Brown–Forsythe: F=10.664260، P=0.004720.

### Excel

ToolPak فقط مدل کلاسیک این تمرین را اجرا می‌کند. برای Welch، برای هر گروه n و VAR.S را بسازید؛ w=n/VAR.S و F تصحیح‌شده را از درس بگیرید. سپس `F.DIST.RT(F,df1,df2)` را محاسبه کنید.

### SPSS

در One-Way ANOVA، Options و بخش Robust Tests of Equality of Means را باز کنید. Welch و Brown–Forsythe را درخواست کنید.

### Prism

در One-way ANOVA، گزینهٔ واریانس‌های نابرابر و Welch/Brown–Forsythe را انتخاب کنید. جدول مقایسهٔ میانگین‌ها را بخوانید.

### R

اسکریپت R را اجرا کنید. خط L2 خروجی همین درس را نشان می‌دهد. تعریف گروه‌ها، مدل و توزیع مرجع درون فایل آمده است.

### Python

اسکریپت Python را اجرا کنید. خط L2 را با عدد کنترل مقایسه کنید. این فایل به SciPy و NumPy متکی است.

<a id="lesson-3"></a>

## تمرین 20.3

**خروجی مرجع R و Python.** روند C−A=8.8 و P تعدیل‌شدهٔ Tukey برای C−A حدود 0.001694.

### Excel

اگر سه P خام دارید، برای Bonferroni هرکدام را در ۳ ضرب کنید و با MIN(1,...) سقف بگذارید. ابزار کلاسیک پس‌آزمون‌ها را آماده نمی‌دهد. از خروجی R برای Tukey استفاده کنید.

### SPSS

در One-Way ANOVA، Post Hoc را باز و روش واریانس مشترک یا نامساوی را انتخاب کنید. برای روند از Contrasts با وزن −۱،۰،۱ استفاده کنید.

### Prism

در Multiple Comparisons، همهٔ جفت‌ها برای Tukey یا هر گروه در برابر کنترل برای Dunnett را برگزینید. اگر تحلیل واریانس نابرابر است، گزینهٔ ارائه‌شده برای همین مدل را انتخاب و نام دقیقش را گزارش کنید.

### R

اسکریپت R را اجرا کنید. خط L3 خروجی همین درس را نشان می‌دهد. تعریف گروه‌ها، مدل و توزیع مرجع درون فایل آمده است.

### Python

اسکریپت Python را اجرا کنید. خط L3 را با عدد کنترل مقایسه کنید. این فایل به SciPy و NumPy متکی است.

</div>
