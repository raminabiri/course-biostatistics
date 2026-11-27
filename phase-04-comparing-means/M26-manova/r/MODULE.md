<div dir="rtl">

# M26 در R

[practice.csv](../data/practice.csv) شامل ۳۲ ردیف است. از y و z برای پایان و از y−y0 و z−z0 برای تغییر کمک می‌گیریم. a و b کد شیوه و تنظیم‌اند.

## اجرا و نقش فرمول

[فایل کارگاه](M26_workshop.R) را در RStudio باز کنید. پوشهٔ ماژول را از Session → Set Working Directory انتخاب و Source را بزنید. در Terminal از پوشهٔ ماژول `Rscript --vanilla r/M26_workshop.R` را اجرا کنید. بخش‌های L1 تا L3 در خروجی جدا هستند.

```r
data <- read.csv("data/practice.csv")
data$a <- factor(data$a)
fit <- manova(cbind(y, z) ~ a, data = data)
summary(fit, test = "Pillai")
```

`factor` کد گروه را دسته‌ای می‌کند. `cbind` دو پاسخ را به ستون‌های یک ماتریس می‌چسباند. در سمت راست `~` عامل مدل قرار می‌گیرد. `summary` با `test` مشخص می‌کند جدول بر اساس کدام آماره باشد. در اسکریپت `$stats[effect, ]` فقط ردیف اثر خواسته‌شده را می‌گیرد.

برای مدل دوم، b را هم با `factor` تبدیل کنید و `a*b` را سمت راست بگذارید. این عبارت شامل اثرهای اصلی و a:b است. برای مدل سوم، `data$dy <- data$y - data$y0` و `data$dz <- data$z - data$z0` را محاسبه کنید و `cbind(dy,dz)` را پاسخ بگذارید. اگر پیگیری تک‌متغیره انجام می‌دهید، `summary.aov(fit)` جدول هر پاسخ را جدا می‌دهد. خانواده و تعدیل را هنگام گزارش در نظر بگیرید.

## کنترل خروجی

در مدل پایان، اثر A به Pillai≈۰٫۷۱۹۳۸۶ و F(۲،۲۹)≈۳۷٫۱۷۲ می‌رسد. برای تعامل A×B، Pillai≈۰٫۰۹۴۵۳۰ و P≈۰٫۲۶۱۶۹۷ است. برای تفاوت تغییر A، Pillai≈۰٫۰۰۱۱۶۰ و P≈۰٫۹۸۳۳۱۷ است.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.youtube.com/watch?v=iEBBcckQL0I). متوسط. پس از اجرای یک مدل سادهٔ R، خواندن Pillai، Wilks، Hotelling–Lawley و Roy را ببینید.
- [مرجع نوشتاری](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/summary.manova.html).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
