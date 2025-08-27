l1 = float(input())
l2 = float(input())
l3 = float(input())

is_triangle = l1+l2 > l3 and l2+l3 > l1 and l3+l1 > l2

print(is_triangle)