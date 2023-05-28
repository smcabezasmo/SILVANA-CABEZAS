nombre = input("Hola, ingresa tu nombre: ")
ventas = (input(f"Hola {nombre}, por favor ingresa el monto de tus ventas: "))
comision = (int(ventas)*0.15)
print(f"{nombre}, tus ventas de este mes fueron de {ventas}, por lo que tienes una comisión de {comision}")
