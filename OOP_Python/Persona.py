class Persona:
    def __init__(self): #El parametro 'self' al metodo inicializador de la clase hace referencia al objeto mismo que se va a crear
        #El doble guion bajo 'dunder' le da el nombre de metodo dunder init
        self.nombre = 'Rex' #Atributo de instancia, del objeto que estamos creando por defecto
        self.apellido  = 'Mejia'
        self.edad = 7
    #pass #permite generar la clase sin  que se le defina atributos o metodos

print("\nLeccion 01 POO\n")
print(type(Persona))

persona1 = Persona() #Los parentesis manda a llamar el metodo inicializador o constructor de la clase __init__

print(f"El nombre de la persona es: {persona1.nombre} {persona1.apellido} \ny su edad es: {persona1.edad} \n")