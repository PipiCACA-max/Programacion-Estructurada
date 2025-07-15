#DICT U OBJETO para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma)
#            "nombre":"",
#           "categoria":"",
#            "clasificacion":"",
#            "genero":"idioma",
#            }
import mysql.connector
from mysql.connector import Error

pelicula={}
def borrarpantalla():
    import os
    os.system("cls")

def esperartecla():
    input("\t Oprima cualquier tecla para continuar ...")
    borrarpantalla()

def conectar():
    try:
        conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_peliculas"
        )

        return conexion
    except Error as e:
        print (f"el error que sucedio es: {e}")
        return None

def crearPeliculas():
    borrarpantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t.::\U0001F4DD Alta de Peliculas \U0001F4DD::. ")
        pelicula.update({"nombre":input("Ingresa el nombre: ".upper().strip())}) 
        pelicula.update({"categoria":input("Ingresa la categoria: ".upper().strip())}) 
        pelicula.update({"clasificacion":input("Ingresa la clasificacion: ".upper().strip())}) 
        pelicula.update({"genero":input("Ingresa el genero: ".upper().strip())}) 
        pelicula.update({"idioma":input("Ingresa el idioma: ".upper().strip())}) 
        

        #####AGREGAR REGISTRO A LA BD
        try:
            cursor=conexionBD.cursor()
            sql="insert into peliculas (id,nombre,categoria,clasificacion,genero,idioma) values (null,%s,%s,%s,%s,%s)"
            val=(pelicula['nombre'],pelicula['categoria'],pelicula['clasificacion'],pelicula['genero'],pelicula['idioma'])
            cursor.execute(sql,val)
            conexionBD.commit()
            input("\n\t\t :::\u2705 LA OPERACION SE REALIZO CON EXITO! \u2705:::")
        except Error:
            print("error al intentar insertar un registro en la BD")
    else:
        print("No se pudo establecer conexion")

def borrarPeliculas():
    borrarpantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t\t\t.:: \U0001F50D Borrar una Pelicula \U0001F50D::. \n")
        cursor=conexionBD.cursor()
        nombre=input("\tDame el nombre de la pelicula a eliminar: ").upper().strip()
        sql="select * from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()

        print(f"{'ID':<10}{'NOMBRE':<15}{'CATEGORIA':<15}{'CLASIFICACION':<15}{'GENERO':<15}{'IDIOMA':<15}")
        print("-"*80)
        for fila in registros:
            print (f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
        print("-"*80)
        if registros:
            resp=input(f"Deseas eliminar esta pelicula de {nombre}? Si/No: ").lower().strip()
            if resp=="si":
                sql="delete from peliculas where nombre=%s"
                val=(nombre,)
                cursor.execute(sql,val)
                conexionBD.commit()
                input("\n\t\t :::\u2705 LA OPERACION SE REALIZO CON EXITO! \u2705:::")
        else:
            print("\t \u26A0 No existe esa pelicula en el sistema \u26A0")

def mostrarPeliculas():
    borrarpantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t.:: \U0001F50D Consultar o Mostrar la Pelicula \U0001F50D::. \n")
        cursor=conexionBD.cursor()
        sql="select * from peliculas"
        cursor.execute(sql)
        registros=cursor.fetchall()

        if registros:
            print(f"{'ID':<10}{'NOMBRE':<15}{'CATEGORIA':<15}{'CLASIFICACION':<15}{'GENERO':<15}{'IDIOMA':<15}")
            print("-"*80)
            for fila in registros:
                print (f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
            print("-"*80)
        else:
            print("\t \u26A0 No hay peliculas en el sistema \u26A0")

def modificarPeliculas():
    borrarpantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t\t\t.:: \U0001F50D Modificar una Pelicula \U0001F50D::. \n")
        cursor=conexionBD.cursor()
        nombre=input("\tDame el nombre de la pelicula a modificar: ").lower().strip()
        sql="select * from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()

        if registros:
            resp=input("\n\tDeseas modificar la pelicula? Si/No: ").lower().strip()
            if resp=="si":
                print(f"{'ID':<10}{'NOMBRE':<15}{'CATEGORIA':<15}{'CLASIFICACION':<15}{'GENERO':<15}{'IDIOMA':<15}")
                print("-"*80)
                for fila in registros:
                    print (f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
                print("-"*80)

                pelicula["nombre"]=input("Ingresa el nombre: ").upper().strip()
                pelicula["categoria"]=input("Ingresa la categoria: ").upper().strip()
                pelicula["clasificacion"]=input("Ingresa la clasificacion: ").upper().strip()
                pelicula["genero"]=input("Ingresa el genero: ").upper().strip()
                pelicula["idioma"]=input("Ingresa el idioma: ").upper().strip()

                sql="UPDATE peliculas SET nombre=%s,categoria=%s,clasificacion=%s,genero=%s,idioma=%s WHERE nombre=%s;"
                val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"],nombre)
                cursor.execute(sql,val)
                conexionBD.commit()
                input("\n\t\t :::\u2705 LA OPERACION SE REALIZO CON EXITO! \u2705:::")
        else:
            print("\t \u26A0 No existe esa pelicula en el sistema \u26A0")

def buscarPeliculas():
    borrarpantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t\t\t.:: \U0001F50D Buscar una Pelicula \U0001F50D::. \n")
        cursor=conexionBD.cursor()
        nombre=input("\tDame el nombre de la pelicula a buscar: ").lower().strip()
        sql="select * from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()

        if registros:
            print(f"\n{'ID':<10}{'NOMBRE':<15}{'CATEGORIA':<15}{'CLASIFICACION':<15}{'GENERO':<15}{'IDIOMA':<15}")
            print("-"*80)
            for fila in registros:
                print (f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
            print("-"*80)
        else:
            print("\t \u26A0 No existe esa pelicula en el sistema \u26A0")

def borrarCaracteristicaPeliculas():
    borrarpantalla()
    print("\n\t .:: 🗑️ Borrar Característica de Película ::.\n")
    if len(pelicula) > 0:
        for clave, valor in pelicula.items():
            print(f"\t{clave} : {valor}")
        atributo = input("\n¿Qué característica deseas borrar?: ").lower().strip()
        try:
            pelicula.pop(atributo)
            print("\n\t✅ Característica eliminada con éxito.")
        except KeyError:
            print(f"\n\t \u26A0 La característica '{atributo}' no existe, pruebe con alguna que se muestra anteriormente")
    else:
        print("\t⚠ No hay películas registradas.")
    esperartecla()
    
def borrarCaracteristicaPeliculas2():
    borrarpantalla()
    print("\n\t .:: 🗑️ Borrar Característica de Película ::.\n")
    if len(pelicula) > 0:
        for clave, valor in pelicula.items():
            print(f"\t{clave} : {valor}")
        atributo = input("\n¿Qué característica deseas borrar?: ").lower().strip()
        if atributo in pelicula:
            pelicula.pop(atributo)
            print("\n\t✅ Característica eliminada con éxito.")
        else:
            print("\n\t⚠ Característica no encontrada.")
    else:
        print("\t⚠ No hay películas registradas.")
    esperartecla()