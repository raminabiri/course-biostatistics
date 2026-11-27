<div dir="rtl">

# پاسخ تمرین 4 — excel

[بازگشت به تمرین‌ها](../excel/README.md)

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

[بازگشت به تمرین‌ها](../excel/README.md)

</div>
