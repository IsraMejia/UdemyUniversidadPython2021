class Cubo:
    def __init__(self, ancho, profundo, alto):
        self.ancho = ancho
        self.profundo = profundo
        self.alto = alto
    
    def calcula_volumen(self):
        return self.ancho * self.profundo * self.alto

print("\n\tEste programa calcula el volumen de un Cubo usando POO")
ancho = int(input('Ingrese la ancho del cubo: '))
profundo = int(input('Ingrese la profundo del cubo: '))
alto = int(input('Ingrese la alto del cubo: '))

cubo1 = Cubo(ancho, profundo, alto)
print(f"El volumen del cubo es {cubo1.calcula_volumen()}  unidades cubicas")