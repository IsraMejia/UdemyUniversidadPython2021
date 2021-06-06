from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
print('Creacion de Objeto Cuadrado'.center(70, '-'))
cuadrado1 = Cuadrado(lado=9, color='azul')
print(f"\nEl alto es: {cuadrado1.alto} , su ancho es: {cuadrado1.ancho}, su color es {cuadrado1.color}")
print(f"Y su area es: { cuadrado1.calcular_area() }")

#MRO = Method Resolution Order <- El orden de resolucion de los metodos, como en el caso de herencia multiple
# print(Cuadrado.mro()) # Sigue el orden en el que se definio la herencia, primero la clase hija, luego la primer clase de herencia , luego la segunda y asi
print(f"\n{cuadrado1}\n")

print("\n\t Rectangulo")
rectangulo1 = Rectangulo(ancho= -1 , alto= -3, color= 'Purpura')
#rectangulo1.ancho = 4
print("\n\t Se instancio el Rectangulo")
print(f"\n{rectangulo1}\n")
print(f"Área del rectangulo:  { rectangulo1.calcular_area() }")
