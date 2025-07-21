"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple 
  una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla, es decir, mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor
"""
#caso 1
def solicitarDatos1():
    nombre=input("Ingrese su nombre: ")
    telefono=input("Ingrese su numero de telefono: ")

    print(f"Soy funcion 1: El nombre de la persona es: {nombre} y su telefono es: {telefono}")

#caso 3
def solicitarDatos3(nombre3,telefono3):
    nom3=nombre3
    tel3=telefono3

    print(f"Soy funcion 3: El nombre de la persona es: {nom3} y su telefono es: {tel3}")

#caso 2
def solicitarDatos2():
    nombre2=input("Ingrese su nombre: ")
    telefono2=input("Ingrese su numero de telefono: ")

    return nombre2,telefono2

#caso 4
def solicitarDatos4(nombre4,telefono4):
    nom4=nombre4
    tel4=telefono4

    return nom4,tel4

#llamar a mis funciones

#funcion 1
solicitarDatos1()

#funcion 3

solicitarDatos3()

nombre3=input("Ingrese su nombre: ")
telefono3=input("Ingrese su numero de telefono: ")

#funcion 2
nombre2,telefono2=solicitarDatos2()
print(f"nombre: {nombre2} \ntelefono: {telefono2}")

#funcion 4
nom4=input("Ingrese su nombre: ")
tel4=input("Ingrese su numero de telefono: ")

nombre4,telefono4=solicitarDatos4(nom4,tel4)

print(f"nombre: {nombre4} \ntelefono: {telefono4}")

