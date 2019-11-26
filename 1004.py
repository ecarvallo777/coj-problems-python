
track=[]
locate=""

def derecha(m,n,i,u,x):
    result=""
    locate=""
    while u<n: 
        track.append(str(i+x)+","+str(u+x))
        u=u+1
    i=i+1 
    u=u-1
    locate=str(i+x)+","+str(u+x)
    if locate in track or (i+x)>(m-1):
        result="R"
    return result
def abajo(m,n,i,u,x):
    result=""
    locate=""
    while i<m: 
        track.append(str(i+x)+","+str(u+x))
        i=i+1
    u=u-1 
    i=i-1 
    locate=str(i+x)+","+str(u+x)
    if locate in track or (u+x)<(0) :
        result="D"
    return result
def izquierda(m,n,i,u,x):
    result=""
    locate=""
    while n>1: 
        track.append(str(i+x)+","+str(u+x))
        n=n-1
        u=u-1
    u=u+1
    i=i-1
    locate=str(i+x)+","+str(u+x)
    if locate in track:
        result="L"
    return result
        
def arriba(m,n,i,u,x):
    result=""
    locate=""
    while m>2:
        track.append(str(i+x)+","+str(u+x))
        m=m-1
        i=i-1
    u=u+1
    i=i+1
    locate=str(i+x)+","+str(u+x)
    if locate in track:
        result="U"
    return result        
def arranque():
    select=input()
    select=select.split()
    x=0
    m=int(select[0])
    n=int(select[1])
    i=0
    u=0
    result=""
    while n or m >= 0:
        
        result=derecha(m, n, i, u,x)
        result=abajo(m, n, i, u,x)
        result=izquierda(m, n, i, u,x)
        result=arriba(m, n, i, u,x)
        x=x+1
        m=m-2
        n=n-2
    print(result)

def casos():
    cantidad=int(input())
    i=0
    while i<cantidad:
        arranque()
        i=i+1
casos()