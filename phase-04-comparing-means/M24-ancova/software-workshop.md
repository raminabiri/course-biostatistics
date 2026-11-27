<div dir="rtl">

# کارگاه گام‌به‌گام M24

این کارگاه ادامهٔ [شروع M01](../../phase-00-foundations/M01-data-and-variables/START.md) است. [فیلم و مرجع هر پنج مسیر](references.md#software-media) برای مرور در دسترس است.

- **Excel.** کارپوشهٔ خالی باز کنید. هر فرمول را با علامت = وارد کنید و Enter بزنید. اگر جداکنندهٔ آرگومان در نصب شما نقطه‌ویرگول است، ویرگول بین آرگومان‌ها را عوض کنید. کارپوشه را با File → Save As ذخیره کنید.
- **SPSS.** برای قطعه‌های Syntax از File → New → Syntax استفاده کنید. کد را وارد کنید و Run → All را بزنید. برای حفظ پروژهٔ باز، تمرین را در یک مجموعهٔ تازه انجام دهید. جدول را در Output و متغیر محاسبه‌شده را در Data View بخوانید.
- **Prism.** از File → New Project شروع کنید. نوع جدول و چگونگی ورود داده در تمرین آمده است. Analyze را بزنید و نتیجه را در Results بخوانید. پروژه را از File → Save As ذخیره کنید.
- **R.** در RStudio پوشهٔ ماژول را از Session → Set Working Directory → Choose Directory انتخاب کنید، سپس فایل [M24_workshop.R](r/M24_workshop.R) را باز کنید و Source را بزنید. برای اجرای ترمینالی در پوشهٔ ماژول، `Rscript --vanilla r/M24_workshop.R`. پاسخ در Console دیده می‌شود.
- **Python.** در VS Code پوشهٔ ماژول را باز کنید و فایل [M24_workshop.py](python/M24_workshop.py) را با Run Python File اجرا کنید. اگر SciPy لازم است، در همان مفسر M01 و از Terminal → New Terminal، فرمان `python -m pip install scipy` را اجرا کنید. در سیستمی که M01 را با python3 اجرا کردید همان نام را به کار ببرید. سپس `python python/M24_workshop.py` را اجرا کنید. پاسخ در Terminal چاپ می‌شود. برای نگهداری آن، می‌توانید در پایان فرمان `> output.txt` بگذارید تا متن در همان پوشه ذخیره شود.

[دادهٔ ساختگی](data/practice.csv). در Excel از Data → From Text/CSV و در SPSS از Import Data → CSV Data کمک بگیرید. سرستون‌ها را از ردیف اول بخوانید و جداکننده را ویرگول بگذارید.

<a id="lesson-1"></a>

## تمرین 24.1

**خروجی مرجع R و Python.** پیش‌بینی در baseline=24 برای A0 و A1 برابر 48.942857 و 51.285714.

### Excel

B=0 را جدا کنید. ToolPak → Regression، value را Y و ستون‌های A و baseline را X قرار دهید. مقدار پیش‌بینی با A=0 و A=1 و baseline=24 را حساب کنید.

### SPSS

GLM → Univariate، value را Dependent، a را Fixed Factor و baseline را Covariate بگذارید. Estimated Marginal Means را در خط پایهٔ ۲۴ بخوانید یا دستور EMMEANS=TABLES(a) WITH(baseline=24) را به GLM اضافه کنید.

### Prism

برای مقایسهٔ دو گروه با شیب مشترک، دو مجموعهٔ XY هر گروه را با X خط پایه بسازید. Linear regression و مقایسهٔ خطوط را مرور کنید. میانگین تعدیل‌شده در کارگاه R به دست می‌آید.

### R

اسکریپت R را اجرا کنید. خط L1 خروجی همین درس را نشان می‌دهد. تعریف گروه‌ها، مدل و توزیع مرجع درون فایل آمده است.

### Python

اسکریپت Python را اجرا کنید. خط L1 را با عدد کنترل مقایسه کنید. این فایل به SciPy و NumPy متکی است.

<a id="lesson-2"></a>

## تمرین 24.2

**خروجی مرجع R و Python.** تعامل A×B پس از تعدیل F=1.052051، P=0.317917.

### Excel

ستون حاصل‌ضرب A×B بسازید و مدل با و بدون این ستون را مقایسه کنید. F از تغییر SSE و df به دست می‌آید.

### SPSS

در Univariate، a و b را Fixed و baseline را Covariate بگذارید. Custom model شامل a، b، a*b و baseline، سپس در تحلیل جدا a*baseline را برای بررسی شیب اضافه کنید.

### Prism

برای ANCOVA دوطرفهٔ کامل از R یا SPSS کمک بگیرید. در Prism نمودار پراکنشِ خط پایه و پیامد را به تفکیک خانه‌ها بسازید.

### R

اسکریپت R را اجرا کنید. خط L2 خروجی همین درس را نشان می‌دهد. تعریف گروه‌ها، مدل و توزیع مرجع درون فایل آمده است.

### Python

اسکریپت Python را اجرا کنید. خط L2 را با عدد کنترل مقایسه کنید. این فایل به SciPy و NumPy متکی است.

<a id="lesson-3"></a>

## تمرین 24.3

**خروجی مرجع R و Python.** کنتراست تغییر تعدیل‌شده F=2.373170، P=0.157824.

### Excel

در برگه‌ای جدا فایل [تغییر افراد در B=0](data/change.csv) را باز کنید. در ToolPak → Regression، change را Y و دو ستون a و baseline را X بگذارید. برای بیش از یک تغییر از مدل مستقل روی تمام ردیف‌ها کمک نگیرید.

### SPSS

برای دو زمان کامل، تغییر را در Compute Variable بسازید و GLM Univariate با group و baseline را اجرا کنید. برای همهٔ زمان‌ها، GLM Repeated Measures یا MIXED را مطابق طرح تنظیم کنید.

### Prism

تغییرهای فردی را روی خط پایه رسم کنید. آزمون تغییر تعدیل‌شدهٔ این درس را با فایل R اجرا کنید.

### R

اسکریپت R را اجرا کنید. خط L3 خروجی همین درس را نشان می‌دهد. تعریف گروه‌ها، مدل و توزیع مرجع درون فایل آمده است.

### Python

اسکریپت Python را اجرا کنید. خط L3 را با عدد کنترل مقایسه کنید. این فایل به SciPy و NumPy متکی است.

</div>
