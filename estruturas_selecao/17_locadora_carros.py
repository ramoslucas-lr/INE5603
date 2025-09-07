diarias = int(input())
km_rodados = int(input())

km_cortesia = 60*diarias

custo = diarias*45

if km_rodados > km_cortesia:
    custo_km = 0.5*(km_rodados - km_cortesia)
    custo = custo + custo_km

print(f'{custo:.2f}')