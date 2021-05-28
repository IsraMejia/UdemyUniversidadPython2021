class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self.edad = edad
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self):#Por defectote muestra la direccion de memoria del objeto en cuestion, vamos a sobre escribirlo
        return f"\nEl objeto tipo Persona: {self.nombre}, con la edad de: {self.edad}\n"




class Empleado (Persona): #Empleado Hereda de Persona
    def __init__(self,  nombre, edad, sueldo):
        super().__init__(nombre, edad) #Usamos el constructor de la clase padre
        self.sueldo = sueldo

    def __str__(self):
        return f" {super().__str__()} Que es un Empleado con un sueldo de {self.sueldo} \n"

# empleado1 = Empleado('Isra', 23, 5000)
# print(f"\nEl emplado: {empleado1._nombre} de {empleado1.edad} años, gana {empleado1.sueldo}")