from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica , Color):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)
    
    def calcular_area(self):
        return self.alto * self.ancho
    
    def __str__(self):
        return f"class Rectangulo \n Hereda de {FiguraGeometrica.__str__(self)} y de {Color.__str__(self)}"