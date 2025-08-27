origem = input()
temp_orig = float(input())
destino = input()

def celsius_to_kelvin(temp):
    return temp + 273.15

def kelvin_to_celsius(temp):
    return temp - 273.15

def fahrenheit_to_kelvin(temp):
    return (temp-32)*5/9 + 273.15

def kelvin_to_fahrenheit(temp):
    return ((temp - 273.15)*9/5 + 32)

def rankine_to_kelvin(temp):
    return temp*5/9

def kelvin_to_rankine(temp):
    return temp*9/5

if origem == destino:
    temp_destino = temp_orig
else:
    if origem == 'c':
        temp_kelvin = celsius_to_kelvin(temp_orig)
    elif origem == 'f':
        temp_kelvin = fahrenheit_to_kelvin(temp_orig)
    elif origem == 'r':
        temp_kelvin = rankine_to_kelvin(temp_orig)
    else:
        temp_kelvin = temp_orig

    if destino == 'c':
        temp_destino = kelvin_to_celsius(temp_kelvin)
    elif destino == 'f':
        temp_destino = kelvin_to_fahrenheit(temp_kelvin)
    elif destino == 'r':
        temp_destino = kelvin_to_rankine(temp_kelvin)
    else:
        temp_destino = temp_kelvin

print(f"{temp_destino:.6f}")