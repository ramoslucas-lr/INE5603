area = int(input())

rendimento_galao = 18*3.6
preco_galao = 25

galoes_necessarios = max(1, round(area/rendimento_galao))
custo = preco_galao*galoes_necessarios

print("- área de cobertura:", area)
print("- número de galões:", galoes_necessarios)
print(f"- valor a ser pago: R$ {custo:.2f}")
