#Modulos: importa funciones de otros ficheros

#import Funciones #importa todo el fichero
#Funciones.Sum_number(5,3)

from Funciones import Sum_number, Sum_three_num as three
Sum_number(5,3)

three(5,3,8)