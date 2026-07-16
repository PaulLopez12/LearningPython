### Tuples ###

# Definición
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (28, 1.70, "Paul", "Lopez", "Paul")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))
print("-----------------------------------")

# Acceso a elemntos y búsqueda
print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[-6]) IndexError
print(my_tuple.count("Paul"))
print(my_tuple.index("Lopez"))
print(my_tuple.index("Paul"))
print("-----------------------------------")

#my_tuple[1] = 1.8 'tuple' object does not support item assignment

# Concatenación
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print("-----------------------------------")

# Subtuplas
print(my_sum_tuple[3:6])
print("-----------------------------------")

# Tupla mutable con conversion a lista
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = 'ZWarkingZ'
my_tuple.insert(1,'Azul')
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Eliminación

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined