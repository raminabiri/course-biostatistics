d<-read.csv("data/M79_L1.csv")
q<-p.adjust(d$p,"BH")
p<-(2*49+42)/200
expected<-100*c(p^2,2*p*(1-p),(1-p)^2)
stopifnot(sum(q<=.05)==2,max(abs(expected-c(49,42,9)))<1e-10)
print(q)
print(expected)
