x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

desloc_x = abs(x2 - x1)
desloc_y = abs(y2 - y1)

print((desloc_x == 1 and desloc_y == 2) or (desloc_x == 2 and desloc_y == 1))