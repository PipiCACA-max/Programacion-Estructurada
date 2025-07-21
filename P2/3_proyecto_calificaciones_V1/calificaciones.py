def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\U0001F552Oprima una tecla para continuar...\U0001F552")

def menu_principal():
    print("""	\U0001F44D.::Sistema de gestion de calificaciones::.\U0001F44D
        \n\t\t\U00000031\U000020E3 Agregar 
          \n\t\t\U00000032\U000020E3 Mostrar 
          \n\t\t\U00000033\U000020E3 Calcular promedio 
          \n\t\t\U00000034\U000020E3 Salir""")
    
    opcion=input("\n\t\t\U0001F449Elige una opcion (1-4):")

    return opcion

def agregar_calificaciones(lista):
    borrarPantalla()
    print("\t\t\t\U0001F4DDAgregar calificaciones\U0001F4DD")
    nombre=input("\t\U0001F464Nombre del alumno: ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        continua=True
        while continua:
            try:
                cal=float(input(f"\U0001F4DDCalificacion {i}: "))
                if cal>=0 and cal<11:
                    calificaciones.append(cal)
                    continua=False
                else:
                    print("\u274CIngresa un numero valido\u274C")
            except ValueError:
                print("\t\u274CIngresa un valor numerico\u274C")
    lista.append([nombre]+calificaciones)
    print("\u2705Accion realizada con exito\u2705")

def mostrar_calificaciones(lista):
    borrarPantalla()
    print("\U0001F4C2Mostrar calificaciones\U0001F4C2")
    print(f"\U0001F464{'Nombre':<15}{'Cal.1':<10}{'Cal.2':<10}{'Cal.3':<10}")
    print(f"{'-'*40}")

    if len(lista)>0:
        for fila in lista:
            print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
        print(f"{'-'*40}")
        cuantos=len(lista)
        print(f"\U0001F464Son {cuantos} alumnos")
    else:
        print("\u274Cno hay calificaciones registradas\u274C")
        esperarTecla()

def calcular_promedio(lista):
    borrarPantalla()
    print("..::PROMEDIOS::..")
    if len(lista)>0:
        print(f"{'Alumno':<15}{'Promedio':<10}")
        print(f"{'-'*30}")
        promedio_grupal=0
        for fila in lista:
            nombre=fila[0]
            promedio=sum(fila[1:])/3
            print(f"{nombre:<15}{promedio:.2f}")
            promedio_grupal+=promedio
        print(f"{'-'*30}")
        promedio_grupal=promedio_grupal/len(lista)
        print(f"El promedio grupal es {promedio_grupal}")
    else:
        print("no hay calificaciones registradas")
        esperarTecla()

def calcular_calificaciones(lista):
    borrarPantalla()
    print("..::PROMEDIOS::..")
    if len(lista)>0:
        print(f"{'Alumno':<15}{'Promedio':<10}")
        print(f"{'-'*30}")
        promedio_grupal=0
        for fila in lista:
            nombre=fila[0]
            i=1
            suma=0
            promedio=0
            while i<=3:
                suma+=fila[i]
                i+=1
            promedio=suma/3
            print(f"{nombre:<15}{promedio:.2f}")
            promedio_grupal+=promedio
        print(f"{'-'*30}")
        promedio_grupal=promedio_grupal/len(lista)
        print(f"El promedio grupal es {promedio_grupal}")
    else:
        print("no hay calificaciones registradas")
        esperarTecla()

