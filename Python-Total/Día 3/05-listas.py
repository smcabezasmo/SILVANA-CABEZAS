mi_lista=["a","b","c"]
print(type(mi_lista))
print(mi_lista[0])
otra_lista=["hola","0.1","5","hello"]
otra_lista.append("Silvana") #Añadir un elemento a la lista
lista=mi_lista+otra_lista
print(type(otra_lista))
print(len(otra_lista))
print(otra_lista[2:5])
print(mi_lista+otra_lista) #concatenar listas
lista[0]="Alfa" #reemplazar elemento 0 por alfa
eliminado=otra_lista.pop(0) #eliminar indice 0 en lista otra_lista
print(otra_lista)
print(eliminado) #imprime indice eliminado

#ordenar lista
l1=[6,2,4,7,9,8,5]
l1.sort()
print(l1)
l2=["a","e","g","x","t","b","c","l"]
l2.reverse()
print(l2)