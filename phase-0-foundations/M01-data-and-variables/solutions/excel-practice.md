# پاسخ‌های مسیر excel

<a id="answer-1"></a>

## پاسخ 1

```
=ROWS(uti!A2:A31)     → 30
=COUNTA(uti!A1:L1)    → 12
```
**جواب: ۳۰ سطر، ۱۲ ستون.** راه سریع دیگر: ستون A را انتخاب کنید؛ نوار وضعیت پایین Excel «Count: 31» نشان می‌دهد (۳۰ داده + ۱ سرستون).

<a id="answer-2"></a>

## پاسخ 2

برگهٔ `labels` (ستون‌های D و E ستون کلید و برچسب‌اند):

| variable | code | label | key | label |
|---|---|---|---|---|
| sex | 1 | Female | `=A2&"\|"&B2` ← sex\|1 | Female |
| sex | 2 | Male | sex\|2 | Male |
| ward | 1 | Internal | ward\|1 | Internal |
| ... | | | | |

ستون‌های برچسب در برگهٔ `uti`:
```
M2: =VLOOKUP("sex"&"|"&C2,       labels!$D$2:$E$11, 2, FALSE)
N2: =VLOOKUP("ward"&"|"&D2,      labels!$D$2:$E$11, 2, FALSE)
O2: =VLOOKUP("severity"&"|"&J2,  labels!$D$2:$E$11, 2, FALSE)
P2: =VLOOKUP("cipro_res"&"|"&L2, labels!$D$2:$E$11, 2, FALSE)
```
**کنترل:** سطر بیمار ۱ ← Female، Surgery، Mild، Susceptible. سطر بیمار ۶ ← Male، Internal، Moderate، Resistant.
اگر جایی `#N/A` دیدید، یعنی کدی در داده هست که در برگهٔ برچسب نیست؛ این خودش یک کنترل کیفیت است!

<a id="answer-3"></a>

## پاسخ 3

| محاسبه | فرمول | جواب |
|---|---|---|
| میانگین با ‎-99 | `=AVERAGE(G2:G31)` | **35.10** ✘ |
| میانگین بدون ‎-99 | `=AVERAGEIF(G2:G31,"<>-99")` | **44.68** ✔ |
| CRP معتبر | `=COUNTIFS(G2:G31,"<>-99",G2:G31,"<>")` | **28** |
| WBC معتبر | `=COUNT(H2:H31)` | **29** |

نکته: `AVERAGE` و `COUNT` خانهٔ خالی را خودشان کنار می‌گذارند، ولی ‎-99 را نه.

<a id="answer-4"></a>

## پاسخ 4

`=AVERAGE(D2:D31)` ← **1.8**؛ بی‌معنا، چون 1، 2، 3 برچسب‌اند (درس ۱.۲).

| ward | فرمول | فراوانی |
|---|---|---|
| Internal | `=COUNTIF(D2:D31,1)` | 12 |
| Surgery | `=COUNTIF(D2:D31,2)` | 12 |
| ICU | `=COUNTIF(D2:D31,3)` | 6 |

| organism | فرمول | فراوانی |
|---|---|---|
| E. coli | `=COUNTIF(E2:E31,"E. coli")` | 17 |
| Klebsiella | `=COUNTIF(E2:E31,"Klebsiella")` | 9 |
| Proteus | `=COUNTIF(E2:E31,"Proteus")` | 4 |

PivotTable همین اعداد را می‌دهد. درصد: در PivotTable، `Value Field Settings > Show Values As > % of Grand Total` ← 40٪، 40٪، 20٪.

<a id="answer-5"></a>

## پاسخ 5

```
=COUNTIFS(C2:C31,1, L2:L31,1)    → 7   (زن، مقاوم)
=COUNTIFS(C2:C31,1, L2:L31,0)    → 13  (زن، حساس)
=COUNTIFS(C2:C31,2, L2:L31,1)    → 4   (مرد، مقاوم)
=COUNTIFS(C2:C31,2, L2:L31,0)    → 6   (مرد، حساس)
```
**جواب: ۷.** جمع چهار خانه = ۳۰ (کنترل).

<a id="answer-6"></a>

## پاسخ 6

Power Query: `Unpivot Other Columns` روی همهٔ ستون‌ها به‌جز `id` (گام ۶). یا روش فرمولی برگهٔ `crp_long`.
**جواب: ۲۴ سطر.** سه سطر اول: (1, 0, 94.8)، (1, 3, 46.2)، (1, 7, 12.1)؛ سطر آخر: (8, 7, 6.9).

<a id="answer-7"></a>

## پاسخ 7

- **xlsx:** همهٔ برگه‌ها، فرمول‌ها، Data Validation و PivotTable ها می‌مانند.
- **CSV:** فقط برگهٔ فعال و فقط **مقادیر** می‌ماند؛ برگه‌های `labels` و `codebook`، فرمول‌ها (به عدد ثابت تبدیل می‌شوند)، Data Validation و قالب‌بندی از دست می‌روند.
- **نتیجه:** فایل کاری را xlsx نگه دارید؛ CSV فقط برای **انتقال** داده به نرم‌افزار دیگر است.

