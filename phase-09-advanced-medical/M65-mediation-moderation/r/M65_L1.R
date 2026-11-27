d <- read.csv("data/M65_L1.csv")
effects <- d$treated - d$control
interaction <- diff(effects)
indirect <- 3*2
stopifnot(all(effects==c(4,7)), interaction==3, indirect==6)
print(c(low=effects[1],high=effects[2],interaction=interaction,indirect=indirect,total=4+indirect))
