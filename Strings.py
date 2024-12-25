#Strings

mi_first_string = "mi string con doble comillas"
mi_second_string = 'mi string con simple comilla'
print(mi_first_string,mi_second_string)
print('esto es un texto de una variable '+ mi_first_string + ' '+ mi_second_string) # pesado
print(f'esto es un texto de una variable {mi_second_string} dasdas')

other_string='hola'
a,b,c,d = other_string #asigna letra por letra
print(c)
print(a)
print(b)
print(d)

print(mi_first_string.upper()) #pasa todo a mayusculas
print(mi_first_string.capitalize()) #Primera letra en mayuscula
print(mi_first_string.lower()) #pasa todo a minusculas
print(len(mi_first_string)) #cuenta los caracteres
print(mi_first_string.find('r')) #Cuenta la posicion de la primera ves que sale el caracter
print(mi_first_string.count('l')) #Cuenta las veces de tipeo
print(mi_first_string.lower().isupper()) #unir funciones