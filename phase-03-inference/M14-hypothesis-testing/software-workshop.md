<div dir="rtl">

# کارگاه گام‌به‌گام M14

این کارگاه ادامهٔ [شروع M01](../../phase-00-foundations/M01-data-and-variables/START.md) است. [فیلم و مرجع هر پنج مسیر](references.md#software-media) برای مرور در دسترس است.

- **Excel.** کارپوشهٔ خالی باز کنید. هر فرمول را با علامت = وارد کنید و Enter بزنید. اگر جداکنندهٔ آرگومان در نصب شما نقطه‌ویرگول است، ویرگول بین آرگومان‌ها را عوض کنید. کارپوشه را با File → Save As ذخیره کنید.
- **SPSS.** برای قطعه‌های Syntax از File → New → Syntax استفاده کنید. کد را وارد کنید و Run → All را بزنید. برای حفظ پروژهٔ باز، تمرین را در یک مجموعهٔ تازه انجام دهید. جدول را در Output و متغیر محاسبه‌شده را در Data View بخوانید.
- **Prism.** از File → New Project شروع کنید. نوع جدول و چگونگی ورود داده در تمرین آمده است. Analyze را بزنید و نتیجه را در Results بخوانید. پروژه را از File → Save As ذخیره کنید.
- **R.** در RStudio فایل [M14_workshop.R](r/M14_workshop.R) را باز کنید و Source را بزنید. برای اجرای ترمینالی در پوشهٔ ماژول، `Rscript --vanilla r/M14_workshop.R`. پاسخ در Console دیده می‌شود.
- **Python.** در VS Code پوشهٔ ماژول را باز کنید و فایل [M14_workshop.py](python/M14_workshop.py) را با Run Python File اجرا کنید. اگر SciPy لازم است، در همان مفسر M01 و از Terminal → New Terminal، فرمان `python -m pip install scipy` را اجرا کنید. در سیستمی که M01 را با python3 اجرا کردید همان نام را به کار ببرید. سپس `python python/M14_workshop.py` را اجرا کنید. پاسخ در Terminal چاپ می‌شود. برای نگهداری آن، می‌توانید در پایان فرمان `> output.txt` بگذارید تا متن در همان پوشه ذخیره شود.

<a id="lesson-1"></a>

## تمرین 14.1

**خروجی برای مقایسه.** t=۲، df=۲۴.

### Excel

A1=54، A2=50، A3=10، A4=25 و A5 برابر `=(A1-A2)/(A3/SQRT(A4))`. فرضیه و جهت را در B1 و B2 ثبت کنید.

### SPSS

در Syntax یک سطر با `DATA LIST FREE / mean_value target sd_value n.
BEGIN DATA
54 50 10 25
END DATA.
COMPUTE tval=(mean_value-target)/(sd_value/SQRT(n)).
EXECUTE.` بسازید. tval در Data View برابر ۲ است.

### Prism

در XY، Y=54 بگذارید. در User-defined Y transform فرمول `Y=(Y-50)/(10/sqrt(25))` را وارد کنید و Results را بخوانید.

### R

سطر L1 بعد از اجرای اسکریپت، t و df را چاپ می‌کند.

### Python

سطر L1 آماره و df را چاپ می‌کند. فرمول داخل فایل از mean، ref، sd و n استفاده می‌کند.

<a id="lesson-2"></a>

## تمرین 14.2

**خروجی برای مقایسه.** P راست حدود ۰٫۰۲۸۵ و P دوطرفه حدود ۰٫۰۵۶۹.

### Excel

در A6 بنویسید `=T.DIST.RT(A5,A4-1)`. در A7 بنویسید `=T.DIST.2T(ABS(A5),A4-1)`. مقدارها را با سطح ۰٫۰۵ مقایسه کنید.

### SPSS

روی همان فایل، در Compute Variable برای p_right از `1-CDF.T(tval,n-1)` و برای p_two از `2*(1-CDF.T(ABS(tval),n-1))` کمک بگیرید.

### Prism

در Prism 11 در یک XY جدا Y=2 بگذارید. برای دنبالهٔ راست `Y=TDIST(Y,24)` و برای دوطرفه `Y=2*TDIST(abs(Y),24)` را روی دادهٔ اولیه اجرا کنید.

### R

pt با lower.tail=FALSE سمت راست را حساب می‌کند. سطر L2 هر دو P را چاپ می‌کند.

### Python

t.sf سمت راست را حساب می‌کند. P دوطرفه از قدر مطلق آماره و ضرب در ۲ به دست می‌آید.

<a id="lesson-3"></a>

## تمرین 14.3

**خروجی برای مقایسه.** فاصلهٔ اختلاف [−۰٫۱۳، ۸٫۱۳].

### Excel

در A8، `=T.INV.2T(.05,A4-1)*A3/SQRT(A4)` را بزنید. برای کران‌ها، آن را از اختلاف A1−A2 کم و به آن اضافه کنید.

### SPSS

با Compute Variable ابتدا h را با `IDF.T(.975,n-1)*sd_value/SQRT(n)` حساب کنید. سپس lo برابر mean_value−target−h و hi برابر mean_value−target+h است.

### Prism

در Prism 11، Y=4 و تبدیل کاربر `Y=Y-TINV(.05,24)*2` کران پایین را می‌دهد. + به جای − کران بالا را می‌دهد. صفر را با بازه بسنجید.

### R

در L3 اسکریپت، qt ضریب فاصله را از df به دست می‌آورد.

### Python

در L3 اسکریپت، ppf(.975, df) فاصله را می‌سازد. تطابق قرارگرفتن صفر و P در کد بررسی می‌شود.

</div>
