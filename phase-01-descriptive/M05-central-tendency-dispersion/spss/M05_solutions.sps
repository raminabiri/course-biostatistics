* =============================================================.
* ماژول M05 — شاخص‌های مرکزی و پراکندگی | مسیر SPSS | حل تمرین‌های عملی ع۱ تا ع۷.
* خط CD را به مسیر پوشهٔ data تغییر دهید.
* =============================================================.
CD 'C:\biostat\phase-01-descriptive\M05-central-tendency-dispersion\data'.

GET DATA /TYPE=TXT /FILE='M05_lipid.csv' /ENCODING='UTF8'
  /DELIMITERS="," /ARRANGEMENT=DELIMITED /FIRSTCASE=2
  /VARIABLES= id F3.0 sex A1 age F3.0 sbp F4.0 ldl F4.0 hdl F4.0 hscrp F5.1 cigs F3.0.
DATASET NAME lipid WINDOW=FRONT.
VARIABLE LEVEL sex (NOMINAL) /age sbp ldl hdl hscrp cigs (SCALE).

* ---- ع۱ و ع۲: مرکز و پراکندگی ----.
FREQUENCIES VARIABLES=sbp ldl hscrp cigs /FORMAT=NOTABLE
  /STATISTICS=MEAN MEDIAN MODE STDDEV VARIANCE RANGE MINIMUM MAXIMUM SEMEAN.
* انتظار: sbp 130.19 / 130.00 / SD 11.32 / var 128.11 / range 56.
*         ldl 131.08 / 136.50 / SD 31.85 / var 1014.42 / range 145.
*         hscrp 3.11 / 1.75؛ نمای cigs = 0.

* ---- ع۳: ضریب تغییرات (SPSS مستقیم نمی‌دهد؛ با AGGREGATE) ----.
DATASET DECLARE cvtab.
AGGREGATE /OUTFILE=cvtab /BREAK=
  /m_sbp=MEAN(sbp) /s_sbp=SD(sbp) /m_ldl=MEAN(ldl) /s_ldl=SD(ldl) /m_crp=MEAN(hscrp) /s_crp=SD(hscrp).
DATASET ACTIVATE cvtab.
COMPUTE cv_sbp = 100 * s_sbp / m_sbp.
COMPUTE cv_ldl = 100 * s_ldl / m_ldl.
COMPUTE cv_crp = 100 * s_crp / m_crp.
EXECUTE.
LIST cv_sbp cv_ldl cv_crp.
* انتظار: 8.69 24.30 143.87.
DATASET ACTIVATE lipid.

* ---- ع۴: SEM (در خروجی FREQUENCIES بالا: S.E. Mean) ----.
DESCRIPTIVES VARIABLES=sbp ldl /STATISTICS=MEAN STDDEV SEMEAN.
* انتظار: SEM ldl 4.60، sbp 1.63.
* بازه‌ها را از روی خروجی حساب کنید: 131.08 ± 2×31.85 و 131.08 ± 2×4.60.

* ---- ع۵: به تفکیک جنس ----.
MEANS TABLES=sbp ldl hdl BY sex /CELLS=COUNT MEAN STDDEV.
* انتظار: زنان n 16، sbp 127.94 (9.28)؛ مردان HDL 45.84 (8.98).

* ---- ع۶: hsCRP چوله ----.
MEANS TABLES=hscrp /CELLS=MEAN MEDIAN GEOMETRIC.
EXAMINE VARIABLES=hscrp /PERCENTILES(25,50,75) /PLOT=NONE /STATISTICS=NONE.
* انتظار: میانگین 3.11، میانه 1.75، هندسی 1.85.
* EXAMINE به‌طور پیش‌فرض روش HAVERAGE (Weighted Average، تعریف ۶) را به کار می‌برد: Q1 = 1.000، Q3 = 3.375.

* ---- ع۷: دادهٔ پرصفر ----.
COMPUTE smoker = (cigs > 0).
EXECUTE.
FREQUENCIES VARIABLES=smoker.
TEMPORARY.
SELECT IF (cigs > 0).
FREQUENCIES VARIABLES=cigs /FORMAT=NOTABLE /STATISTICS=MEAN MEDIAN.
* انتظار: 15 سیگاری (31.3٪)؛ در سیگاری‌ها میانه 15، میانگین 16.
