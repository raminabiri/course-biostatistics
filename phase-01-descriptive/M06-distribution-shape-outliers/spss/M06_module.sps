DATA LIST FREE / wait.
BEGIN DATA
1
2
3
4
5
6
7
8
40
END DATA.
SORT CASES BY wait.
COMPUTE position=$CASENUM.
FORMATS position (F3.0).
TEMPORARY.
SELECT IF ANY(position,3,5,7).
LIST VARIABLES=position wait.
COMPUTE flagged=(wait < -3 OR wait > 13).
COMPUTE log_diff=LN(40/8)/LN(2).
FORMATS log_diff (F8.4).
TEMPORARY.
SELECT IF flagged=1.
LIST VARIABLES=wait flagged log_diff.
