<div dir="rtl">

# M04 در Excel

[کاربرگ دوبرگه](M04_module.xlsx) را باز کنید. ستون‌های A تا E در Registry خام‌اند. در F2 بنویسید `=IF(A2=2,100*B2,B2)` و تا ردیف ۴ بکشید. این شرط فقط برای شناسهٔ تأییدشده در این تمرین است. در G2 بنویسید `=IF(D2=-99,"",D2)` تا نمایش فشار گمشده خالی باشد. سپس در H2 بنویسید `=C2/(F2/100)^2`.

در I2 فرمول `=IF(COUNTIF(Labs!$A$2:$A$4,A2)=0,"",AVERAGEIF(Labs!$A$2:$A$4,A2,Labs!$B$2:$B$4))` را وارد کنید. COUNTIF ابتدا وجود آزمایش را می‌سنجد. AVERAGEIF فقط LDLهای همان شناسه را میانگین می‌گیرد. فرمول‌های G2:I2 را پایین ببرید. انتظار داریم قد نفر دوم ۱۶۸، BMI او ۲۶٫۰۴ و LDLها ۱۲۰، ۱۴۰ و خالی باشند.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

**مقدماتی.** در فیلم، پیدا کردن خطا و ساخت ستون محاسبه‌شده را ببینید. فایل درس از فرمول سلول بهره می‌گیرد و بازسازی با Power Query مرحلهٔ بعدی است. [فیلم پاک‌سازی در Excel](https://www.youtube.com/watch?v=x7mzOYEn0XA) · [مرجع توابع آماری Microsoft](https://support.microsoft.com/en-us/excel/statistical-functions-reference)

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
