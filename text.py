from math import comb

n = 15
m = 3

numberOfWays = comb(n - 1, m - 1) - 1 if n % m == 0 else 0
print(numberOfWays)