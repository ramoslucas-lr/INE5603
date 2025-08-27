a, b, c = [int(w) for w in input().split()]
x, y, z = [int(w) for w in input().split()]

max_horiz = int(x/a)
max_vert = int(y/b)
max_alt = int(z/c)

print(max_vert*max_horiz*max_alt)