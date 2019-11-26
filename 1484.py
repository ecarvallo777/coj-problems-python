def insertTemperature():
    cases=int(raw_input())
    listt=[]
    i=0
    while i<cases:
        listt.append(float(input()))
        i=i+1
    return listt

def arrancar():
    lista=insertTemperature()

    compareTemperature(lista)

def compareTemperature(lista):
    tam=len(lista)
    mayor=max(lista)
    i=0
    index=[]
    while i<tam:
        if lista[i] == mayor:
            index.append(i+1)
        i=i+1
    ind=index[len(index)-1]
    print(ind)
arrancar()


