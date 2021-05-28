from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica , Color) :
    def __init__(self, lado , color):
        FiguraGeometrica.__init__(self, lado, lado) #Cuadrado, ancho y alto = lado
        Color.__init__(self, color)         #De esta forma inicializamos la herencia multiple
    
    def calcular_area(self):
        return self.alto * self.ancho
        
