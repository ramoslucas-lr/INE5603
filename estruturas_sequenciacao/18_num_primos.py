import math

n = int(input())

min_primos = n/math.log(n)
max_primos = 1.25506*min_primos

print(round(min_primos, 1), round(max_primos, 1))