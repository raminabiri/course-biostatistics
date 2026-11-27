<div dir="rtl">

# M22 در R

از [جدول پهن](../data/wide.csv) ستون‌های id، t0c0، t1c0 و t2c0 را پیدا کنید. هر ردیف یک فرد است. هر سه اندازه باید برای همان ردیف کنار هم بمانند. شرط صفر همان c0 در نام ستون‌هاست.

## اجرای اسکریپت

در RStudio، [فایل کارگاه](M22_workshop.R) را باز کنید. از Session → Set Working Directory → Choose Directory، پوشهٔ دارای data را انتخاب و Source را بزنید. در Terminal همان پوشه، فرمان `Rscript --vanilla r/M22_workshop.R` را اجرا کنید. جدول و نام مقایسه‌ها در Console یا Terminal دیده می‌شوند.

```r
long <- read.csv("data/practice.csv")
data <- subset(long, condition == 0)
data$id <- factor(data$id)
data$time <- factor(data$time)
counts <- xtabs(~ id + time, data)
stopifnot(all(counts == 1), !anyNA(data$value))
model <- aov(value ~ time + Error(id / time), data = data)
summary(model)
```

`subset` شرط صفر را جدا می‌کند و `factor` شناسه و زمان را به برچسب گروه تبدیل می‌کند. `xtabs` جدول شمارش فرد و زمان را می‌سازد. `stopifnot` بررسی می‌کند هر خانه دقیقاً یک مشاهدهٔ کامل دارد. در `aov`، بخش `Error(id / time)` سطح‌های خطا را مشخص می‌کند. برای زمان از خروجی Error: id:time بخوانید.

## بازبینی و مقایسه

`sweep` میانگین هر فرد و سپس هر زمان را از خانه‌های متناظر کم می‌کند. با `cov(cbind(u,v))` ماتریس واریانس و کوواریانس دو کنتراست ساخته می‌شود. `diag(s)` قطر ماتریس را برمی‌گرداند. `pf(..., lower.tail = FALSE)` احتمال بزرگ‌تر از F با درجات آزادی تازه را می‌دهد.

در بخش پایانی، `t.test(..., paired = TRUE)` هر جفت را از ردیف‌های متناظر می‌سنجد. `p.adjust(p, "holm")` تعدیل را روی همان سه P اعمال می‌کند. برای T2−T0، نشانهٔ مثبت mean difference و کران‌های فاصلهٔ تکی را با درس مقایسه کنید. اگر خواستید خروجی نگه داشته شود، در فرمان Terminal پس از نام فایل `> M22-output.txt` بنویسید.

## کنترل نتیجه

F(۲،۲۲)≈۲۵٫۱۰۹۶ و P خام زمان ≈۰٫۰۰۰۰۰۲۰۹۶ است. ضریب گرین‌هاوس–گایزر ≈۰٫۹۰۴۵۶۵ و P بازبینی‌شده ≈۰٫۰۰۰۰۰۵۶۵۵ است. تغییر T2−T0 برابر ۵٫۲۰۸۳ و P خام زوجی ≈۰٫۰۰۰۰۲۲۹۱۴ است.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.youtube.com/watch?v=iR7NqJL-7Vk). متوسط. پس از تمرین مدل M20، فیلم را برای تحلیل زمان در دادهٔ تکراری ببینید. محاسبهٔ ضریب گرین‌هاوس–گایزر در اسکریپت همین ماژول آمده است.
- [مرجع نوشتاری](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/aov.html).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
