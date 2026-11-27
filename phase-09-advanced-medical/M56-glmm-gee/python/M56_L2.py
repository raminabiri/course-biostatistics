rho = .4
independent = [[int(i==j) for j in range(3)] for i in range(3)]
exchangeable = [[1 if i==j else rho for j in range(3)] for i in range(3)]
ar1 = [[rho**abs(i-j) for j in range(3)] for i in range(3)]
for matrix in (independent, exchangeable, ar1):
    print(matrix)
assert abs(ar1[0][2]-.16)<1e-12
