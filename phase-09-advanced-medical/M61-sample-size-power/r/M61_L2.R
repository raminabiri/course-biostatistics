p <- power.prop.test(p1=.2,p2=.3,power=.8)$n
c <- 3+((qnorm(.975)+qnorm(.8))/atanh(.3))^2
a <- power.anova.test(groups=3,between.var=4,within.var=25,power=.8)$n
print(c(proportion=p,correlation=c,anova=a))
stopifnot(all(ceiling(c(p,c,a))==c(294,85,32)))
