### Regular Expressions ### 
import re

# match
my_string = "Esta es la lección número 7: Lección llamada expresiones regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la lección", my_other_string)
#if not (match == None): #Otra forma de comprobar el None
#if match != None: #Otra forma de comprobar el None
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])
    
print(re.match("Expresiones regulares", my_string)) 
print("-----------------------------")  

# search
search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])
print("-----------------------------")  

# findall
findall = re.findall("lección", my_string, re.I)
print(findall)
print("-----------------------------") 

# split
print(re.split(":", my_string))
print("-----------------------------") 

# sub
print(re.sub("[1|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones regulares", "RegEx", my_string))
print("-----------------------------") 

### Regular Expressions Patterns ###

# Para aprender y validar expresiones regulares: https://regex101.com

pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "XxwarriorlagxX@hotmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "XxwarriorlagxX@hotmail.com"
print(re.findall(pattern, email))