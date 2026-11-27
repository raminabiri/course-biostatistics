d<-read.csv("data/M82_L1.csv")
risk<-setNames(d$improved/d$n,d$arm)
rd<-risk[["program"]]-risk[["control"]]
stopifnot(abs(rd-1/3)<1e-12)
print(risk)
print(rd)
