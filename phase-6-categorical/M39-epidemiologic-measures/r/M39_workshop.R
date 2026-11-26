d <- read.csv("data/M39_risk.csv")
risk <- d$events/d$total
odds <- risk/(1-risk)
cat("L1:",risk[1]-risk[2],risk[1]/risk[2],odds[1]/odds[2],
    ceiling(prod(d$total)/(d$events[2]*d$total[1]-d$events[1]*d$total[2])),"\n")
d <- read.csv("data/M39_followup.csv")
print(data.frame(group=d$group, incidence=d$events/d$eligible,
                 rate=100*d$events/d$person_years, prevalence=d$existing/d$census))
d <- read.csv("data/M39_standard.csv")
direct <- indirect <- numeric(2)
for (i in 1:2) {
  s <- d[d$group==c("A","B")[i],]
  direct[i] <- sum(s$events/s$population*s$standard_population)/sum(s$standard_population)
  indirect[i] <- sum(s$events)/sum(s$population*s$reference_risk)
}
cat("L3:",direct,indirect,"\n")
stopifnot(isTRUE(all.equal(direct,c(.13,.104))),abs(indirect[2]-.8)<1e-12)
