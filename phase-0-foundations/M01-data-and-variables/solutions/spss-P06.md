<div dir="rtl">

# پاسخ تمرین 6 — spss

[بازگشت به تمرین‌ها](../spss/README.md)

`Data > Restructure` (گام ۶) یا Syntax:

```
VARSTOCASES /MAKE crp FROM crp_d0 crp_d3 crp_d7 /INDEX=visit(3) /KEEP=id.
RECODE visit (1=0) (2=3) (3=7) INTO day.
EXECUTE.
```

**جواب: ۲۴ سطر** (۸ بیمار × ۳ روز). سه سطر اول: id = 1 با day = 0، 3، 7 و crp = 94.8، 46.2، 12.1.

[بازگشت به تمرین‌ها](../spss/README.md)

</div>
