<div dir="rtl">

# M20 در R

[فایل practice.csv](../data/practice.csv) ۱۵ ردیف دارد. ردیف اول نام ستون‌هاست. group کد روش و value عدد مشاهده‌شده را نشان می‌دهد. پنج مشاهده به هر روش تعلق دارد.

## از خواندن فایل تا تفسیر جدول

در RStudio [فایل تمرین](M20_workshop.R) را باز کنید. از Session → Set Working Directory → Choose Directory پوشهٔ دارای data را انتخاب کنید. Source را بزنید. برای ترمینال، از پوشهٔ ماژول `Rscript --vanilla r/M20_workshop.R` را اجرا کنید.

```r
d <- read.csv("data/practice.csv")
d$group <- factor(d$group)
fit <- aov(value ~ group, data = d)
summary(fit)
oneway.test(value ~ group, data = d, var.equal = FALSE)
TukeyHSD(fit)
```

`factor` به R می‌گوید group دسته‌ای است. در فرمول `value ~ group` در سمت چپ عدد مورد تحلیل است و در سمت راست عاملی که میانگین را مدل می‌کند. `aov` مدل کلاسیک را می‌سازد و `summary` جدول درجات آزادی، مجموع مربعات و P را نشان می‌دهد. `oneway.test` با `var.equal=FALSE` مدل Welch را می‌سازد و درجهٔ آزادی اعشاری را نشان می‌دهد.

در بخش براون–فورسایت اسکریپت، `split` آرایهٔ اندازه‌ها را به گروه تقسیم می‌کند و `sapply(g,var)` واریانس هر گروه را می‌دهد. `pf(...,lower.tail=FALSE)` دنبالهٔ راستِ F را محاسبه می‌کند. در جدول `TukeyHSD`، ردیف C-A، ستون diff و سپس p adj را بخوانید. lwr و upr دو کران فاصلهٔ تعدیل‌شده هستند.

## عددهای کنترل

در مدل کلاسیک F≈۱۰٫۶۶۴ و P≈۰٫۰۰۲۱۸ است. در Welch، F≈۹٫۲۶۶ و P≈۰٫۰۰۹۵۵ است. برای C−A اختلاف ۸٫۸ واحد و در Tukey مقدار P تعدیل‌شده حدود ۰٫۰۰۱۶۹ است.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.youtube.com/watch?v=lpdFr5SZR0Q). در فیلم از حدود ۰:۳۷ اجرای aov و از حدود ۲:۴۸ اجرای TukeyHSD را ببینید.
- [مرجع نوشتاری](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/oneway.test.html).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
