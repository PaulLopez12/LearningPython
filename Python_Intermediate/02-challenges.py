### Challenges ###


"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i) 
            
fizzbuzz()

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(texto1 = "", texto2 = ""):
    if(texto1.lower() == texto2.lower()):
        return False
    return sorted(texto1.lower()) == sorted(texto2.lower())
 

print(is_anagram("Amor", "Rama"))

"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    first_value = 0
    second_value = 1
    
    for i in range(0,51):
        print(first_value)
        next = second_value + first_value
        first_value = second_value
        second_value = next
        
fibonacci()

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def is_primo(number, n=2):
    if n >= number:
        print("Es primo")
        return True
    elif number % n != 0:
        return is_primo(number, n + 1)
    else:
        print(f"No es primo,", {n}, "es divisor")
        return False

for i in range (1,101):
    print(is_primo(i), i)
    
"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def inverted(texto = ""):
    text_len = len(texto)
    reversed_text = ""
    for i in range(0,text_len):
        reversed_text += texto[text_len - 1 - i]
    return reversed_text

print(inverted("ZWarkingZ"))