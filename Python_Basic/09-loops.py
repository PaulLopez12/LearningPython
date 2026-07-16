### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # es opcional
    print("Mi condición es mayor o igual a 10")
    
print("La ejecución continua")

while my_condition < 20:
    my_condition +=1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("La ejecución continúa")

# for
my_list = [35, 24, 62, 52, 30, 30, 17]
for element in my_list:
    print(element)
print("La ejecución continúa")
    
my_tuple = (28, 1.7, "Paul", "Lopez", "Paul")
for element in my_tuple:
    print(element)
print("La ejecución continúa")

my_set = {"Paul", "Lopez", 28}
for element in my_set:
    print(element)
print("La ejecución continúa")

my_dict = {"Nombre": "Paul", "Apellido": "Lopez", "Edad": 28, 1: "Python"}
for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para el dict ha finalizado")
print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejectuta")
else:
    print("El bucle for para el dict ha finalizado")