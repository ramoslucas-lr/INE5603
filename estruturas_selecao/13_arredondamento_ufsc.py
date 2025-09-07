import math

nota_original = float(input())

nota = nota_original*2
decimais = nota-int(nota)

if decimais == 0.5:
    nota = math.ceil(nota)
else:
    nota = round(nota)

nota = nota/2

print(f'{nota:.1f}')
