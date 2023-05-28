animal=" chanCHito feliz   "
print(animal.upper()) #pasar letras a mayúsculas
print(animal.lower()) #pasar letras a minúsculas
print(animal.capitalize()) #primera letra a mayúscula y lo demás en minúscula
print(animal.title()) #primera letra de cada palabra a mayúscula y lo demás a minúscula.
print(animal.strip()) #remover los espacios en blanco
print(animal.strip().capitalize()) #remover espacios primero para luego aplicar capitalize
print(animal.lstrip()) #remover los espacios en blanco a la izquierda
print(animal.rstrip()) #remover los espacios en blanco a la derecha
print(animal.find("CH")) #buscar una cadena de caracteres dentro del string arroja el índice de ubicación de la cadena
print(animal.find("re")) #buscar una cadena de caracteres que no está dentro del string arroja -1 cuando no encuentra nada
print(animal.replace("nCH", "j")) #reemplazar parte de la cadena de caracteres
print("nCH" in animal) #devuelve un booleano para saber si una cadena de caracteres está dentro de una variable
print("nCH" not in animal) #devuelve un booleano para saber si una cadena de caracteres NO cleestá dentro de una variable