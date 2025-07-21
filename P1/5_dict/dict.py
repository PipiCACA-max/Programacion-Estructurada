""""
dict.-
es un tipo de datos que se utiliza para almacenar datos de diferentes tipos de datos pero en lugar de tener como las listas 
indices numericos tiene alfanumericos. Es decir, es algo parecido como los objetos.

tambien se conoce como un arreglo asosiativo u objeto JSON

el diccionario es una coleccion ordenada y modificable. No hay miembros duplicables
"""

import os
os.system("cls")

#Lista de paises
#paises=["Mexico","Brasil","Canada","España"]

#Dict u Objeto
paises_mexico={
        "nombre":"Mexico",
        "capital":"CDMX",
        "poblacion":12000000,
        "idioma":"español"
        }

paises_brasil={
        "nombre":"Brasil",
        "capital":"Brasilia",""
        "poblacion":10000000,
        "idioma":"portugues"
        }

paises_canada={
        "nombre":"Canada",
        "capital":"Ottawa",
        "poblacion":9000000,
        "idioma":["ingles","frances"]
        }

alumnos1={
        "nombre":"solomeo",
        "apellido1":"paredes",
        "apellido2":"mojica",
        "carrera":"TI",
        "matricula":"TI123456",
        "area":"software multiplataforma",
        "modalidad":"BIS",
        "semestre":"2"
        }

#mostrar el contenido del diccinario
for i in alumnos1:
    print(f"{i}: {alumnos1[i]}")

#agregar un campo o atributo
alumnos1["telefono"]="1234567"
for i in alumnos1:
    print(f"{i}: {alumnos1[i]}")

