#Excpeciones (para codigo que puede dar error)
#print(5+'3') # da error

try: #pregunta si el codigo funciona    
    print(5+'3')
except TypeError as error:
    print('error de variable')
    print(error)
except NameError:
    print('error de nombre')
else: #solo funciona cuando try funciona
    print('Hola mundo')    
finally: #funciona si o si
    print('Suscribete')    
    