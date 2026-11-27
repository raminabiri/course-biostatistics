tost <- function(d, se, lower, upper, cdf, quantile, alpha=.05) {
  p_lower <- cdf((d-lower)/se, lower.tail=FALSE)
  p_upper <- cdf((d-upper)/se, lower.tail=TRUE)
  half <- quantile(1-alpha)*se
  c(estimate=d, se=se, p_lower=p_lower, p_upper=p_upper,
    p_tost=max(p_lower,p_upper), lo=d-half, hi=d+half)
}
cat("L1: CI inside margins:", -1.1 > -2 && 1.3 < 2, "\n")
means <- read.csv("data/means.csv")
new <- means$value[means$group_id==1]
reference <- means$value[means$group_id==0]
n1 <- length(new)
n0 <- length(reference)
df <- n1+n0-2
pooled <- ((n1-1)*var(new)+(n0-1)*var(reference))/df
cat("L2: means\n")
print(tost(mean(new)-mean(reference), sqrt(pooled*(1/n1+1/n0)), -2, 2,
           function(x, lower.tail) pt(x, df, lower.tail=lower.tail), function(p) qt(p, df)))
rates <- read.csv("data/proportions.csv")
new <- rates$response[rates$group_id==1]
reference <- rates$response[rates$group_id==0]
p1 <- mean(new)
p0 <- mean(reference)
se <- sqrt(p1*(1-p1)/length(new)+p0*(1-p0)/length(reference))
cat("L3: proportions, unpooled Wald approximation\n")
print(tost(p1-p0, se, -.12, .12, pnorm, qnorm))
