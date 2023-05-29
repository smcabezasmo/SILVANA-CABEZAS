texto = "ABCDEFGHIIJKLM"
# imprime los caracteres desde el 2 al 10, el 11 no lo toma
fragmento = texto[2:11]
print(fragmento)

texto = "ABCDEFGHIIJKLM"
# imprime el fragmento saltando de a 2 espacios hasta el 10, el 11 no lo toma
fragmentos = texto[2:11:3]
print(fragmentos)
# Si quiero ver desde el 9 caracter, tengo que especificar que desde el 8, porque el caracter 8 no lo tiene en cuenta, sino el que sigue
