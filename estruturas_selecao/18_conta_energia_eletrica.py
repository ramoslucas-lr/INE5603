consumo = int(input())

tarifa_1 = 0.09556
tarifa_2 = 0.16698
tarifa_3 = 0.25052
tarifa_4 = 0.27836

if consumo <= 30:
    custo_energia = consumo*tarifa_1
elif 31 <= consumo <= 100:
    custo_energia = 30*tarifa_1 + (consumo-30)*tarifa_2
elif 101 <= consumo <= 200:
    custo_energia = 30*tarifa_1 + 70*tarifa_2 + (consumo -100)*tarifa_3
elif consumo > 200:
    custo_energia = 30*tarifa_1 + 70*tarifa_2 + 100*tarifa_3 + (consumo-200)*tarifa_4

print(f'{custo_energia:.2f}')
