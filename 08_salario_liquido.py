horas_normais = int(input())
horas_extras = int(input())

salario_base = 2500
valor_hora = 2500/200

salario_bruto = horas_normais*valor_hora + horas_extras*valor_hora*1.2
ir = salario_bruto*0.13
inss = salario_bruto*0.09
salario_liquido = salario_bruto - inss - ir

print(f"- Salário Bruto : R$ {salario_bruto:.2f}")
print(f"- IR (13%) : R$ {ir:.2f}")
print(f"- INSS (9%) : R$ {inss:.2f}")
print(f"- Salário Líquido : R$ {salario_liquido:.2f}")