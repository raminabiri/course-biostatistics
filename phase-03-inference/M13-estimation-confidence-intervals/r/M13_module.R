se <- 10/sqrt(25)
width <- qt(.975,24)*se
p <- 18/30
z <- qnorm(.975)
center <- (p+z^2/60)/(1+z^2/30)
half <- z*sqrt(p*(1-p)/30+z^2/3600)/(1+z^2/30)
v <- c(se,100-width,100+width,p,center-half,center+half,105-100,sqrt(8))
stopifnot(max(abs(v-c(2,95.8722028767,104.1277971233,0.6,0.4232036025,0.7540937188,5,2.8284271247)))<1e-6)
print(v)
