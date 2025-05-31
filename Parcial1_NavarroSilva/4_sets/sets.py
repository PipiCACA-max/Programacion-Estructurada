""""
set es una coleccion desordenada, inmutable y no indexada 
no hay miembros duplicados
"""
import os
os.system("cls")

personas={"ramiro","choche","lupe"}
print (personas)

personas.add("peje")
print (personas)

"""personas.pop()
print (personas)

personas.clear()
print(personas)"""

varios={3.12,3,True,"pipikk"}
print(varios)

os.system("cls")
#ejemplo crear un programa que solicite los emails de los alumnos de la utd. Almacenar en una lista y posteriormente mostrar 
# en pantalla los mails sin duplicar

opc="si"
emails=[]
while opc=="si":
    emails.append(input("ingrese email: "))
    opc=input("otro?").lower()

print(emails)


