#1er utilizar modulos
import modulos

modulos.borrarPantalla()
print(modulos.saludar("solomeo paredes"))

#2da forma 

from modulos import saludar,borrarPantalla,espereTecla

print(saludar("solomea paredes"))

nombre4=input("ingresa nombre del contacto: ")
telefono4=input("ingresa su numero de telefono: ")

nom4,tel4=modulos.solicitarDatos4(nombre4,telefono4)

print(f"\tNombre completo: {nom4} \n\tTelefono:{tel4}")