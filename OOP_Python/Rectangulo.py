class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcula_area(self):
        return self.base * self.altura

print("\n\tEste programa calcula el area de un rectangulo usando POO")
base = int(input('Ingrese la base del rectangulo: '))
altura = int(input('Ingrese la altura del rectangulo: '))

rectangulo1 = Rectangulo(base, altura)
print(f"\n\tEl area del rectangulo es: {rectangulo1.calcula_area()}")

base = int(input('\n\nIngrese la base del rectangulo2: '))
altura = int(input('Ingrese la altura del rectangulo2: '))

rectangulo2 = Rectangulo(base, altura)
print(f"\n\tEl area del rectangulo2 es: {rectangulo2.calcula_area()}")

