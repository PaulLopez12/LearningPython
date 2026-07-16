# Variables
my_string_variable = 'My string variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Concatenacion de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea, !Cuidado con el abuso kaumza¡
name, surname, alias, age = 'Paul', 'Anderson', 'ZWarkingZ', 28
print("Me llamo", name, surname, ", en los juegon me dicen:", alias, "y tengo", age, "años") 

# Inputs
name = input('¿Cuál es tu nombre?')
age = input('¿Cuál es tu edad?')
print(name)
print(age)

# Cambiamos su tipo
name = 28
age = 'Paul'
print(name)
print(age)

# Forzando el tipo
address : str = "Mi dirección"
adrress : True
address : 5
address : 1.2
print(type(address))