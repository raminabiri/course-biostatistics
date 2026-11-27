<div dir="rtl">

# M31 در R

[دادهٔ پایه](../data/practice.csv) هفت مقدار A و هفت B دارد. [دادهٔ افزوده](../data/extended.csv) ۲۴ مشاهده در هر گروه و مقدارهای مساوی دارد. جهت برآورد در این درس A−B است.

## اجرا و تفسیر U

[اسکریپت](M31_workshop.R) را از پوشهٔ ماژول در RStudio باز کنید. Session → Set Working Directory و سپس Source را بزنید. در Terminal از `Rscript --vanilla r/M31_workshop.R` کمک بگیرید.

`a <- d$value[d$group=="A"]` فقط ردیف‌های A را برمی‌دارد. `wilcox.test(a,b,exact=TRUE,correct=FALSE)` در فایل پایه آزمون دقیق می‌دهد. در افزوده `exact=FALSE` و اصلاح پیوستگی خاموش است. آماره در R با W برچسب می‌خورد و در این طرح همان U گروه نخست است.

## شکل توزیع، میانه و برآورد

`sort(unique(c(a,b)))` آستانه‌ها را یکتا و مرتب می‌کند. `tabulate` تعداد هر آستانه و `cumsum` شمار تجمعی را می‌دهد. در تابع `ks_permutation` یک بردار شمار مسیرها داریم. در دستهٔ هم‌ارزش، `choose(m,k)` راه‌های قرار دادن k برچسب A میان m مشاهده را وزن می‌دهد. مسیرهای با فاصلهٔ کمتر از دیده‌شده نگه داشته می‌شوند.

`outer(a,b,"-")` شبکهٔ تفاضل‌ها و `median` میانهٔ شبکه را می‌دهد. `table(d$group,d$value>median(d$value))` گروه و وضعیت بالای میانه را می‌شمارد. `fisher.test(tab)` احتمال دقیق دوطرفه را محاسبه می‌کند.

## کنترل خروجی

پایه، U_A=۳۲ و P دقیق≈۰٫۳۸۲۸۶۷، D=۲/۷ و P دقیق≈۰٫۹۶۲۷۰۴، HL=۲ و P فیشر=۱. افزوده، U_A=۳۵۷ و P تقریبی بدون اصلاح پیوستگی≈۰٫۱۵۴۱۲۳، D≈۰٫۲۰۸۳۳۳ و P جایگشتیِ مشروط≈۰٫۵۷۸۴۰۲ است.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.youtube.com/watch?v=KroKhtCD9eE). متوسط. بخش Wilcoxon rank-sum برای داده‌های جدا را پس از شناخت رتبهٔ مشترک ببینید.
- [مرجع نوشتاری](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/wilcox.test.html).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
