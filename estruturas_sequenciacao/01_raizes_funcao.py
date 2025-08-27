import math

a = int(input())
b = int(input())
c = int(input())

delta = math.sqrt(math.pow(b, 2) - 4*a*c)
x1 = (-b + delta)/(2*a)
x2 = (-b - delta)/(2*a)

print(x1, x2)