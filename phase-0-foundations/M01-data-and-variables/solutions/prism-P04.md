# پاسخ تمرین 4 — prism

[بازگشت به تمرین‌ها](../prism/README.md)

1. یک جدول Column با ستون `ward_code` (۳۰ کد) ← Descriptive statistics ← **Mean = 1.800**. Prism نمی‌داند این‌ها کدند؛ ۱٫۸ هیچ بخش واقعی‌ای نیست (درس ۱.۲، دام ۱).
2. Analyze ← Column analyses ← **Frequency distribution** ← Bin width = **1** (و مرکز اولین بین = 1) ← Tabulate: **Number of values**:

| Bin center | Frequency |
|---|---|
| 1 (Internal) | 12 |
| 2 (Surgery) | 12 |
| 3 (ICU) | 6 |

3. **organism** متنی است و Frequency distribution فقط عدد می‌پذیرد. راه ساده در Prism: داده را در Excel بر اساس `organism` مرتب کنید و `age` هر گروه را در یک جدول Column با سه ستون (E. coli، Klebsiella، Proteus) بچسبانید (سن گمشده ندارد). در Descriptive statistics، Number of values هر ستون:
   **E. coli = 17، Klebsiella = 9، Proteus = 4**.
   (یا مستقیم در Excel با `COUNTIF`. این یکی از محدودیت‌های Prism برای کار با دادهٔ کیفی خام است.)

[بازگشت به تمرین‌ها](../prism/README.md)
