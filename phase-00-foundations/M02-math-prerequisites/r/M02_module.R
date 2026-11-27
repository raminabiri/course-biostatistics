reference <- 24/200
comparison <- 8/100
x <- c(3, 5, 10)
table <- matrix(c(12, 288, 9, 291), nrow = 2, byrow = TRUE)
time <- 0:3
linear <- 80 - 20*time
exponential <- 80 * .5^time
answer <- c(absolute_points=100*(reference-comparison),
            relative_percent=100*(reference-comparison)/reference,
            incidence_per_100=8/160*100, mean=mean(x),
            sum_of_squares=sum(x^2), square_of_sum=sum(x)^2,
            second_row=sum(table[2,]), first_column=sum(table[,1]),
            final_linear=tail(linear,1), final_exponential=tail(exponential,1),
            log_ratio=log2(exponential[4]/exponential[1]))
stopifnot(max(abs(answer-c(4,100/3,5,6,134,324,300,21,20,10,-3)))<1e-10)
print(answer)
