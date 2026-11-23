# M09 در SPSS | از چهار سطر تا جدول هزارنفری

۱. [CSV](../data/M09_screening.csv) را با **File → Import Data → CSV Data** وارد کنید. سطر اول نام ستون‌هاست. در Variable View، reference و test از نوع String و count از نوع Numeric هستند.
۲. در **Data → Weight Cases** گزینهٔ **Weight cases by** را بزنید و count را وارد کنید. حالا سطر اول نمایندهٔ ۹۰ نفر است. اگر این مرحله را جا بیندازید، هر خانه یک نفر حساب می‌شود و جدول به ۴ می‌رسد.
۳. در **Analyze → Descriptive Statistics → Crosstabs** ستون reference را در Rows و test را در Columns قرار دهید. در **Cells** گزینه‌های Observed، Row و Column را علامت بزنید. OK را بزنید. جمع کل ۱۰۰۰ است. جای ردیف بیماری را با برچسب positive پیدا کنید. ترتیب نرم‌افزار ممکن است اول negative باشد.
۴. در خانهٔ positive/positive شمار ۹۰، درصد سطری ۹۰٪ و درصد ستونی ۵۰٪ را بخوانید. برای احتمال اجتماع، تنها خانهٔ negative/negative را از کل کنار بگذارید. ۱۹۰/۱۰۰۰=۱۹٪.
۵. برای سناریوی شیوع تازه، وزن‌دهی را از **Data → Weight Cases → Do not weight cases** خاموش کنید. در **Transform → Compute Variable** نام p را در Target Variable و `.01` را در Numeric Expression بگذارید. با Compute تازه، ppv را با `(.9*p)/(.9*p+.1*(1-p))` بسازید. عدد در هر ردیف تکرار می‌شود چون ورودی‌ها ثابت‌اند. در Data View باید حدود ۰٫۰۸۳۳ ببینید. اگر فقط ۰٫۰۸ می‌بینید، Decimals را در Variable View افزایش دهید.
۶. فایل داده را sav و خروجی را از پنجرهٔ Output به صورت spv ذخیره کنید. کنار فایل بنویسید وزن‌گذاری برای جدول فعال و برای محاسبهٔ مدل خاموش شده بود.

[کارگاه](../software-workshop.md) · [منابع و فیلم](../references.md#software-media)
