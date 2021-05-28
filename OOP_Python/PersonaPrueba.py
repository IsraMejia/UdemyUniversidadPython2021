from Persona import Persona 
#Del modulo/archivo Persona, importamos la clase Persona   . importar todas las clases es con '*'
print('\n\t\t Modulos\n')
print('Creacion de Objetos'.center(50,'-')) #centramos con 50 quion bajos en total
persona1 = Persona('Bella', 'Poarch', 23)
persona1.mostrar_detalle()

# print(__name__)  #dunder name =  Nos dice el nombre del modulo 
    #Si nos sale __main__ se refiere que el modulo ejecutado es del propio archivo

print('Eliminacion de Objetos'.center(40,'-'))
del persona1 #Para Eliminar o Destruir el objeto en cuestion
