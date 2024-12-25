#Tuplas 
my_tupla = (53,'perro',7.4,True) #no se puede modificar como las listas
print(type(my_tupla))

print(my_tupla[1])
print(my_tupla.count(53))
print(my_tupla.index(True)) #indica posicion del elemento

my_tupla = list(my_tupla) #convierte la tupla a lista
print(type(my_tupla))
