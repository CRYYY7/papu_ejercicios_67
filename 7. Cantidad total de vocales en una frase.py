frase = input("Ingresa una frase: ").lower()
vocales = "aeiouáéíóú"
contador = 0

for caracter in frase:
    if caracter in vocales:
        contador += 1

print(f"La frase contiene {contador} vocales.")