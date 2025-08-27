dias_totais = int(input())

anos = int(dias_totais / 365)
dias_restantes = dias_totais % 365
meses = int(dias_restantes / 30)
dias = int(dias_restantes % 30)

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")