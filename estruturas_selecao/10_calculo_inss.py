salario = float(input())

if salario <= 720:
    inss = 0.0765*salario
elif salario <= 1200:
    inss = 0.09*salario
elif salario <= 2400:
    inss = 0.11*salario
else:
    inss = 0.11*2400

print(f"{inss:.2f}")