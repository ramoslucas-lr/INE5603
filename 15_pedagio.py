L, D = [int(w) for w in input().split()]
K, P = [int(w) for w in input().split()]

custo_gasolina = K*L
num_pedagios = int(L/D)

custo_pedagio = num_pedagios*P

print(custo_gasolina + custo_pedagio)