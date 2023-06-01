diccionario={"d1":"valor1","c2":"valor2", "c3":"valor3"}
print(type(diccionario))
resultado=diccionario["d1"]
print(resultado)

cliente={"nombre":"Silvana","apellido":"Cabezas", "edad":23, "talla":168.7}
print(cliente["edad"])
consulta=(cliente["talla"])
print(consulta)


dic={'c1':55, 'c2':[10,20,30], 'c3':{'s1':100,'s2':220}}
print(dic['c2'][1]) #imprime únicamente la posición 1 de la lista que pertenece al valor c2 del diccionario
print(dic["c3"]["s1"]) #imprime únicamente el valor asigando a c3 en la posición s1

dicc={'c1':['a','b','c'], 'c2':['d','e','f']}
print(dicc["c2"][1].upper())

dicc[3]="c" #agregar elementos al diccionario
print(dicc)


print(dicc.keys())#para conocer la claves que hay en el diccionario
print(dicc.values())#para conocer los valores de las claves
print(dicc.items())