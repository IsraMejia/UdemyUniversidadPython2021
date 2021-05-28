from Persona import Persona 
#Del modulo/archivo Persona, importamos la clase Persona   . importar todas las clases es con '*'
print('\n\t\t Modulos')
persona1 = Persona('Bella', 'Poarch', 23)
persona1.mostrar_detalle()

print(__name__)  #dunder name =  Nos dice el nombre del modulo 
    #Si nos sale __main__ se refiere que el modulo ejecutado es del propio archivo
