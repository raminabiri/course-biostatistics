# کارگاه قدم‌به‌قدم M08

این راهنما ادامهٔ [شروع M01](../../phase-0-foundations/M01-data-and-variables/START.md) است. مسیر نرم‌افزاری خودتان را دنبال کنید.

[فیلم‌ها و راهنماهای نوشتاری پنج مسیر](references.md#software-media)

## مسیر R

۱. در RStudio، پوشهٔ همین ماژول را به عنوان Working Directory انتخاب کنید. از `Session → Set Working Directory → Choose Directory` کمک بگیرید. در Console، با `getwd()` مطمئن شوید نام آخر پوشه با M08 شروع می‌شود و با `list.files()` وجود پوشهٔ r را ببینید.
۲. از `File → Open File` فایل [تمرین R](r/M08_figures.R) را باز کنید. فایل را در جای فعلی نگه دارید تا مسیر داده و شکل‌ها برقرار باشد.
۳. در Console فرمان `source("r/M08_figures.R")` را وارد کنید و Enter بزنید. برای دیدن یک فرمان در لحظه، نشانگر را روی خط مربوطه بگذارید و Run را بزنید. خط خواندن داده یا تعریف متغیر را اول اجرا کنید.
۴. سه شکل آغازین و شکل‌های تکمیلی در پوشهٔ figures به صورت PNG ذخیره می‌شوند. شمارهای معتبر و خلاصهٔ جدول ۱ در Console چاپ می‌شوند. برای نگهداری متن خروجی، آن را از Console به یک فایل متنی منتقل کنید.

## مسیر Python

۱. در VS Code با `File → Open Folder` پوشهٔ همین ماژول را باز کنید. همان مفسر Python که در M01 انتخاب کردید به کار می‌رود. فایل [تمرین Python](python/M08_practice.py) را باز کنید.
۲. اگر بسته‌ها در محیط M01 نصب نیستند، از Command Palette گزینهٔ `Python: Select Interpreter` را بزنید و مفسرتان را انتخاب کنید. ترمینال قدیمی را ببندید و `Terminal → New Terminal` را بزنید. در ترمینال `python -m pip install matplotlib` را اجرا کنید. اگر فرمان M01 برای شما python3 بود، همان را به جای python بگذارید. سپس برای نصب‌های بعدی نیز همین محیط را نگه دارید.
۳. دکمهٔ `Run Python File` بالای فایل را بزنید یا در ترمینالِ پوشهٔ ماژول، `python python/M08_practice.py` را اجرا کنید. پاسخ‌ها در Terminal ظاهر می‌شوند و شکل‌های Python، در درس‌های دارای شکل، در پوشهٔ ماژول ذخیره می‌شوند.
۴. اگر `ModuleNotFoundError` دیدید، اول مفسر انتخاب‌شده و مفسر ترمینال را یکی کنید. اگر فایل داده پیدا نشد، مطمئن شوید پوشهٔ data را همراه فایل برنامه دارید. خطوط چاپ‌شده را با خروجی مورد انتظار درس مقایسه کنید.

## پیش از کار در Excel، SPSS یا Prism

- **Excel.** برای CSV، یک کارپوشهٔ خالی باز کنید. از `Data → From Text/CSV` فایل را انتخاب کنید، در پیش‌نمایش Delimiter را Comma بگذارید و Load را بزنید. هر ستون باید جدا دیده شود. اگر فرمول با ویرگول پذیرفته نشد، جداکنندهٔ آرگومان را مطابق تنظیم Excel خود عوض کنید. در پایان با `File → Save As` یک نسخهٔ xlsx ذخیره کنید.
- **SPSS.** از `File → Import Data → CSV Data` فایل را انتخاب کنید. سطر اول نام متغیرهاست و جداکننده ویرگول است. پس از وارد کردن، ستون‌های عددی را در Variable View بررسی کنید. از `File → Save As` برای ذخیرهٔ دادهٔ sav و از پنجرهٔ Output برای ذخیرهٔ نتایج spv کمک بگیرید.
- **Prism.** از `File → New Project` شروع کنید. نوع جدول را طبق تمرین انتخاب کنید. هنگام انتقال جدول از CSV، عنوان ستون‌ها را جدا از خانه‌های عددی بگذارید. نتیجهٔ تحلیل در Results و نمودار در Graphs دیده می‌شود. از `File → Save As` برای ذخیرهٔ پروژه کمک بگیرید.

اگر درس دادهٔ آماده ندارد، جدول جدید بسازید و عددهای خود درس را وارد کنید. در SPSS برای تمرین‌های محاسباتیِ بدون فایل، می‌توانید `File → New → Syntax` را باز کنید، دستورهای داده‌شده را منتقل کنید و `Run → All` را بزنید.

## Excel

۱. **درس ۸.۱.** فایل `data/M08_followup.csv` را وارد کنید. در ستون H، خانه‌های H2 تا H8 را با ۱۱۰ تا ۱۷۰ در گام‌های ده‌تایی پر کنید. در I2 بنویسید `=COUNTIFS($D$2:$D$17,">="&H2,$D$2:$D$17,"<"&H3)`. فرمول را تا I7 بکشید. ستون D همان day0 است. H2:I7 را انتخاب کنید و از Insert، نمودار ستونی بسازید. در Format Data Series فاصلهٔ ستون‌ها را صفر کنید. بازهٔ آغازشونده از ۱۲۰ باید ۸ نفر داشته باشد.
۲. **درس ۸.۲.** از Insert نمودار Scatter خالی بسازید. در Select Data، برای سری A، X را C2:C9 و Y را D2:D9 بگذارید. برای B، به ترتیب از C10:C17 و D10:D17 کمک بگیرید. محور X سن و محور Y فشار آغازین است. برای میانگین و SE گروه A از `=AVERAGE(D2:D9)` و `=STDEV.S(D2:D9)/SQRT(COUNT(D2:D9))` کمک بگیرید.
۳. **درس ۸.۳.** در یک برگهٔ تازه، A2:A4 را با ۰، ۷ و ۱۴ پر کنید. B2:B4 را با مقادیر فرد ۷ یعنی ۱۳۶، خانهٔ خالی و ۱۳۰ پر کنید. نمودار Scatter with Straight Lines بسازید. از Select Data و Hidden and Empty Cells، گزینهٔ Gaps را بزنید. برای گروه B، `=COUNT(F10:F17)` باید ۷ بدهد. برای جدول ۱، AVERAGE و STDEV.S را جدا برای بازه‌های سن و day0 هر گروه اجرا کنید.

## SPSS

۱. **درس ۸.۱.** در `Transform → Compute Variable` نام target را bin10 و عبارت عددی را `TRUNC(day0/10)*10` بگذارید. در `Analyze → Descriptive Statistics → Frequencies` متغیر bin10 را انتخاب کنید. فراوانی ۱۲۰ باید ۸ باشد. در `Graphs → Chart Builder` نوع Histogram را انتخاب و day0 را روی X بکشید.
۲. **درس ۸.۲.** در Chart Builder، یک Scatter ساده بردارید. age را به X و day0 را به Y ببرید. برای جداسازی گروه‌ها نوع Grouped Scatter را انتخاب و group را در جای دسته‌بندی قرار دهید. در `Analyze → Descriptive Statistics → Explore`، day0 را در Dependent List و group را در Factor List بگذارید. میانگین و Standard Error را از خروجی Descriptives بخوانید.
۳. **درس ۸.۳.** اول دادهٔ اصلی را ذخیره کنید. برای ساخت جدول بلند روی یک کپی، دستور زیر را در Syntax اجرا کنید. NULL=KEEP باعث می‌شود ردیف نوبت گمشده بماند. N شمار مقدارهای معتبر هر گروه و نوبت را می‌دهد. برای فرد ۷، دستورهای پس از MEANS یک نمودار نقطه‌ای از دو اندازه‌گیری ثبت‌شده می‌سازند. روز ۷ نقطه ندارد و خطی روی این فاصله نمی‌کشیم. در نمودار خروجی محور روز را از صفر تا ۱۴ با گام ۷ تنظیم کنید تا جای روز ۷ روشن باشد.

```spss
VARSTOCASES
  /MAKE pressure FROM day0 day7 day14
  /INDEX=visit
  /KEEP=id group
  /NULL=KEEP.
COMPUTE day=(visit-1)*7.
EXECUTE.
MEANS TABLES=pressure BY group BY day
  /CELLS=COUNT MEAN.
TEMPORARY.
SELECT IF id=7.
GGRAPH
  /GRAPHDATASET NAME="followup" VARIABLES=day pressure
  /GRAPHSPEC SOURCE=INLINE.
BEGIN GPL
  SOURCE: s=userSource(id("followup"))
  DATA: day=col(source(s), name("day"))
  DATA: pressure=col(source(s), name("pressure"))
  GUIDE: axis(dim(1), label("Day"))
  GUIDE: axis(dim(2), label("Systolic BP (mmHg)"))
  SCALE: linear(dim(1), min(0), max(14))
  ELEMENT: point(position(day*pressure))
END GPL.
```

## Prism

۱. **درس ۸.۱.** نوع جدول Column را انتخاب کنید. فشارهای روز صفر را در دو ستون A و B وارد کنید. از Analyze، گزینهٔ Frequency distribution را پیدا کنید و از آغاز یکسان و پهنای ۱۰ کمک بگیرید. قرارداد مرز را در خروجی کنترل کنید. در نمودار Column، نوع Box-and-whiskers یا Violin را انتخاب و در Format Graph نمایش نقطه‌ها را روشن کنید.
۲. **درس ۸.۲.** نوع XY و ورود یک مقدار Y به ازای هر X را انتخاب کنید. age را در X بگذارید. دو ستون Y با عنوان A و B بسازید. فشار هر فرد فقط در ستون گروه خودش نوشته شود. در Change Graph Type، نمایش نقطه‌ای بدون خط را انتخاب کنید. نقطهٔ ۷۱ سالهٔ A باید فشار ۱۶۰ داشته باشد.
۳. **درس ۸.۳.** در XY، سه X یعنی ۰، ۷ و ۱۴ را وارد کنید. برای هر شناسه یک سری Y بگذارید. سری فرد ۷ در ردیف وسط خالی است. نمودار خط و نقطه را انتخاب کنید. اگر نسخهٔ شما دو نقطه را روی فاصلهٔ خالی به هم وصل می‌کند، سری فرد ۷ را فقط نقطه‌ای نمایش دهید. برای جدول ۱، دادهٔ آغاز هر گروه را در Column جدا بگذارید و در Analyze، Column statistics و سپس Mean و SD را بخوانید.
