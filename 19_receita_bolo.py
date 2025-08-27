a, b, c = [int(w) for w in input().split()]

fator_farinha = int(a/2)
fator_ovos = int(b/3)
fator_leite = int(c/5)

print(min(fator_farinha, fator_ovos, fator_leite))