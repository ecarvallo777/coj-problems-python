def cases():
    i=0
    u=0
    while i==u:
        run()
        i=i+1
        u=u+1

def run():
    num= insertNum()
    tamano=howLongNum(num)
    acmv(num, tamano)

def insertNum():
    num=int(raw_input())
    if num==0:
        quit()
    return num

def howLongNum(num):
    tamano=len(str(num))
    return tamano

def acmv(num, tamano):
    i=1
    acm=0
    factorial=0
    u=tamano
    num=str(num)

    while i<=u:
        factorial=factorials(tamano)
        acm=acm+int(num[i-1])*factorial

        i=i+1
        tamano=tamano-1
    print(acm)
def factorials(num):
    fact = 1
    for i in range(1, num):
        fact += fact * i
    return fact

cases()