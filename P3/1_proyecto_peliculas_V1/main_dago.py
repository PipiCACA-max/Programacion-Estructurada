"""
AHORA CON BD
"""

import peliculas

peliculas.borrarpantalla()
opcion = True
while opcion:
    print(
        "\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Agregar película  \n\t\t 2.- Borrar película \n\t\t 3.- Mostrar películas \n\t\t 4.- Modificar pelíula \n\t\t 5.- Buscar película \n\t\t 6.- SALIR  "
    )
    opcion = input("\t\t\t Elige una opción: ").upper()

    peliculas.borrarpantalla()
    match opcion:
        case "1":
            print(".:: Agregar Peliculas ::.")
            peliculas.crearPeliculas()
            peliculas.esperartecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.esperartecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperartecla()
            peliculas.borrarpantalla()
        case "4":
            peliculas.modificarPeliculas()
            peliculas.esperartecla()
        case "5":
            peliculas.buscarPeliculas()
            peliculas.esperartecla()
        case "6":
            opcion = False
            peliculas.borrarpantalla()
            print("\n\tTerminaste la ejecucion del SW")
        case _:
            peliculas.borrarpantalla()
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")