<div dir="rtl">

# M30 در GraphPad Prism

[دادهٔ پایه](../data/practice.csv) هشت زوج و دوازده وضعیت دارد. design هر طرح را جدا می‌کند. [دادهٔ افزوده](../data/extended.csv) ۲۴ زوج با صفر و رتبهٔ برابر و ۴۸ وضعیت دارد. تحلیل ترتیب را بر اساس id اجرا کنید.

## ویلکاکسون برای زوج‌ها

۱. از File → New Project نوع Column را بگیرید. دو ستون after و before بسازید. در هر ردیف دو اندازهٔ همان id قرار می‌گیرند. در Analyze → t tests و سپس Paired، آزمون Wilcoxon matched pairs را انتخاب کنید.

۲. در Results بررسی کنید ترتیب اختلاف after−before است. تعداد غیرصفر هشت و رتبهٔ مثبت ۸ است. P دقیق پایه نزدیک ۰٫۱۹۵۳ است. برای دادهٔ افزوده نسخهٔ Prism ممکن است روش دقیقِ دارای رتبهٔ مساوی را به کار ببرد. نام روش را کنار P بنویسید. این مقدار را با تقریب R و Python فقط بعد از بررسی روش مقایسه کنید.

## علامت و ترتیب وضعیت‌ها

برای فایل پایه و آزمون علامت، سه مثبت و پنج منفی داریم. در Prism 11 یک جدول XY یک‌ردیفی با Y=۵ بسازید. در Analyze → Transform و User-defined، فرمول `Y=BINOMIAL(Y,8,0.5)` را بزنید. تابع احتمال دست‌کم پنج موفقیت را می‌دهد. به دلیل تقارن در p=۰٫۵، این همان احتمال حداکثر سه مثبت است. برای P دوطرفهٔ پایه آن را دو برابر کنید. [مرجع تابع‌ها](https://www.graphpad.com/guides/prism/latest/user-guide/available_functions_transforms_table.htm)

برای دیدن گردش‌ها X=id و Y=before را با دادهٔ runs بسازید. نقاط را بر اساس id وصل کنید تا تغییر حالت‌ها دیده شوند. برای P دقیق، از [برگهٔ Runs](../excel/M30_module.xlsx) یا [روش Python](../python/MODULE.md) کمک بگیرید.

## کنترل خروجی

پایه، علامت: ۳ مثبت، ۵ منفی و P دوطرفهٔ ۰٫۷۲۶۵۶۳. ویلکاکسون: W+=۸ و P دقیق ۰٫۱۹۵۳۱۳. گردش: ۸ گردش و P دقیق ۰٫۷۸۳۵۵۰. افزوده، ۸ مثبت، ۱۴ منفی و ۲ صفر، W+=۸۴ و P تقریبی ۰٫۱۶۶۱۹۳ و ۱۴ گردش با P دقیق ۰٫۰۰۱۹۲۷.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.graphpad.com/series/key-analysis-t-test). مقدماتی. بخش ورود دو ستون جفت‌شده را ببینید. گزینهٔ آزمون رتبه‌ای را طبق راهنمای نوشتاری انتخاب کنید.
- [مرجع نوشتاری](https://www.graphpad.com/guides/prism/latest/statistics/stat_how_to_do_an_unpaired_t_test_w_3_2.htm).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
