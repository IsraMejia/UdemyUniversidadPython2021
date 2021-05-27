# class Persona:
#     def __init__(self, nombre, apellido, edad, *tupla, **diccionario): 
#         #   *args = argumentos variables de tipo tupla
#         #   **kwargs = argumentos variables de tipo diccionario
#     #El parametro 'self' al metodo inicializador de la clase hace referencia al objeto mismo que se va a crear
#         #El doble guion bajo 'dunder' le da el nombre de metodo "dunder init"
#         self.__nombre =  nombre #self.Atributo de instancia, del objeto que estamos creando por defecto
#         self.apellido  =  apellido  #Atributo = parametro
#         self.edad =  edad
#         self.tupla = tupla
#         self.diccionario = diccionario
    
#     def mostrar_detalle(self): #Se necesita el parametro "self" para funcionar como metodo de instancia
#         print(f"El nombre de la persona es:\n {self.__nombre} {self.apellido} \n  su edad es: {self.edad} \n Su tupla es {self.tupla} \n y su diccionario es {self.diccionario}")
#             #Con la palabra self nos referimos al objeto en cuestion como cuando usamos widget en flutter :D


#     #pass #permite generar la clase sin  que se le defina atributos o metodos


# print("\n\tLeccion 01 POO\n")
# print(type(Persona))

# persona1 = Persona("Isra" , "Mejia", 23,   3178,45,321,32, m='manzana', a = 'apple' ) #Los parentesis manda a llamar el metodo inicializador o constructor de la clase __init__

# # print(f"El nombre de la persona1 es: {persona1.nombre} {persona1.apellido} \ny su edad es: {persona1.edad} \n")

# # persona1.nombre = "Hipolito"
# # persona1.edad = 60
# # print(f"El nombre de la persona1 es: {persona1.nombre} {persona1.apellido} \ny su edad es: {persona1.edad} \n")
# persona1.mostrar_detalle()
# persona1.carrera = "Ingenieria en Computacion"
# print(f"Y su carrera es {persona1.carrera}\n\n") #Se le pueden crear atributos dentro de la marcha, pero esto no se aplica a todas las clases, solo al objeto en cuestion

# persona2 = Persona("Rex", "PerroBeibe", 7)
# # print(f"El nombre de la persona 2 es: {persona2.nombre} {persona2.apellido} \ny su edad es: {persona2.edad} \n")
# Persona.mostrar_detalle(persona2) #Podemos usar el nombre de la clase y pasamos como parametro el objeto para que jale 
# # print(f"Y es {persona2.carrera}") #No tiene definido el atributo carrera, se puede definir durante la marcha al objeto, pero no se hizo


# #----------------------Encapsulamiento 
# # al poner "__" en las variables de instancia, se entiende que son privadas, y asi tenemos que usarlas
# persona1.__nombre = 'Hipolitooo' #NO se recomieda hacer esto
# print(f'Nombre = {persona1.__nombre}') 
# #Al poner el "__" el metodo mostrar detalle deja de servir, asi que se podria decir que si sirve, pero es por buenas practicas de codigo
# persona1.mostrar_detalle()

class Persona:
    def __init__(self, nombre, apellido, edad):   
        #El doble guion bajo 'dunder' le da el nombre de metodo "dunder init"
        self.__nombre =  nombre #self.Atributo de instancia, del objeto que estamos creando por defecto
        self.apellido  =  apellido  #Atributo = parametro
        self.edad =  edad 

    @property #decorador que deja en claro que es Metodo 'get' para mostrar el nombre, al llamar el metodo no se pone '()'
    def nombre(self): 
        return self.__nombre

    @nombre.setter#Decorador para definir el metodo 'setter'
    def nombre(self, nombre):
        self.__nombre = nombre

    def mostrar_detalle(self):  
        print(f"El nombre de la persona es:\n {self.__nombre} {self.apellido} \n su edad es: {self.edad}")
  
persona1 = Persona("Isra" , "Mejia", 23)

#----------------------Encapsulamiento 
# al poner "__" en las variables de instancia, se entiende que son privadas, y asi tenemos que usarlas
persona1.__nombre = 'Hipolito' #NO se recomieda hacer esto
print(f'\npensariamos que se modifico el nombre = {persona1.__nombre}') #Hace referencia a __nombre, pero NO a _Persona__nombre = 'Isra'
print(f'Pero _Persona__nombre =  {persona1.nombre}') #no se necesita poner () al metodo ya que el property deja en claro que es un metodo get
#Al poner el "__" el metodo mostrar detalle deja de servir, asi que se podria decir que si sirve, pero es por buenas practicas de codigo

print('\nPara cambiarlo de verdad usamos el metodo setter')
persona1.nombre = 'Israaaaa'
print(f'_Persona__nombre =  {persona1.nombre}')
print(f'De la otra forma que esta mal sale : {persona1.__nombre} \n')
print("Conclusion, solo se puede encapsular con '__' , junto con los decoradores de @property para el getter y @nombre.setter \n ")


