comp_mesa = float(input())
larg_mesa = float(input())
gavetas = int(input())
madeira = input()

min_preco = 200
custo_m2 = 100
preco_gaveta = 30
acresc_mesa_grande = 50
acresc_madeira = {
    'mogno': 150,
    'carvalho': 125
}

area_mesa = comp_mesa*larg_mesa
preco_mesa = area_mesa*custo_m2
if area_mesa > 2:
    preco_mesa += acresc_mesa_grande
if madeira in acresc_madeira:
    preco_mesa += acresc_madeira[madeira]

preco_mesa += gavetas*preco_gaveta
preco_mesa = max(preco_mesa, min_preco)

print(f'{preco_mesa:.2f}')

