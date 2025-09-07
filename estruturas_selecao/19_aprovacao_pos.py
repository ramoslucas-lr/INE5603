c1 = input()
c2 = input()
c3 = input()
c4 = input()

conceito_numerico = {
    'A': 4,
    'B': 3,
    'C': 2,
    'E': 0
}

if 'E' in [c1, c2, c3, c4]:
    print(False)
else:
    media = (conceito_numerico[c1] + conceito_numerico[c2] + conceito_numerico[c3] + conceito_numerico[c4])/4

    print(media>=3)