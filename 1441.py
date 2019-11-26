def arranque():
    i=0
    u=0
    while i==u:

        longitud=raw_input()
        longitud=longitud.split()
        longitud= convert(longitud)
        analysis(longitud)
        c=max(longitud)
        longitud.remove(c)
        c=c*c
        a=longitud[0]*longitud[0]
        b=longitud[1]*longitud[1]
    
        if a+b==c:
            print("right")
        else:
            print("wrong")
def analysis(longitud):
    if longitud[0] == 0 and longitud[1]==0 and longitud[2]==0:
        quit()
def convert(longitud):
    i=0
    tam=len(longitud)
    while i<tam:
        longitud[i]=int(longitud[i])
        i=i+1
    return longitud



arranque()