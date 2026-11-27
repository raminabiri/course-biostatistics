DATA LIST FREE / arm n improved.
BEGIN DATA
1 6 3
0 6 1
END DATA.
VALUE LABELS arm 1 'Program' 0 'Control'.
COMPUTE risk=improved/n.
LIST VARIABLES=arm n improved risk.
