import os

peliculas=[]

def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("Oprima cualquier tecla para continuar...")    

def agregarPeliculas():
    borrarPantalla()
    print(".:: Alta de Peliculas ::. ")
    peliculas.append(input("Ingresa el nombre: ").upper().strip())
    input("\n\t\t:::LA OPREACION SE REALIZO CON EXITO:::")

def consultarPeliculas():
    borrarPantalla()

    if len(peliculas)>0:
        print("\n\t.:: Consultar Peliculas ::.")
        for i in range (0,len(peliculas)):
            print(f"{i+1}: {peliculas[i]}")
    else:
        print("\n\t..::NO HAY PELICULAS EN EL SISTEMA::..")
    

def vaciarPeliculas():
    borrarPantalla()
    print("\n\t.::Borrar o quitar todas las peliculas")
    resp=input("Deseas quitar o borrar todas las peliculas del sistema? (Si/No): ").lower()

    if resp=="si":
        peliculas.clear()
        input("\n\t\t:::LA OPREACION SE REALIZO CON EXITO:::")

def buscarPeliculas():
    borrarPantalla()
    print("\n\t.:: Buscar Peliculas ::.")

    pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
    encontro=0

    if not(pelicula_buscar in peliculas):
        print(f"\n\t\tNo se encontro la pelicula {pelicula_buscar}")
        borrarPantalla()
    else:
        for i in range(0,len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                print(f"\nLa pelicula {pelicula_buscar} si la tenemos y esta en la casilla {i+1}")
                encontro+=1
        
        print(f"\nTenemos {encontro} pelicula(s) con este titulo")
        input("\n\t\t:::LA OPREACION SE REALIZO CON EXITO:::")
        borrarPantalla()

def eliminarPeliculas():
    borrarPantalla()
    print("\n\t.:: Eliminar Peliculas ::.")

    pelicula_eliminar=input("Ingrese el nombre de la pelicula a eliminar: ").upper().strip()
    encontro=0

    if not(pelicula_eliminar in peliculas):
        print("\n\t\tNo se encontro la pelicula")
        esperarTecla()
    else:
        resp="si"
        while pelicula_eliminar in peliculas and resp=="si":
            resp=input("Deseas quitar esta pelicula? (Si/No): ").lower()

            if resp=="si":
                posicion=peliculas.index(pelicula_eliminar)
                peliculas.remove(pelicula_eliminar)
                print(f"\nSe elimino la pelicula {pelicula_eliminar} y esta en la casilla {posicion+1}")
                encontro+=1
        
        print(f"\nSe eliminaron {encontro} pelicula(s) con este titulo")
