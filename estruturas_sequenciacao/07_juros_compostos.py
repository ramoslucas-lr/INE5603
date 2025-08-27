import math

capital_inicial = float(input())
meses = int(input())
taxa = float(input())/100

montante = capital_inicial*math.pow(1+taxa, meses)

print(round(montante, 2))