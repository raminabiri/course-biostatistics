d <- read.csv("data/M64_L2.csv")
null <- dbinom(d$k,d$n,.5)
alternative <- 1/(d$n+1)
bf <- alternative/null
stopifnot(abs(bf - 128/165) < 1e-12)
print(c(null=null, alternative=alternative, BF10=bf, posterior=bf/(1+bf)))
