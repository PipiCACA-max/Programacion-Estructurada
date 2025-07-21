"""
List(Array)

Son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores  se hace con un indice numerico

Nota: sus valores sí son modificables 

La lista es una coleccion ordenada y modificable 
Permite miembros duplicados

"""
import os
os.system("cls")
#Funciones mas comunes en las listas 

paises=["mexico","brasil","españa","canada"]
numeros=[23,12,100,34]

#ordenar ascendentemente 
print(numeros)
numeros.sort()
print(numeros)

paises.sort()
print(paises)

#añadir o ingresar o instertar elementos a una lista

#1er forma
paises.append("honduras")

#2da forma 
paises.insert(1,"honduras")
print(paises)

#eliminar o borrar o quitar elementos a una lista

#1ra forma con el indice
paises.pop(1)
print(paises)

#2da forma con el valor o contenido
paises.remove("honduras")
print(paises)

#buscar un elemento dentro de la lista

#1er forma
resp="Brasil" in paises
if resp==True:
    print("si esta el pais")
else:
    print("no encontre el pais")

#2da forma

for i in range(0,len(paises)):
    if paises[i]=="brasil":
        print("si encontrado")
    else:
        print("pais no encontrado")

#cuantas veces aparece un elemento dentro de la lista
#numeros=[23,12,100,34]
print(f"el numero 12 aparece {numeros.count(12)} vez o veces")
numeros.append(12)
print(f"el numero 12 aparece {numeros.count(12)} vez o veces")

#identificar o conocer el indice de un valor
#paises=["mexico","brasil","españa","canada"]

indice=(paises.index("españa"))
print(indice)

paises.pop(indice)
print(paises)

#recorrer los valores de la lista
#1ra forma (valores)
for i in paises:
    print(i)

#2da forma (indices)
for i in range(0,len(paises)):
    print(f"el valor {i} es: {paises[i]}")

#unir contenido de vistas
#paises=["mexico","brasil","españa","canada"]
#numeros=[23,12,100,34]

print(paises)
print(numeros)
paises.extend(numeros)
print(paises)