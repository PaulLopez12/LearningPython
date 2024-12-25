#Diccionarios

my_dict = {'a','b'}
print(type(my_dict))

my_dict = {'Nombre':'Paul',  #No necesariamente se guarda solo con '',
           'Apellido':'Lopez', #se puede usar otras variables
           'Apodo':'Imbecil'}
print(type(my_dict))
print(my_dict['Nombre'])

print(my_dict.keys()) #Imprime las variables a conceptuar
print(my_dict.values()) #Imprime los significados de las keys

#Al pasar a lista, tupla o sets, solo guarda las llaves