### Sets ###

# Definición

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Paul", "Lopez", 28}
print(type(my_other_set))

print(len(my_other_set))
print("--------------------------")

# Inserción
my_other_set.add("ZWarkingZ")
print(my_other_set) # no es una estructura ordenada

my_other_set.add("ZWarkingZ") # no admite repetidos
print(my_other_set)
print("--------------------------")

# Búsqueda
print("Paul" in my_other_set)
print("Añañin" in my_other_set)
print("--------------------------")

# Eliminación
my_other_set.remove("Paul")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined
print("--------------------------")

# Transformación
my_set = {"Paul", "Lopez", 28}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}
print("--------------------------")

# Otras operaciones
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Js", "C#"}))
print(my_new_set.difference(my_set))