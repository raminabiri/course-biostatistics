se <- 10/sqrt(25)
t <- (104-100)/se
df <- 24
p <- 2*pt(-abs(t),df)
half <- qt(.975,df)*se
v <- c(se,t,df,p,104-half,104+half)
stopifnot(max(abs(v-c(2,2,24,0.0569398499,99.8722028767,108.1277971233)))<1e-6)
print(v)
