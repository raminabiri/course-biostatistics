d<-read.csv("data/P03.csv")
f<-summary(aov(signal~factor(dose),d))[[1]][1,"F value"]
slope<-unname(coef(lm(signal~dose,d))[2])
stopifnot(abs(f-32)<1e-10,abs(slope-4)<1e-10)
print(c(F=f,slope=slope))
