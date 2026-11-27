d <- read.csv("data/M36_practice.csv")
stopifnot(nrow(d)==120, !anyDuplicated(d$id))
s <- d$dose-mean(d$dose)
p <- mean(d$total_response)
z <- sum(s*d$total_response)/sqrt(p*(1-p)*sum(s^2))
r <- cor(d$dose,d$response)
x2 <- (nrow(d)-1)*r^2
tab <- with(d, table(dose,response))
concordant <- discordant <- 0
for (i in 1:2) for (ii in (i+1):3) {
  for (j in 1:2) for (jj in (j+1):3) {
    concordant <- concordant + tab[i,j]*tab[ii,jj]
    discordant <- discordant + tab[i,jj]*tab[ii,j]
  }
}
gamma <- (concordant-discordant)/(concordant+discordant)
cat("L1:",z,pnorm(z,lower.tail=FALSE),2*pnorm(-abs(z)),"\n")
cat("L2:",r,x2,pchisq(x2,1,lower.tail=FALSE),"\n")
cat("L3:",concordant,discordant,gamma,"\n")
stopifnot(concordant==2356,discordant==876,abs(z-3.1749015733)<1e-9)
