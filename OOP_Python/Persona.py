class Persona:
    def __init__(self, nombre, apellido, edad): 
    #El parametro 'self' al metodo inicializador de la clase hace referencia al objeto mismo que se va a crear
        #El doble guion bajo 'dunder' le da el nombre de metodo "dunder init"
        self.nombre =  nombre #self.Atributo de instancia, del objeto que estamos creando por defecto
        self.apellido  =  apellido  #Atributo = parametro
        self.edad =  edad
    
    def mostrar_detalle(self): #Se necesita el parametro "self" para funcionar como metodo de instancia
        print(f"El nombre de la persona es:\n {self.nombre} {self.apellido} \n y su edad es: {self.edad} \n")
            #Con la palabra self nos referimos al objeto en cuestion como cuando usamos widget en flutter :D


    #pass #permite generar la clase sin  que se le defina atributos o metodos


print("\n\tLeccion 01 POO\n")
print(type(Persona))

persona1 = Persona("Isra" , "Mejia" , 23) #Los parentesis manda a llamar el metodo inicializador o constructor de la clase __init__

# print(f"El nombre de la persona1 es: {persona1.nombre} {persona1.apellido} \ny su edad es: {persona1.edad} \n")

# persona1.nombre = "Hipolito"
# persona1.edad = 60
# print(f"El nombre de la persona1 es: {persona1.nombre} {persona1.apellido} \ny su edad es: {persona1.edad} \n")
persona1.mostrar_detalle()
persona1.carrera = "Ingenieria en Computacion"
print(f"Y su carrera es {persona1.carrera}\n\n") #Se le pueden crear atributos dentro de la marcha, pero esto no se aplica a todas las clases, solo al objeto en cuestion

persona2 = Persona("Rex", "PerroBeibe", 7)
# print(f"El nombre de la persona 2 es: {persona2.nombre} {persona2.apellido} \ny su edad es: {persona2.edad} \n")
Persona.mostrar_detalle(persona2) #Podemos usar el nombre de la clase y pasamos como parametro el objeto para que jale 
# print(f"Y es {persona2.carrera}") #No tiene definido el atributo carrera, se puede definir durante la marcha al objeto, pero no se hizo
