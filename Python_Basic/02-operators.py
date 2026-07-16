### Operadores Aritméticos ###

# Operadores con enteros
print(3+4)
print(3-4)
print(3*4)
print(3/4)
print(10%3) # modulo (resto)
print(10//3) # cociente
print(2**3)
print(2 ** 3 + 3 - 7 / 1 // 4)
print("--------------------------------------")

# Operadores con cadenas de texto
print("Yo" + "me pregunto " + "y me pongo a pensar")
print("Hola" + str(5))
print("--------------------------------------")

# Operaciones mixtas
print("Hola " * 5)
print("Hola " * (2**3))
print("--------------------------------------")

my_float = 2.5 * 2
print("Hola " * int(my_float))
print("--------------------------------------")

### Operadores Comparativos ###

# Operaciones con enteros
print(3 < 4)
print(3 > 4)
print(3 <= 4)
print(3 >= 4)
print(3 == 4)
print(3 != 4)
print("--------------------------------------")

# Operaciones con cadenas de texto
print("Hola" > "python")
print("Hola" < "python")
print("aaaa" >= "abaa") # Operación alfabética por ASCII
print(len("aaaa") >= len("abaa")) # Cuenta caractereres
print("Hola" <= "python")
print("Hola" == "python")
print("Hola" != "python")
print("--------------------------------------")

### Operadores lógicos ###

# Basada en el álgebra de Boole
print(3 > 4 and "Hola" > "python")
print(3 > 4 or "Hola" > "python")
print(not (3 > 4))