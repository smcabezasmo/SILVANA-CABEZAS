texto="Este es el texto de Silvana, "
texxto="25"
otro="Silvana"
texto1="la mejor"
e=" ".join([texto, otro, texto1])
resultado=texto.upper() #todo mayúsculas
resultado1=texto[2].upper() #mayúscula sólo una letra
resultado2=texto.lower() #todo minúsculas
resultado3=texto.split() #devuelve una lista de palabras (separación)
resultado4=texto.split("e") #devuelve una lista de palabras cortando la cadena en ""
resultado5=texto.find("f") #imprime -1 cuando lo que se busca no está en la cadena
resultado6=texto.replace("Silvana", "la mejor")
resultado7=texxto.replace("25","2")


print(resultado)
print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)
print(e)
print(resultado5)
print(resultado7)