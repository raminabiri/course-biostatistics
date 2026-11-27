<div dir="rtl">

# M24 در R

[practice.csv](../data/practice.csv) ۲۴ مشاهده دارد. برای مرحلهٔ نخست فقط ۱۲ ردیف b=0 را بگیرید. x خط پایه منهای ۲۴ است. در تحلیل سوم، [جدول change.csv](../data/change.csv) را جدا باز کنید و ستون change را پاسخ بگذارید.

## خواندن داده و پیدا کردن اختلاف

از RStudio، [اسکریپت](M24_workshop.R) را باز کنید. پوشهٔ ماژول را به عنوان Working Directory انتخاب و Source را بزنید. در Terminal همان پوشه از `Rscript --vanilla r/M24_workshop.R` کمک بگیرید.

```r
d <- read.csv("data/practice.csv")
d$x <- d$baseline - 24
b0 <- subset(d, b == 0)
fit <- lm(value ~ a + x, data = b0)
predict(fit, newdata = data.frame(a = 0:1, x = 0))
confint(fit)["a", ]
```

`lm` مدل خطی را می‌سازد. در فرمول، سمت چپ پاسخ و سمت راست پیش‌بین‌ها هستند. `newdata` ردیف‌های تازه‌ای با x صفر می‌سازد. `0:1` کد هر دو شیوه را وارد و `predict` پیش‌بینی در همان خط پایه را می‌دهد. `confint(fit)["a", ]` ردیف فاصلهٔ ضریب a را برمی‌دارد.

در L2، `a*b` دو اثر اصلی و تعاملشان را دارد. برای آزمون تغییر شیب، `a*b*x` همهٔ جمله‌های پایین‌تر و تعامل سه‌طرفه را وارد می‌کند. `anova(small, common)` و سپس `anova(common, varying)` کاهش مجموع مربعات مانده‌ها و P را نشان می‌دهند. در L3، `read.csv` فایل جداگانهٔ change را می‌خواند و `coef(change_model)["a"]` ضریب همان سناریو را می‌دهد. خروجی‌ها را با نام پاسخ value یا change نگه دارید.

## کنترل نتیجه

در B0، پایان تعدیل‌شده برای A0 و A1 برابر ۴۸٫۹۴۳ و ۵۱٫۲۸۶ و فاصلهٔ ۹۵٪ اختلاف ۰٫۶۷۲ تا ۴٫۰۱۴ است. در همهٔ ردیف‌ها، F تعامل A×B≈۱٫۰۵۲ و P≈۰٫۳۱۸ هستند. برای تغییر، اختلاف ۱٫۴۴۳، بازهٔ ۹۵٪ از −۰٫۶۷۶ تا ۳٫۵۶۲ و P≈۰٫۱۵۷۸ است.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.youtube.com/watch?v=OqBiCb1GjgE). متوسط. فیلم اجرای ANCOVA و گزارش آن در RStudio را نشان می‌دهد. در این درس lm و مقایسهٔ دو مدل تودرتو مستقیم اجرا می‌شوند.
- [مرجع نوشتاری](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/anova.lm.html).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
