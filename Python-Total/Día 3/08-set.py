mi_set=set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set={1,2,3}
print(type(otro_set))
print(otro_set)

print(2 in mi_set)


s1={1,2,3}
s2={3,4,5}
s3=s1.union(s2) #unir sets
print(s3)


s1.add(4) #añadir elemento al set
print(s1)

s1.remove(3)
print(s1)

s1.discard(6) #descartar un valor, no arroja error
print(s1)


sorteo=s1.pop() #eliminar un número aleatorio
print(sorteo)

s1.clear() #vaciar el set
print(s1)