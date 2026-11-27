x <- read.csv("data/M52_counts.csv")$events
mu <- mean(x)
v <- var(x)
out <- c(mean=mu, variance=v, size=mu^2/(v-mu), observed_zero=mean(x==0),
         poisson_zero=dpois(0,2), inflated_zero=.25+.75*dpois(0,2),
         hurdle_zero=.25, conditional_one=dpois(1,2)/(1-dpois(0,2)))
print(out)
stopifnot(mu==2, mean(x==0)==.4)
