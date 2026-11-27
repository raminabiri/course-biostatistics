<div dir="rtl">

# M27 در R

[practice.csv](../data/practice.csv) ۳۲ ردیف دارد. a و b کد دو عامل، y و z پاسخ پایان و baseline هم‌متغیر است. مدل نخست تنها با B0 اجرا می‌شود. در هر سه مدل از x=baseline−25 کمک می‌گیریم.

## خواندن فایل و پیش‌بینی مشترک

[اسکریپت](M27_workshop.R) را در RStudio از پوشهٔ دارای data باز کنید. با Session → Set Working Directory همان پوشه را مشخص و Source را بزنید. در Terminal از `Rscript --vanilla r/M27_workshop.R` کمک بگیرید.

```r
d <- read.csv("data/practice.csv")
d$a <- factor(d$a)
d$x <- d$baseline - 25
b0 <- subset(d, b == 0)
fit <- manova(cbind(y, z) ~ x + a, data = b0)
summary(fit, test = "Pillai")
predict(fit, data.frame(x = 0, a = factor(c(0, 1), levels = levels(d$a))))
```

`factor` کد A را دسته‌ای می‌کند. `subset` تنها تنظیم صفر را برمی‌دارد. `cbind` دو پاسخ را در یک مدل نگه می‌دارد. در مدل، x پیش از a آمده تا ردیف اثر a پس از x حساب شود. `levels(d$a)` باعث می‌شود دو کد تازه در predict با همان سطح‌های آموزشی خوانده شوند.

برای مدل دوم از `x + a*b` و برای مدل سوم از `x + a*b + a:x` کمک بگیرید. `a*b` هر دو اثر اصلی و تعامل را می‌سازد. `a:x` تنها جملهٔ تعامل شیوه و خط پایه را اضافه می‌کند. در خلاصهٔ مدل سوم ممکن است ترتیب نام تعامل به صورت x:a دیده شود. `coef` دو ستون برآورد را برای خواندن جهت‌ها ارائه می‌کند.

## کنترل خروجی

در B0 و خط پایهٔ ۲۵، بردار پیش‌بینی A0 حدود (۴۴٫۳۶۶،۲۶٫۰۷۳) و A1 حدود (۴۷٫۹۵۵،۲۴٫۰۵۲) است. P آزمون مشترک A≈۰٫۰۱۰۹۶۴، برای A×B≈۰٫۲۷۳۴۶۹ و برای A×خط پایه≈۰٫۲۹۹۳۷۹ است.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.youtube.com/watch?v=iEBBcckQL0I). متوسط. فیلم خواندن جدول MANOVA برای دو پاسخ را نشان می‌دهد. در این ماژول x در سمت راست مدل افزوده می‌شود.
- [مرجع نوشتاری](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/summary.manova.html).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
