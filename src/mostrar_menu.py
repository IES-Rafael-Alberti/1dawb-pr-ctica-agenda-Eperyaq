def mostrar_menu():
    print("AGENDA: ")
    print("---------------")
    print("1. Nuevo contacto ")
    print("2. Modificar contacto ")
    print("3. Eliminar contacto ")
    print("4. Vaciar agenda")
    print("5. Cargar agenda inicial")
    print("6. Mostrar contacto por criterio")
    print("7. Mostrar agenda completa")
    print("8. Salir")
    
    todo_ok = False
    while not todo_ok:
        try:
            opcion = int(input("Escoge una opcion: "))
            todo_ok = True
        except ValueError:
            ("ERROR numero incorrecto")
    
    return opcion
    
    
def main():
    mostrar_menu()
    
if __name__ == "__main__":
    main()
    #TODO: Crear un menú para gestionar la agenda con las funciones previamente desarrolladas y las nuevas que necesitéis:
    # AGENDA
    # ------
    # 1. Nuevo contacto
    # 2. Modificar contacto
    # 3. Eliminar contacto
    # 4. Vaciar agenda
    # 5. Cargar agenda inicial
    # 6. Mostrar contactos por criterio
    # 7. Mostrar la agenda completa
    # 8. Salir
    #
    # >> Seleccione una opción: 
    #
    #TODO: Para la opción 3, modificar un contacto, deberás desarrollar las funciones necesarias para actualizar la información de un contacto.
    #TODO: También deberás desarrollar la opción 6 que deberá preguntar por el criterio de búsqueda (nombre, apellido, email o telefono) y el valor a buscar para mostrar los contactos que encuentre en la agenda.