<div dir="rtl">

# M23 در R

[جدول پهن](../data/wide.csv) ۱۲ ردیف دارد. t0c1 یعنی زمان ۰ در شرط ۱، و group کد ثابت هر فرد است. برای تحلیل زمانی در شرط صفر، فقط t0c0، t1c0 و t2c0 را بگیرید. در مدل زمان×شرط همهٔ شش ستون را لازم داریم.

## اجرا و خواندن لایهٔ خطا

[فایل کارگاه](M23_workshop.R) را در RStudio باز کنید. پوشهٔ ماژول را به عنوان پوشهٔ کاری بگذارید و Source را بزنید. در Terminal همان پوشه می‌توانید `Rscript --vanilla r/M23_workshop.R` را اجرا کنید.

```r
long <- read.csv("data/practice.csv")
long$id <- factor(long$id)
long$time <- factor(long$time)
long$condition <- factor(long$condition)
model <- aov(value ~ time * condition + Error(id / (time * condition)), data = long)
summary(model)
```

`factor` کدها را دسته‌ای می‌کند. `time * condition` دو اثر اصلی و تعاملشان را به مدل می‌برد. `Error(id / (time * condition))` لایه‌های خطا را با شناسهٔ فرد و ترکیب عوامل درون‌فردی تعیین می‌کند. جدول `Error: id:time:condition` برای خواندن تعامل اول است.

در مدل آمیخته، `subset(long, condition == 0)` شرط صفر را نگه می‌دارد. `group * time` اثر گروه و زمان و تعامل را می‌سازد. `Error(id / time)` خطای زمان در فرد را مشخص می‌کند. ردیف group:time را در جدول Error: id:time ببینید.

برای تغییر فردی، از همان ردیف دو ستون کم می‌شوند. `wide$change[wide$group == 1]` شش تغییر گروه ۱ را می‌گیرد. t.test گروه ۱ را اول می‌گیرد و `var.equal = TRUE` برابری واریانس تغییرها را فرض می‌کند. با دیدن فاصلهٔ تکی ۹۵٪، جهت و عدم‌قطعیت نتیجه را گزارش کنید.

## کنترل نتیجه

زمان×شرط با فرض کرویت F(۲،۲۲)≈۴٫۱۵۳ و P≈۰٫۰۲۹۵۰ است. زمان×گروه در شرط ۰ با فرض کرویت F(۲،۲۰)≈۳٫۳۴۸ و P≈۰٫۰۵۵۷۰ است. تفاوت تغییر شروع تا پایان در شرط ۰، گروه ۱ منهای ۰، حدود ۳٫۴۱۷ و P≈۰٫۰۱۲۷۳ با فرض واریانس مشترک است.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.youtube.com/watch?v=wL0MVlusawY). متوسط. آموزش دانشگاه Liverpool ساخت مدل تکراری دوطرفه را نشان می‌دهد. نحو مدل و طبقهٔ خطای کد کارگاه را از متن زیر دنبال کنید.
- [مرجع نوشتاری](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/aov.html).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
