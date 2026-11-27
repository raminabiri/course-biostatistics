ra <- 15/100
rb <- 25/100
diff <- 105-100
v <- c(diff,diff/10,ra,rb,rb-ra,ra/rb,1/(rb-ra),(5/2.5)^2)
stopifnot(max(abs(v-c(5,0.5,0.15,0.25,0.1,0.6,10,4)))<1e-6)
print(v)
