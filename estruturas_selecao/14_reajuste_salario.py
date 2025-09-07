salario_func = float(input())
salario_min = float(input())

salarios = salario_func/salario_min

if salarios <= 3:
    aumento = salario_func*0.2
elif 3 < salarios <= 5:
    aumento = salario_func*0.15
else:
    aumento = salario_func*0.1

piso = salario_min*1.5
teto = salario_min*20

salario_ajustado = salario_func + aumento
salario_ajustado = max(salario_ajustado, piso)
salario_ajustado = min(salario_ajustado, teto)

print(f"{salario_ajustado:.2f}")
