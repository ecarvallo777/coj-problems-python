def pedirDulces():
    child=int(input()) 
    i=0
    dulces=0
    while i<child:
        dulces=dulces+int(input())
        i=i+1
    print("")
    return dulces, child

def judge(datos):    
    if (int(datos[0]) % int(datos[1])) == 0:
     print("YES")
    else:
     print("NO")


def casos():
    casos=int(input())
    print("")
    i=0
    while i<casos:
        judge(pedirDulces())
        i=i+1
casos()