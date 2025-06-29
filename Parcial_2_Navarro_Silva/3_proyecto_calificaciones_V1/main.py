'''Crear un proyecto que permita gestionar calificaciones, colocar un menu de opciones para agregar, 
eliminar, calcular promedio de calificaciones de un estudiante

notas:
1._Utilizar funciones y mandar a llamar desde otros archivo
2._Utilizar listas para los nombre del alumno

'''
import calificaciones

def main():
    
    datos = []

    opcion = True
    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menu_principal()

        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_promedio(datos)
                calificaciones.esperarTecla()
            case "4":
                calificaciones.borrarPantalla()
                print("Terminaste la ejecucion del SW")
            case _:
                opcion=True
                print("Opcion invalida, vuelva a intentarlo")
                calificaciones.esperarTecla()

if __name__ == "__main__":
    main()



