from Persona import Persona, Empleado

persona1 = Persona('Bella' , 23)
print(persona1) # = print(persona1.__str__()) <-Lo sobre esceribimos para que no muestre la direccion de memoria del objeto, sino sus atributos

empleado1 = Empleado('Isra', 23, 6000)
print(empleado1) # = print(persona1.__str__()) de la clase Empleado que se sobre escribio