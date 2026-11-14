# پاسخ تمرین 2 — excel

[بازگشت به تمرین‌ها](../excel/README.md)

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

[بازگشت به تمرین‌ها](../excel/README.md)
