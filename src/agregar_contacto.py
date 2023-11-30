import os
def clean_terminal():
    if os.name == "nt":
        os.system("cls")
        
def agregar_contacto():
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
    contactos_lista = [{"nombre":"", "apellidos":"" , "telefonos": "" }]
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
                        
                if len(telefono_str) > 9:
                    print("ERROR, el numero de telefono no puede tener más de 9 caracteres.")  
                else:  
                    contactos_lista[0]["telefonos"]=telefono_str
            #si me ponen mas de un telefono lo que hace es reemplazar por el valor nuevo
        print("contacto creado correctamente")
    
    except ValueError:
        print("No puedes introducir letras en el numero de telefono.")
            #si pulso enter para salir del bucle me salta el valueError igual
            #Si pongo espacios en el email tambien me salta el valueError
        

def mostrar_menu():
    print("Hola")
    
        
        
def main():
    clean_terminal()
    agregar_contacto()
    
    
    
if __name__ == "__main__":
    main()