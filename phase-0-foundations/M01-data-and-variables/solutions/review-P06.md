# پاسخ تمرین 6 — review

[بازگشت به تمرین‌ها](../review.md)

| پرسش | جواب | راهنما |
|---|---|---|
| پ۶ | **1** | جدول توافقی ward × severity: ICU ← خفیف 2، متوسط 3، شدید 1 |
| پ۷ | **4** | جدول توافقی organism × cipro_res: Klebsiella ← حساس 5، مقاوم 4 |
| پ۸ | **27** | ۳۰ − ۲ (CRP گمشده: بیماران ۷ و ۱۹) − ۱ (WBC گمشده: بیمار ۱۲) |
| پ۹ | **3** | بیماران با los > 7 (بیماران ۷، ۱۲ و ۱۵ با 13، 8 و 12 روز) |

**دستورها در هر نرم‌افزار:**

| | SPSS | Prism | R | Python | Excel |
|---|---|---|---|---|---|
| پ۶، پ۷ | `CROSSTABS /TABLES=ward BY severity.` | شمارش در Excel (PivotTable) ← جدول Contingency | `table(uti$ward, uti$severity)` | `pd.crosstab(uti["ward"], uti["severity"])` | `COUNTIFS(D2:D31,3,J2:J31,3)` یا PivotTable |
| پ۸ | `COUNT nmiss = crp wbc (MISSING).` سپس `FREQUENCIES nmiss.` (n با nmiss = 0) | ستون‌ها را مرتب کنید و سطرهای کامل را بشمارید | `sum(complete.cases(uti))` | `uti.dropna().shape[0]` یا `uti.notna().all(axis=1).sum()` | `=30-COUNTIF(G2:G31,-99)-COUNTBLANK(H2:H31)` (چون هیچ بیماری هر دو را گمشده ندارد) |
| پ۹ | `COMPUTE long_stay = los > 7.` سپس `FREQUENCIES long_stay.` | Frequency distribution روی los یا مرتب‌سازی | `sum(uti$los > 7)` | `(uti["los"] > 7).sum()` | `=COUNTIF(K2:K31,">7")` |

[بازگشت به تمرین‌ها](../review.md)
