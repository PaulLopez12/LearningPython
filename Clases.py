#Clases
class UnHumano:
    def __init__(self,altura,edad,peso):
        self.altura = altura #se usa self para guardar informacion
        self.edad = edad
        self.peso = peso
    #crear una accion    
    def comer (self):
        print(f' el humano de {self.edad} años esta comiendo')
            
humano1= UnHumano(1.8,23,87) #solo guarda informacion, no se muestra en print
print(f'El humano 1 mide {humano1.altura}m, pesa {humano1.peso}kg y tiene {humano1.edad} años')

humano1.comer()