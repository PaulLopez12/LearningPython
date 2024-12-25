#Sets
my_set = {}
print(type(my_set))

my_set = {'Python', 'Javascript', 'C++'}
print(type(my_set))

print(my_set) #Imprime sin importar el orden
#print(my_set[0]) nos bota error

my_set.add('C#') #no repite elementos
print(my_set)

my_set_0 = {'Python', 'Javascript', 'C++'}

my_set.difference_update(my_set_0)
print(my_set)