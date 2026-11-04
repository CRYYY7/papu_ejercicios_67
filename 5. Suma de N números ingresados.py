cantidad = int(input("¿Cuántos números deseas ingresar?: "))
suma = 0

for _ in range(cantidad):
    numero = float(input("Ingresa un número: "))
    suma += numero

print(f"La suma total es: {suma}")