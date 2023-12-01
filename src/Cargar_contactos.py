import os
import pathlib
from os import path


# Constantes globales
RUTA = pathlib.Path(__file__).parent.absolute() 

NOMBRE_FICHERO = 'contactos.csv'

RUTA_FICHERO = path.join(RUTA, NOMBRE_FICHERO)

#TODO: Crear un conjunto con las posibles opciones del menú de la agenda
OPCIONES_MENU = {1, 2, 3, 4, 5, 6, 7, 8}
#TODO: Utiliza este conjunto en las funciones agenda() y pedir_opcion()


def cargar_contactos():
    #FUNCIONA A MEDIAS, HACE FALTA BORRAR EL NUMERO DEL TIO PESAO QUE NO TIENE NUMERO
    #HACER QUE NO PETE CON EL TIO QUE NO TIENE NUMERO DE TELEFONO
    
    #PASARLE CONTACTOS GENERALES DE LA FUNCION AGREGAR DATOS__________________________________---------------------
    
    #TODO: Modificar la función cargar_contactos para que almacene todos los contactos del fichero en una lista con un diccionario por contacto (claves: nombre, apellido, email y telefonos)
    
    """ Carga los contactos iniciales de la agenda desde un fichero
    ...
    """
    prefijo = "+34"
    contactos_generales = {}
    contactos_lista = [{"nombre":"", "apellido":"",  "email": "", "telefonos": [] }]
    
    #TODO: Controlar los posibles problemas derivados del uso de ficheros...
    #cambiar el print para que se meta en contactos
    try:
        with open(RUTA_FICHERO, 'r') as fichero:
            for linea in fichero:
                info = linea.strip().split(";")
                print(contactos_generales)
                print(len(linea))
                if len(linea) == 33:
                    contactos_generales[info[2]]=contactos_lista
                    contactos_lista[0]["nombre"] = info[0]
                    contactos_lista[0]["apellido"] = info[1]
                    contactos_lista[0]["email"] = info[2]
                else:
                    contactos_generales[info[2]]=contactos_lista
                    
                    contactos_lista[0]["nombre"] = info[0]
                    
                    contactos_lista[0]["apellido"] = info[1]
                    
                    contactos_lista[0]["email"] = info[2]
                    
                    if info[3].startswith(prefijo):
                        contactos_lista[0]["telefonos"].append(info[3])
                        
                    else:
                        contactos_lista[0]["telefonos"].append(info[3])
             
    except IndexError:
        print("eres bobo elia")
        
def main():
    
    cargar_contactos()
    
    
if __name__ == "__main__":
    main()