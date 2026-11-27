d <- read.csv("data/M07_module.csv")
tab <- xtabs(count~center+status,d)
valid <- tab[,c("positive","negative")]
rates <- prop.table(valid,1)[,"positive"]
bounds <- c(tab["A","positive"],tab["A","positive"]+tab["A","unknown"])/sum(tab["A",])
stopifnot(all(rates==c(.3,.4)),sum(tab[,"unknown"])==10,all(bounds==c(.24,.44)))
print(tab)
print(rates)
print(c(overall=sum(valid[,"positive"])/sum(valid),A_among_positive=12/20,bounds))
