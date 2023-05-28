x=4
y=2
z=7

print(f"{x} más {y} es igual a {x+y}")
print(f"{x} menos {y} es igual a {x-y}")
print(f"{x} por {y} es igual a {x*y}")
print(f"{x} dividido {y} es igual a {x/y}")

print(f"{z} dividido al piso de {y} es igual a {z//y}")
print(f"{z} modulo de {y} es igual a {z%y}")
print(f"{z} elevado a la {y} es igual a {z**y}")
print(f"{z} elevado a la  {3} es igual a {z**3}")
print(f"La raíz cuadrada de {x} es igual a {x**0.5}")


#Redondeo
print(round(95.33333333, 2)) #después de la coma se ponen la cantidad de decimales

valor=95.44812134
print(round(valor))
print(type(valor))

#al redondear directamente la variable se cambia el tipo de dato
valor=round(95.44812134)
print(valor)
print(type(valor))