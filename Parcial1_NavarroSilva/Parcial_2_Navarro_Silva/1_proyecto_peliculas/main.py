"""Crear un proyecto que permita gestionar (administrar) peliculas, colocar un menu de opciones para agregar, eliminar, modificar y consultar peliculas
Notas:
1.-Utilizar funciones y mandar llamar desde otro archivo
2.-Utilizar listas para almacenar los nombres de peliculas
"""
import peliculas

peliculas.borrarPantalla()

print("\n\t\t\t..::CINEPOLIS CLON::..\n\t\t..::Sistema de Gestión de Películas::..\n\n" \
"\t\t1.-Agregar \n" \
"\t\t2.-Eliminar \n" \
"\t\t3.-Actualizar \n" \
"\t\t4.-Consultar \n" \
"\t\t5.-Buscar \n" \
"\t\t6.-Vaciar \n" \
"\t\t7.-SALIR")

opcion = True

while opcion:
    
    opcion=input("\n\t\tElige una opción: ").upper()

    match opcion:
        case "1":
            print("..::Agregar::..")
            peliculas.agregarPeliculas()
        case "2":
            print("..::Eliminar::..")
            peliculas.eliminarPeliculas()
            peliculas.esperarTecla()
        case "3":
            print("..::Actualizar::..")
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
        case "4":
            print("..::Consultar::..")
            peliculas.consultarPeliculas()
            peliculas.esperarTecla()
        case "5": 
            print("..::Buscar::..")
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case "6":
            print("..::Vaciar::..")
            peliculas.vaciarPeliculas()
            peliculas.esperarTecla()
        case "7":
            
            opcion=False
            peliculas.borrarPantalla()
            print("\n\tTerminaste la ejecucion del SW\n")
        case _:
            peliculas.borrarPantalla()
            print("\n\tOpción no válida, vuelva a intentarlo por favor")
