def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("Ingrese cualquier tecla para continuar...")

def menuPrincipal():
    print("""	\U0001F44D.::Sistema de gestion de calificaciones::.\U0001F44D
        \n\t\t\U00000031\U000020E3 Agregar 
          \n\t\t\U00000032\U000020E3 Mostrar 
          \n\t\t\U00000033\U000020E3 Mostrar contacto 
          \n\t\t\U00000034\U000020E3 Modificar contacto
          \n\t\t\U00000035\U000020E3 Eliminar contacto
          \n\t\t\U00000035\U000020E3 Salir
          """)
    
    opcion=input("\n\t\t\U0001F449Elige una opcion (1-4):")

    return opcion


def agregar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t..::Agregar contacto::..")
    nombre=input("Nombre del contacto: ").upper().strip()
   

    if nombre in agenda:
        print("\n\t\tEl contacto ya existe")
    else:
        telefono=input("Telefono: ").strip()
        email=input("Email: ").lower().strip()
        #agregar el atributo "nombre" al diccionario con los valores de telefono e email en una lista
        agenda[nombre]=[telefono,email]
        print("\n\t\t..::Accion realizada con exito::..")

def mostrar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t..::Mostrar contactos::..")

    if not agenda:
        print("\t\tNo existen contactos en la agenda")
    else:
        for nombre,datos in agenda.items():
            print(f"\n\t{'nombre: '+nombre}\n\t{'telefono: '+datos[0]}\n\t{'email: '+datos[1]}")


