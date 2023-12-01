
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


def borrar_consola():
    """ Limpia la consola
    """
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
        
        
        
def agregar_contacto(contactos_lista:list):
    """Agrega contactos a la base de datos
    
    args:
        lista_correos(list): comprueba los correos ya añadidos y si algunos se repite dirá que no se puede añadir ese correo debido a que ya existe
        agregar (str): pregunta si quieres agregar un contacto o no
        nombre (str): Pide un nombre ¿hay que poner si lo pone en mayus y le quita los espacios?
        
    
    """
    #TODO: Crear función para agregar un contacto. Debes tener en cuenta lo siguiente:
    # - El nombre y apellido no pueden ser una cadena vacía o solo espacios y se guardarán con la primera letra mayúscula y el resto minúsculas (ojo a los nombre compuestos)
    
    # - El email debe ser único en la lista de contactos, no puede ser una cadena vacía y debe contener el carácter @.
    # - El email se guardará tal cuál el usuario lo introduzca, con las mayúsculas y minúsculas que escriba. 
    #  (CORREO@gmail.com se considera el mismo email que correo@gmail.com)
    
    # - Pedir teléfonos hasta que el usuario introduzca una cadena vacía, es decir, que pulse la tecla <ENTER> sin introducir nada.
    # - Un teléfono debe estar compuesto solo por 9 números, aunque debe permitirse que se introduzcan espacios entre los números.
    # - Además, un número de teléfono puede incluir de manera opcional un prefijo +34.
    
    # - De igual manera, aunque existan espacios entre el prefijo y los 9 números al introducirlo, debe almacenarse sin espacios.
    # - Por ejemplo, será posible introducir el número +34 600 100 100, pero guardará +34600100100 y cuando se muestren los contactos, el telófono se mostrará como +34-600100100.
    
    lista_correos = []
    contactos_generales = {}
    salir = False
 
    try:
        agregar = input("Desea agregar un contacto? (s/n)").lower()
        if agregar not in {"s","si"}:
            mostrar_menu()
                
        else:
            nombre = input("Introduzca un nombre -> ").capitalize().strip()#si es un nombre compuesto no puedo usar el strip podria separar con un if tienes nombre compuesto? si, pasa esto, no, con strip.
            if nombre =="":
                raise ValueError(print, "No puedes dejar el campo vacío.")
            contactos_lista[0]["nombre"] = nombre
                
            apellidos = input("Introduzca su apellido -> ").capitalize()
            contactos_lista[0]["apellidos"] = apellidos
                
            email = input("Introduzca un email -> ").strip()
            email_guardado = email.lower()
            
            lista_correos.append(email_guardado)# a parte que siempre contenga el @ 
            
                
            if email_guardado == lista_correos[::]:
                print("Error, ese correo ya existe")
            else:
                contactos_generales[email]=contactos_lista
                    
       
            while not salir:
                

                telefono_int = int(input("Introduzca su telefono/s pulse enter para dejar de añadir números -> "))
                telefono_str = str(telefono_int).replace("   ", "-")
                    
                if telefono_int =="":
                    salir=True
                        
                if len(telefono_str) != 9 :
                    print("ERROR, el numero de telefono no puede tener más de 9 caracteres.")  
                else:  
                    contactos_lista[0]["telefonos"].append(telefono_int)
                #validar que tenga el +34
            print("contacto creado correctamente")
    
    except ValueError:
        print("No puedes introducir letras en el numero de telefono.")
            #si pulso enter para salir del bucle me salta el valueError igual
            #Si pongo espacios en el email tambien me salta el valueError



   
def cargar_contactos(contactos_generales: list):
    #FUNCIONA A MEDIAS, HACE FALTA BORRAR EL NUMERO DEL TIO PESAO QUE NO TIENE NUMERO
    #HACER QUE NO PETE CON EL TIO QUE NO TIENE NUMERO DE TELEFONO
    
    #PASARLE CONTACTOS GENERALES DE LA FUNCION AGREGAR DATOS__________________________________---------------------
    
    #TODO: Modificar la función cargar_contactos para que almacene todos los contactos del fichero en una lista con un diccionario por contacto (claves: nombre, apellido, email y telefonos)
    
    """ Carga los contactos iniciales de la agenda desde un fichero
    ...
    """
    contactos_generales_archivo=[]
    prefijo = "+34"
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
                    contactos_generales_archivo[info[2]]=contactos_lista
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
        print("ERROR* se paso de la longitud de la lista.")
    except FileNotFoundError:
        print("ERROR* no se encuentra el archivo.")
    except Exception:
        print("*ERROR")
            


def eliminar_contacto(contactos: list, email_buscar: str, email_buscar_archivos: str ):
    """ Elimina un contacto de la agenda
    ...
    """
    try:
        #TODO: Crear función buscar_contacto para recuperar la posición de un contacto con un email determinado

        if pos != None:
            del contactos[pos]
            print("Se eliminó 1 contacto")
        else:
            print("No se encontró el contacto para eliminar")
    except Exception as e:
        print(f"**Error** {e}")
        print("No se eliminó ningún contacto")
        
def buscar_contacto(contactos_generales_archivos:list, contactos_generales:list):
    
    email_buscar_archivos = contactos_generales_archivos[0]
    
    email_buscar = contactos_generales[0]
    
    return email_buscar, email_buscar_archivos

def mostrar_menu():
    print("Hola")

def main():
    borrar_consola()
    
    contactos_lista = cargar_contactos(contactos_generales)
    
    contactos_generales = agregar_contacto(contactos_lista)
    
    
if __name__ == "__main__":
    main()