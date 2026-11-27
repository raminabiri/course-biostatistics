<div dir="rtl">

# M30 در SPSS

[دادهٔ پایه](../data/practice.csv) هشت زوج و دوازده وضعیت دارد. design هر طرح را جدا می‌کند. [دادهٔ افزوده](../data/extended.csv) ۲۴ زوج با صفر و رتبهٔ برابر و ۴۸ وضعیت دارد. تحلیل ترتیب را بر اساس id اجرا کنید.

## آزمون علامت و رتبه‌ای

۱. از File → Import Data → CSV Data و جداکنندهٔ Comma استفاده کنید. برای انتخاب paired، در Data → Select Cases شرط design='paired' را بگذارید. در Transform → Compute Variable می‌توانید diff=after-before بسازید و اولین مقدار −۷ را کنترل کنید.

۲. از Analyze → Nonparametric Tests → Legacy Dialogs → 2 Related Samples، after و before را یک جفت بگذارید. Sign را برای شمار علامت و Wilcoxon را برای رتبه‌ها علامت بزنید. عنوان جدول after−before و تعداد صفرها را بخوانید. P دقیق علامت و مجموع رتبهٔ مثبت باید با درس همخوان باشد.

۳. برای ویلکاکسون به ستون Asymp. Sig. یا Exact Sig. توجه کنید. PSPP در این فایل P تقریبی حدود ۰٫۱۶۱ می‌دهد و W+ همان ۸ است. با امکان Exact Tests می‌توانید مسیر دقیق را جداگانه انتخاب کنید. نام روش باید در گزارش مشخص باشد.

## گردش‌ها

داده را دوباره باز کنید و شرط design='runs' را بگذارید. از Data → Sort Cases با id صعودی استفاده کنید. در Legacy Dialogs → Runs، before و Custom = 0.5 را بگذارید تا صفر و یک جدا شوند. Run Test باید ۸ گردش و تقریب نرمال حدود ۰٫۷۶۲ بدهد. برای P دقیق از کاربرگ کمک بگیرید. [فایل فرمان](M30_module.sps) مسیر پایهٔ هر سه آزمون را اجرا می‌کند. مسیر FILE را کامل کنید و Run → All را بزنید.

## کنترل خروجی

پایه، علامت: ۳ مثبت، ۵ منفی و P دوطرفهٔ ۰٫۷۲۶۵۶۳. ویلکاکسون: W+=۸ و P دقیق ۰٫۱۹۵۳۱۳. گردش: ۸ گردش و P دقیق ۰٫۷۸۳۵۵۰. افزوده، ۸ مثبت، ۱۴ منفی و ۲ صفر، W+=۸۴ و P تقریبی ۰٫۱۶۶۱۹۳ و ۱۴ گردش با P دقیق ۰٫۰۰۱۹۲۷.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://guides.lib.uoguelph.ca/c.php?g=525348&p=5374874). متوسط. ویدئوی Wilcoxon Signed Rank Test دانشگاه Guelph را برای تنظیم آزمون ناپارامتری ببینید. نام و جهت جفت‌ها در فرمان کارگاه آمده‌اند.
- [مرجع نوشتاری](https://www.ibm.com/docs/en/spss-statistics/30.0.0?topic=reference-npar-tests).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
