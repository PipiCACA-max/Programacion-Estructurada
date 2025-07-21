#ejemplo 1: crear una lista de numeros e imprimir el contenido

import os 
os.system("cls")

numeros = [1,2,3,4]
print (numeros)

for i in numeros:
    print (i)

for i in range (0,len(numeros)):
    print (numeros[i])

#ejemplo 2 crear una lista de palabras y posteriormente buscar la coincidencia de una palabra
os.system("cls")

"""palabras = ["pipi","caca","pefico","cheve","snus","caca"]
print (palabras)

palabra_buscar=input("dame la palabra a buscar: ")

#1er forma
print (f"se encontro: {palabras.count(palabra_buscar)} veces")
if palabra_buscar in palabras:
    resp = palabra_buscar 
    print (f"\nsi encontre {resp}\n")
else:
    resp = palabra_buscar
    print (f"\nno encontre {resp}\n")

#2da forma
encontro = False
contador = 0

for i in palabras:
    if i == palabra_buscar:
        encontro = True
        contador+=1
        
if encontro:
    print (f"\nsi encontre\nse encontro {contador} veces")

else:
    print("\nno encontre\n")

#3ra forma
encontro = False
for i in range (0,len(palabras)):
    if palabras[i]==palabra_buscar:
        encontro = True

if encontro:
    print ("\nsi encontre tu palabra\n")
else:
    print ("\nno encontre tu paalabrra\n")"""

#ejemplo 3 añadir elementos a la lista
"""os.system("cls")

numeros=[]

opc=True
while opc:
    numero=float(input("dame un numero entero o decimal:"))
    numeros.append(numero)

    resp=input("deseas agregar otro numero?:").lower()

    if resp=="si":
        opc=True
    else:
        opc=False

print(numeros)"""

#ejemplo 4 crear una lista multidimensional que sea una agenda
agenda=[
        ["carlos","123456"],
        ["solomeo paredes","445566"],
        ["martin","11223344"]
       ]

print (agenda)

for i in agenda :
    print(i)

for r in range (0,3):
    for c in range (0,2):
        print (agenda[r][c])

cadena=""
for r in range (0,3):
    for c in range (0,2):
        #print (agenda[r][c])
        cadena+=f"{agenda[r][c]}, "
    cadena+="\n"
print(cadena)

#concatenacion de cadenas
#listas multidimensionales