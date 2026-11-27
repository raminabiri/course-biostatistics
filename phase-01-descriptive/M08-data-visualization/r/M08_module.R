d <- read.csv("data/M08_followup.csv",na.strings="")
counts <- hist(d$day0, breaks=c(110,130,150,170), right=FALSE, plot=FALSE)$counts
delta <- d$day14-d$day0
stopifnot(all(counts==c(9,6,1)), sum(!is.na(delta))==15, sum(delta,na.rm=TRUE)==-88)
print(counts)
print(c(pairs=sum(!is.na(delta)),change=mean(delta,na.rm=TRUE)))
plot(d$age,d$day0,col=ifelse(d$group=="A","steelblue","darkorange"),
     pch=19,xlab="Age (years)",ylab="Day 0 pressure (mmHg)")
