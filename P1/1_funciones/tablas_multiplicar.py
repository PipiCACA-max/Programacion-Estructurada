"""
crear un programa que calcule e imprima cualquier de multiplicar

con funciones que regrese valor y utilize parametros
"""
#v1
"""numero=int(input("tabla de multiplicar del: "))
print(f"{numero}x1: {numero*1}")
print(f"{numero}x2: {numero*2}")
print(f"{numero}x3: {numero*3}")
print(f"{numero}x4: {numero*4}")
print(f"{numero}x5: {numero*5}")
print(f"{numero}x6: {numero*6}")
print(f"{numero}x7: {numero*7}")
print(f"{numero}x8: {numero*8}")
print(f"{numero}x9: {numero*9}")
print(f"{numero}x10: {numero*10}")"""

#v2

#for
"""for i in range(1,11):
    print(f"{numero}x{i}={numero*i}")"""

#while
"""while i<=10:
    print(f"{numero}x{i}={numero*i}")
    i+=1"""

#v3
def tablaMultiplicar(numero):
    num=numero
    mensaje=""
    for i in range (1,11):
        mensaje=print(f"{num}x{i}={num*i}")

    return mensaje

numero=int(input("tabla del: "))
mensaje=tablaMultiplicar(numero)
print(mensaje)