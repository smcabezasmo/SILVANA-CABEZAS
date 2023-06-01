#Ingresar texto
#Ingrese tres letras 
#1. Cuantas veces aparece la letra que ingresó
#2. Cuantas palabras hay en total
#3. Primer y última letra
#4. Texto inverso
#5. Aparece pyhton en el texto?

texto=input("Ingrese un texto de su preferencia: ")
texto=texto.split()
textoreverse=texto.reverse()
letras=list(input("Ingre tres letras de su preferencia: "))
lista=letras
cantidad_letras1=texto.count(lista[0])
print(f"Hemos encontrado la letra '{lista[0]}' repetida {cantidad_letras1} veces")
print(f"El texto ingresado contiene {len(texto)} palabras")
print(f"La primera palabra del texto ingresaso es la {texto[0][0]} y la última palabra es la {texto[-1][-1]}")
print(f"El texto ingresado invertido es: {texto.reverse}")
