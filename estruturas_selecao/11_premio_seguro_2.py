valor_carro = float(input())
genero = input()
idade_segur = int(input())

valor_base = 0.1*valor_carro

if genero == 'M':
    if idade_segur <=24:
        desc = 0.0
    elif 25 <= idade_segur <= 33:
        desc = 0.1
    else:
        desc = 0.2
else:
    if idade_segur <=24:
        desc = 0.05
    elif 25 <= idade_segur <= 33:
        desc = 0.2
    else:
        desc = 0.35

premio = valor_base*(1-desc)
print(f'{premio:.2f}')