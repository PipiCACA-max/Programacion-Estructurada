"""
Un modulo es simplemente un archivo con extension py que contiene un codigo de python (funciones,clases,variables,etc).

Un paquete es una carpeta que contiene varios modulos (archivos .py) y un archivo epecial llamado __init__.py, que le indica a
python que esa carpeta debe tratarse como un paquete
"""
import os

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

def borrarPantalla():
    os.system("cls")

def espereTecla():
    input("...Oprima una tecla para continuar...")

def saludar(nombre):
    nom=nombre
    return f"hola, bienvenido: {nom}"
