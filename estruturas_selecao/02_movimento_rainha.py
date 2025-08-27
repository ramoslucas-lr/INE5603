x1, y1 = [int(w) for w in input().split()]
x2, y2 = [int(w) for w in input().split()]

if x2 == x1 and y2 == y1:
    print(False)
elif (x2 == x1 or y2 == y1):
    print(True)
else:
    desloc_x = abs(x2 - x1)
    desloc_y = abs(y2 - y1)

    print(desloc_x == desloc_y)
