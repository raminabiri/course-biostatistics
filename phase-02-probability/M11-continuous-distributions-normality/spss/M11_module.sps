DATA LIST FREE / example.
BEGIN DATA
1
END DATA.
COMPUTE pnormal=CDF.NORMAL(110,100,10).
COMPUTE medianlog=EXP(LN(10)).
COMPUTE psurvival=EXP(-.25*4).
COMPUTE tcritical=IDF.T(.975,9).
FORMATS pnormal medianlog psurvival tcritical (F10.6).
LIST VARIABLES=pnormal medianlog psurvival tcritical.
