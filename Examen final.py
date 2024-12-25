#1 Segundo numero más grande
#lista =[5,7,2,7,9,4,8]
#lista.sort()
#print(lista[-2])

#2 Conversor de tiempo
#def miliseg (d=0,h=0,m=0,s=0):
#    time=0
#    mils=0
#    time= (d*24*60*60) + (h*60*60) + (m*60) + s
#    mils = time/1000
#    print(mils)
    
#miliseg(2,15,45,20) 

#3FizzBuzz: funcion que muestre numeros del 1 al 100 
#           si es multiplo de 3, imprime Fizz
#           si es multiplo de 5, imprime Buzz
#           so es multiplo de 3 y 5, imprime FizzBuzz

for n in range(1,101):
    if n%3==0 and n%5==0:
        print('FizzBuzz')
    elif n%3==0:
        print('Fizz')
    elif n%5==0:
        print('Buzz')
    else:
        print(n)    