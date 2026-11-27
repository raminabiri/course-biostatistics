<div dir="rtl">

# M01 در R

از پوشهٔ ماژول اجرا کنید `Rscript --vanilla r/M01_module.R`. اگر با RStudio کار می‌کنید، پوشهٔ ماژول را پوشهٔ کار قرار دهید و `source("r/M01_module.R")` را در Console بنویسید.

`read.csv` جدول را می‌خواند. `split` دماها را بر حسب روز جدا می‌کند. `is.na` خانهٔ گمشده را پیدا می‌کند. `!is.na(x)` برای هر مقدار موجود TRUE است و جمع آن شمار مقدارهای معتبر را می‌دهد. `na.rm=TRUE` در mean مقدار گمشده را برای همان میانگین کنار می‌گذارد. `reshape` مقدارهای دو روز را با شناسهٔ فرد در دو ستون می‌چیند تا تفاضل جفتی از فردهای درست گرفته شود.

خروجی باید به‌ترتیب روز صفر و روز سه شمار ۳،۳ و ۳،۲ و میانگین حدود ۳۷٫۳۶۶۷ و ۳۷٫۲ باشد. خط آخر میانگین تغییرهای جفتی را حدود منفی ۰٫۲۵ نشان می‌دهد.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

[فیلم MarinStatsLectures دربارهٔ خواندن CSV](https://www.youtube.com/watch?v=qPk0YEKhqB8) · [مستندات read.csv در R](https://stat.ethz.ch/R-manual/R-devel/library/utils/html/read.table.html). بخش CSV کافی است.

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ تمرین‌ها](../solutions/module.md)

</div>
