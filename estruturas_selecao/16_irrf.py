salario = float(input())
dependentes = int(input())

desc_dependente = 137.99

if salario <= 720:
    inss = 0.0765*salario
elif salario <= 1200:
    inss = 0.09*salario
elif salario <= 2400:
    inss = 0.11*salario
else:
    inss = 0.11*2400

if salario <= 1372.81:
    aliquota = 0.0
    deducao = 0.0
elif 1372.82 <= salario <= 2743.25:
    aliquota = 0.15
    deducao = 205.92
else:
    aliquota = 0.275
    deducao = 548.82

irrf = (salario - dependentes*desc_dependente - inss) * aliquota - deducao
irrf = max(irrf, 0)

print(f'{irrf:.2f}')
