d<-read.csv("data/P01.csv")
t<-table(d$mobility_issue,d$delayed)
risk<-prop.table(t,1)[,"1"]
stats<-c(RD=unname(risk["1"]-risk["0"]),RR=unname(risk["1"]/risk["0"]),OR=t["1","1"]*t["0","0"]/(t["1","0"]*t["0","1"]))
stopifnot(abs(stats["RD"]-.3)<1e-12)
print(t)
print(stats)
