lista=[]

if len(lista)==0:
    resp=True
    while resp:
        lista.append(input("ingresa contenido del elemento: ").upper().strip())
        resp=input("quieres agregar otro elemento? S/N: ").upper().strip()
        if resp!="S":
            resp=False
    print(lista)
else:
    print("esta vacia")

