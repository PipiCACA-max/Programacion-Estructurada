"""
agenda_contactos={
    "RUBEN":[1234,"ruben@gmail.com"]
    "MARIA":[5678,"maria@gmail.com"]
}
"""

import agenda

def main():
    agenda_contactos={}
    agenda.borrarPantalla()
    opcion=True

    while opcion:
        agenda.borrarPantalla()
        opcion=agenda.menuPrincipal()
        match opcion:
            case "1":
                agenda.agregar_contacto(agenda_contactos)
                agenda.esperarTecla()
            case "2":
                agenda.mostrar_contacto(agenda_contactos)
                agenda.esperarTecla()
            case "3":
                agenda.buscar_contacto(agenda_contactos)
                agenda.esperarTecla()
            case "4":
                agenda.agregar_contacto(agenda_contactos)
                agenda.esperarTecla()
            case "5":
                opcion=False
                agenda.borrarPantalla()
                print("Terminaste la ejecucion del SW")
            case "6":
                opcion=False
                agenda.borrarPantalla()
                print("Terminaste la ejecucion del SW")
            case _:
                opcion=True
                agenda.borrarPantalla()
                print("Opcion invalida, vuelva a intentarlo")
                agenda.esperarTecla()
                agenda.borrarPantalla()

if __name__ == "__main__":
    main()