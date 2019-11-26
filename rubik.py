
track=[]

def recorrer(m,n,i,u,x):
    locate=""

    #Derecha #Recorrer n con contador u
    while u<n: #contador u veces a n
        track.append(str(i+x)+","+str(u+x))
        u=u+1
    i=i+1 #i se acomoda doblando a la derecha
    u=u-1 #Se le resta el último bucle del while a u para estabilizar
    locate=str(i+x)+","+str(u+x) #Posición actual

    if locate in track or (i+x)>(m-1):
        print("R")
        #print(track)
        #quit()

        



    #Abajo
    while i<m: #Recorrer m con contador i
        track.append(str(i+x)+","+str(u+x))
        i=i+1
    u=u-1 #Se acomoda doblando a la derecha
    i=i-1 #Se le resta el último bucle del while para estabilizar
    locate=str(i+x)+","+str(u+x) #Posición actual
    if locate in track or (u+x)<(0) :
        #result="D"
        print("D")


    


    #Izquierda
    while n>1: #Recorrer n hacia la izquierda
        track.append(str(i+x)+","+str(u+x))
        n=n-1
        u=u-1
    u=u+1
    i=i-1
    locate=str(i+x)+","+str(u+x)
    if locate in track:
        #result="D"
        print("L")



    #Arriba
    while m>2:
        track.append(str(i+x)+","+str(u+x))
        m=m-1
        i=i-1
    u=u+1
    i=i+1
    locate=str(i+x)+","+str(u+x)
    if locate in track:
        #result="U"
        print("U")
    #x=x+1
    #while u>0

def arranque():
    select=input()
    select=select.split()
    x=0
    m=int(select[0])
    n=int(select[1])
    i=0
    u=0
    while n or m >= 0:
        
        recorrer(m, n, i, u,x)
        x=x+1
        m=m-2
        n=n-2


arranque()