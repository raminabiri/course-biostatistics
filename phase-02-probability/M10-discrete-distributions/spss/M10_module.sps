DATA LIST FREE / example.
BEGIN DATA
1
END DATA.
COMPUTE pbin=PDF.BINOM(2,5,.2).
COMPUTE ppois=PDF.POISSON(3,2).
COMPUTE pnegbin=4*.4**2*.6**3.
COMPUTE phyper=1050/4845.
FORMATS pbin ppois pnegbin phyper (F10.6).
LIST VARIABLES=pbin ppois pnegbin phyper.
