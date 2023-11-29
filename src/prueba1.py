def agregar_contacto():
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
    contactos_lista = [{"nombre":"", "apellidos":"", "email":"", "telefono":""}]
    
    todo_ok = False
    while not todo_ok:
        try:
            agregar = input("Desea agregar un contacto? (s/n)").lower()
            if agregar not in {"s","si"}:
                mostrar_menu()
                todo_ok=True
            else:
                nombre = input("Introduzca un nombre -> ").capitalize().strip()
                if nombre =="":
                    raise ValueError
                contactos_lista[0]["nombre"] = nombre
                
                apellidos = input("Introduzca su apellido -> ")
                contactos_lista[0]["apellido"] = apellidos
                
                email = input("Introduzca un email -> ")
                contactos_lista[0]["email"]=email
                
                telefono = input("Introduzca su telefono/s -> ")
                contactos_lista[0]["telefono"]=telefono
        except ValueError:
            print("No puedes dejar el campo vacío.")

def mostrar_menu():
    print("Hola")
    
        
        
def main():
    agregar_contacto()
    
    
    
if __name__ == "__main__":
    main()