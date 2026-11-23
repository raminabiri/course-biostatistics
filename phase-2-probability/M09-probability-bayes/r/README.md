# M09 در R | جدول وزنی و احتمال شرطی

در RStudio از **Session → Set Working Directory → Choose Directory** پوشهٔ ماژول را انتخاب کنید. با `file.exists("data/M09_screening.csv")` مسیر را کنترل کنید و `source("r/M09_practice.R")` را در Console اجرا کنید. کد [فایل تمرین](M09_practice.R) با R پایه است.

- `read.csv()` چهار سطر می‌خواند. در `xtabs(count ~ reference + test, d)` مقدار count در سمت چپ، **شمار افراد** است. دو ستون سمت راست نام سطر و ستون‌اند. اگر count را از فرمول حذف کنید هر ردیف وزن یک می‌گیرد.
- `tab["positive","positive"]` خانهٔ اشتراک را با نام سطر و ستون پیدا می‌کند. `sum(tab)` هزار نفر را می‌شمارد. عدد L1، ۰٫۱۹ است.
- `prop.table(tab,1)` جمع سطر را مخرج می‌کند و `prop.table(tab,2)` جمع ستون را. خانهٔ مثبت واقعی در L2 به‌ترتیب ۰٫۹ و ۰٫۵ است.
- در بخش L3، `p <- c(.01,.10)` دو شیوع می‌سازد و عملیات ضرب و تقسیم جداگانه برای هر عضو بردار انجام می‌شود. دو خروجی حدود ۰٫۰۸۳۳ و ۰٫۵‌اند.

برای ذخیره، `out <- capture.output(source("r/M09_practice.R"))` و سپس `writeLines(out,"M09_R.txt")` را اجرا کنید. [کارگاه](../software-workshop.md)
