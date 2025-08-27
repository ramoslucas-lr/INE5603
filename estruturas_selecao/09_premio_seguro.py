valor_carro = float(input())
classe_desconto = input()
procedencia = input()
idade_segur = int(input())

classes_desconto = {
    'A': 0.3,
    'B': 0.2,
    'C': 0.1,
    'D': 0.05,
    'E': 0
}

base_procedencia = {
    'nacional': 0.1,
    'estrangeira': 0.15 
}

valor_base = valor_carro*base_procedencia[procedencia] 
valor_premio = valor_base*(1-classes_desconto[classe_desconto])

if idade_segur > 24:
    valor_premio = valor_premio - valor_base*0.1

print(f'{valor_premio:.2f}')