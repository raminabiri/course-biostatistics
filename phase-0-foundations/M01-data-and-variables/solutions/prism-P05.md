# پاسخ تمرین 5 — prism

[بازگشت به تمرین‌ها](../prism/README.md)

جدول Contingency **شمارش** می‌خواهد، نه دادهٔ خام. پس:

1. در Excel با PivotTable (Rows = sex، Columns = cipro_res، Values = Count of id) یا مرتب‌سازی، شمارش‌ها را پیدا کنید.
2. Prism: New Data Table ← **Contingency** ← Create.
3. Row titles: Female، Male | Column titles: Susceptible، Resistant | خانه‌ها:

| | Susceptible | Resistant |
|---|---|---|
| Female | 13 | **7** |
| Male | 6 | 4 |

**جواب: ۷ بیمار زن مقاوم بودند.** همین جدول در M35 با کای‌دو و آزمون دقیق فیشر تحلیل می‌شود.

[بازگشت به تمرین‌ها](../prism/README.md)
