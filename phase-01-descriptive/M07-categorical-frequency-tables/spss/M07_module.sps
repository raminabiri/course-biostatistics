DATA LIST FREE / center status freq.
BEGIN DATA
1 1 12
1 0 28
1 9 10
2 1 8
2 0 12
END DATA.
VALUE LABELS center 1 'A' 2 'B' /status 0 'Negative' 1 'Positive' 9 'Unknown'.
WEIGHT BY freq.
CROSSTABS /TABLES=center BY status /CELLS=COUNT ROW COLUMN.
TEMPORARY.
SELECT IF status<>9.
CROSSTABS /TABLES=center BY status /CELLS=COUNT ROW COLUMN.
WEIGHT OFF.
