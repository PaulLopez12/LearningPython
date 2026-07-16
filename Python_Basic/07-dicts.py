### Dictionaries ###

# Definición
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre" : "Paul", "Apellido" : "Lopez" , "Edad" : 28, 1 : "Python"}

my_dict = {
    "Nombre": "Paul",
    "Apellido": "Lopez",
    "Edad": 28,
    "Lenguajes": {"Python", "C++", "Javascript"},
    1: 1.70
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))
print("--------------------------------")

# Búsqueda
print(my_dict[1]) # muestra la clave de la llave
print(my_dict["Nombre"])

print("Lopez" in my_dict) # solo busca la llave
print("Apellido" in my_dict)
print("--------------------------------")

# Inserción
my_dict["Calle"] = "Cusco"
print(my_dict)
print("--------------------------------")

# Actualización
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])
print("--------------------------------")

# Eliminación
del my_dict["Calle"]
print(my_dict)
print("--------------------------------")

# Otras operaciones
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "ZWarkingZ")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))