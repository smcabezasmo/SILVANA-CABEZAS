#ocupan menos espacios de memoria que una lista
#se ocupan cuando no se quiere que sean modificadas
#apruebas de errores

mi_tuple=(1,2,3), (2.4*7), {"nombre":"Silvana","edad":23}
print(type(mi_tuple))
print(mi_tuple)
print(mi_tuple[-2]) #se puede consultar index
print(mi_tuple[2]["nombre"])
mi_tuple=list(mi_tuple) #sobreescribir 
print(type(mi_tuple))
 #se puede hacer con listas, diccionarios y tuples
t=(1,2,3)
x,y,z = t
print(x,y,z)


f=(1,2,3,1)
print(len(f))
print(f.count(1)) #contar la cantidad de aparicione de un valor
print(f.index(2))
