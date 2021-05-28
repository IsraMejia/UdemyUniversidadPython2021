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
        self.__apellido  =  apellido  #Atributo = parametro
        self.__edad =  edad 

    @property #decorador que deja en claro que es Metodo 'get' para mostrar el nombre, al llamar el metodo no se pone '()'
    def nombre(self): 
        return self.__nombre
    
    @nombre.setter#Decorador para definir el metodo 'setter'
    def nombre(self, nombre):
        self.__nombre = nombre #Se cambia el atributo encapsulado


    @property 
    def apellido(self):
        return self.__apellido #Tiene que ser el mismo atributo en el getter para que sirva el setter
    
    @apellido.setter
    def apellido(self, apellido):   
        self.__apellido = apellido

    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        self.__edad = edad #Los setters no retornan nada


    def mostrar_detalle(self):  
        print(f"El nombre de la persona es:\n {self.__nombre} {self.apellido} \n su edad es: {self.edad}")
        #Los metodos dentro de la clase Si permiten mostrar los atributos encapsulados (getter)
  

if __name__ == '__main__' : #Para asegurarnos de que de este Modulo solo se ejecute la definicion de la clase que necesitamos en otros Modulos/Archivos
    persona1 = Persona("Isra" , "Mejia", 23)

    #----------------------Encapsulamiento 
    # al poner "__" en las variables de instancia, se entiende que son privadas, y asi tenemos que usarlas
    persona1.__nombre = 'Hipolito' #NO se recomieda hacer esto
    print(f'\tEncapsulamiento\npensariamos que se modifico el nombre = {persona1.__nombre}') #Hace referencia a __nombre, pero NO a _Persona__nombre = 'Isra'
    print(f'Pero _Persona__nombre =  {persona1.nombre}') #no se necesita poner () al metodo ya que el property deja en claro que es un metodo get
    #Al poner el "__" el metodo mostrar detalle deja de servir, asi que se podria decir que si sirve, pero es por buenas practicas de codigo

    print('\nPara cambiarlo de verdad usamos el metodo setter')
    persona1.nombre = 'Israaaaa' #<- Setter
    print(f'_Persona__nombre =  {persona1.nombre}')
    print(f'De la otra forma que esta mal sale : {persona1.__nombre} \n   ya que tratamos entrar al atributo fuera de metodos getters o metodos internos de la clase (no se puede acceder a atributos encapsulados fuera de la clase)')
    print("\nConclusion, solo se puede encapsular con '__' , junto con los decoradores de @property para el getter y @nombre.setter  ")

    print('\n Los metodos dentro de la clase Si permiten mostrar los atributos encapsulados (getter) -> persona1.mostrar_detalle()')
    persona1.mostrar_detalle()

    print('\n\nAhora cambiamos con puros setters')
    persona1.nombre = 'Luis'
    persona1.apellido = 'MiRex'
    persona1.edad = 7
    persona1.mostrar_detalle()


    print(__name__)  #dunder name =  Nos dice el nombre del modulo 
        #Si nos sale __main__ se refiere que el modulo ejecutado es del propio archivo
        #Si este modulo es llamado de otro archivo saldra 'Persona', que es el modulo del que se ejecuta el codigo

