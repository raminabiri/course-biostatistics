d <- read.csv("data/M04_module_registry.csv", na.strings="")
labs <- read.csv("data/M04_module_labs.csv")
stopifnot(!anyDuplicated(d$pid))
d$height_cm <- ifelse(d$pid==2, 100*d$height_raw, d$height_raw)
d$sbp <- replace(d$sbp_raw, d$sbp_raw==-99, NA)
d$bmi <- d$weight_kg/(d$height_cm/100)^2
summaries <- aggregate(ldl~pid,labs,mean)
out <- merge(d,summaries,by="pid",all.x=TRUE,sort=TRUE)
stopifnot(nrow(out)==3,out$height_cm[2]==168,is.na(out$sbp[3]),is.na(out$smoker[3]),
          abs(out$bmi[2]-26.0416666667)<1e-9,identical(out$ldl,c(120,140,NA_real_)))
print(out[c("pid","height_cm","sbp","smoker","bmi","ldl")])
