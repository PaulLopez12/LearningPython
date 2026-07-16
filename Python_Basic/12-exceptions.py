### Exception Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

# Excepción base: try except
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se proceduce una excepción
    print("Se ha producido un error")
    
print("-----------------------------")
# Flujo completo de una excepción: try except else finally
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: # opcional
    # Se ejecuta si se produce una excepción
    print("La ejecución continúa correctamente")
finally: # opcional
    # Se ejectuta siempre
    print("La ejecución continúa")
    
print("-----------------------------")

# Excepciones por tipo
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)
    