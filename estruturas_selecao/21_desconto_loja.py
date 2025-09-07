preco_item = float(input())

preco_final = preco_item - 0.2*preco_item

if preco_item >= 500:
    preco_final = preco_final - 0.1*preco_item

if preco_item > 1000:
    preco_final = preco_final - (preco_item - 1000)*0.15

print(preco_final)