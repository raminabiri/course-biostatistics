<div dir="rtl">

# M23 در SPSS

[جدول پهن](../data/wide.csv) ۱۲ ردیف دارد. t0c1 یعنی زمان ۰ در شرط ۱، و group کد ثابت هر فرد است. برای تحلیل زمانی در شرط صفر، فقط t0c0، t1c0 و t2c0 را بگیرید. در مدل زمان×شرط همهٔ شش ستون را لازم داریم.

## دو عامل درون‌فردی

۱. دادهٔ پهن را با File → Import Data → CSV Data و جداکنندهٔ Comma وارد کنید. در Variable View نام ستون‌ها و عددی بودن شش اندازه را کنترل کنید.

۲. از Analyze → General Linear Model → Repeated Measures، ابتدا time با ۳ سطح و بعد condition با ۲ سطح را Add کنید. Define را بزنید. t0c0، t0c1، t1c0، t1c1، t2c0 و t2c1 را به همان ترتیب بگذارید. در این فهرست شرط با هر خانه تغییر می‌کند و زمان پس از هر دو شرط عوض می‌شود. جدول Within-Subjects Factors ترتیب را نشان می‌دهد.

۳. در Tests of Within-Subjects Effects، time*condition را بخوانید. از Sphericity Assumed برای مطابقت با عدد کلاسیک کارگاه کمک بگیرید. Error مربوط به همان اثر مخرج را نشان می‌دهد.

## طرح آمیخته و کنتراست

برای مدل دوم، فقط time با سه سطح را بسازید. سه ستون c0 را به ترتیب در Within-Subjects Variables و group را در Between-Subjects Factor(s) بگذارید. ردیف time*group را در Tests of Within-Subjects Effects پیدا کنید. اگر کرویت را طبق برنامه بازبینی می‌کنید، ردیف گرین‌هاوس–گایزر همان اثر را بخوانید.

برای تفاوت تغییر، از Transform → Compute Variable متغیر change=t2c0−t0c0 بسازید. در Analyze → Compare Means → Independent-Samples T Test، change را متغیر آزمون و group را عامل دو گروه قرار دهید. ترتیب ۱ و ۰ و ردیف Equal variances assumed برای کنترل کارگاه مهم‌اند.

[فایل Syntax](M23_module.sps) این سه تحلیل را اجرا می‌کند. مسیر FILE را در صورت نیاز کامل کنید و Run → All را بزنید. نام group_id در فایل فرمان از همان ستون group خوانده می‌شود. [فرمان PSPP](M23_pspp.sps) دو آزمون زمان با فرض کرویت و آزمون t را با مدل معادل و [جدول اختلاف‌های آماده](../data/condition-differences.csv) بازتولید می‌کند.

## کنترل نتیجه

زمان×شرط با فرض کرویت F(۲،۲۲)≈۴٫۱۵۳ و P≈۰٫۰۲۹۵۰ است. زمان×گروه در شرط ۰ با فرض کرویت F(۲،۲۰)≈۳٫۳۴۸ و P≈۰٫۰۵۵۷۰ است. تفاوت تغییر شروع تا پایان در شرط ۰، گروه ۱ منهای ۰، حدود ۳٫۴۱۷ و P≈۰٫۰۱۲۷۳ با فرض واریانس مشترک است.

<details>
<summary>فیلم و مرجع نوشتاری</summary>

- [فیلم آموزشی](https://www.youtube.com/watch?v=Xa2Ebfnr22M). متوسط. پس از شناخت عامل درون‌فردی، مراحل تعریف زمان و عامل گروه و خواندن تعامل را ببینید.
- [مرجع نوشتاری](https://www.ibm.com/docs/en/spss-statistics/30.0.0?topic=reference-glm-repeated-measures).

</details>

[بازگشت به درس](../lessons/README.md) · [پاسخ‌ها](../solutions/module.md)

</div>
