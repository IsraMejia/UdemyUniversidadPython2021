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



class Empleado (Persona): #Empleado Hereda de Persona
    def __init__(self,  nombre, edad, sueldo):
        super().__init__(nombre, edad) #Usamos el constructor de la clase padre
        self.sueldo = sueldo


empleado1 = Empleado('Isra', 23, 5000)
print(f"\nEl emplado: {empleado1._nombre} de {empleado1.edad} años, gana {empleado1.sueldo}")