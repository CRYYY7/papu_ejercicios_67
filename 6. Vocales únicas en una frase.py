frase = input("Ingresa una frase: ").lower()
vocales = "aeiouáéíóú"
encontradas = set()

for caracter in frase:
    if caracter in vocales:
        encontradas.add(caracter)

print("Vocales encontradas:", ", ".join(encontradas))