def casos():
    casos=int(raw_input())
    i=0
    while i<casos:
        insert()
        i=i+1

def insert():
    intervalo_=raw_input()
    intervalo_=intervalo_.split()

    interval=intervalo(intervalo_)

    sumatoria(interval)


def intervalo(intervalo):
    a=int(intervalo[0])
    b=int(intervalo[1])
    sec=[]
    while a<=b:
        plus=(a)*(a+1)*(a+2)
        sec.append(plus)
        a=a+1
    print(sec)

    return sec

def sumatoria(interval):

    tam=len(interval)
    i=0
    suma=0

    while i<tam:
        a=int(interval[i])
        suma=suma+((a-1)*(a)*(a+1)+(a)*(a+1)*(a+2))
        i=i+1
    suma=suma%100
    print(suma)

casos()