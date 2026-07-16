### Functions ###

# Definición
def my_function():
    print("Esto es una función")
    
my_function()
print("----------------------------------")

# Función con parámetros de entrada/argumentos
def sum_two_values(first_value: int, second_value):
    print(first_value + second_value)

sum_two_values(3,7)
sum_two_values("3","7")
sum_two_values(3.2, 4.5)
print("----------------------------------")

# Función con parámetros de entrada/argumentos y retorno

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(4,2)
print(my_result)
print("----------------------------------")

# Función con parámetros de entrada/argumentos por clave
def print_name(name, surname):
    print(f"{name} {surname}")
    
print_name(surname="Lopez", name="Paul")
print("----------------------------------")

# Función con parámetros de entrada/argumentos por defecto
def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Paul", "Lopez")
print_name_with_default("Paul", "Lopez", "ZWarkingZ")
print("----------------------------------")

# Función con parámetros de entrada/argumentos arbitrarios
def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "ZWarkingZ")
print_upper_texts("Hola")

