import math

x1, y1 = [float(w) for w in input().split()]
x2, y2 = [float(w) for w in input().split()]

d = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2 - y1, 2))
print(round(d, 4))