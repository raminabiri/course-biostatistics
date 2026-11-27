d <- read.csv("data/M50_pairs.csv")
b <- with(d,sum(pairs[case_exposed==1 & control_exposed==0]))
c <- with(d,sum(pairs[case_exposed==0 & control_exposed==1]))
p <- binom.test(b,b+c)$p.value
print(c(b/c,log(b/c),p))
stopifnot(b+c==16,b/c==3,abs(p-.076812744140625)<1e-12)
