### Error Types ###

# SyntaxError
#print "Hola Comunidad!"
from math import pi
import math

print("Hola Comunidad!")
print("----------------------------------")

# NameError
language = "Spanish"   # comentar para error
print(language)
print("----------------------------------")

# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[5]) #Descomentar para error
print("----------------------------------")

# ModuleNotFoundError
#import maths #Descomentar para error

# AttributeError
#print(math.PI) # Descomentar para Error
print(math.pi)
print("----------------------------------")

# KeyError
my_dict = {"Nombre": "Paul", "Apellido": "Lopez", "Edad": 28, 1: "Python"}
print(my_dict["Edad"])
# print(my_dict["Apelido"]) # Descomentar para Error
print(my_dict["Apellido"])
print("----------------------------------")

# TypeError
# print(my_list["0"]) # Descomentar para Error
print(my_list[0])
print(my_list[False])  
print("----------------------------------") 

# ImportError
# from math import PI # Descomentar para Error
print(pi)
print("----------------------------------")

# ValueError
# my_int = int("10 Años") # Descomentar para Error
my_int = int("10")
print(type(my_int))
print("----------------------------------")

# ZeroDivisionError
# print(4/0) # Descomentar para Error
print(4/2)
