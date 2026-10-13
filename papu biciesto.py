n = int(input("Ingresa un año: "))
if n % 4 == 0 and (n % 100 != 0 or n % 400 == 0):
    print(f"{n} es un año bisiesto.") # Si es bisiesto
else:
    print(f"{n} no es un año bisiesto.") #No es bisiesto

    print(n%4)
    print(n%100)
    print(n%400)
