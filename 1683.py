def insertCases():
    cases=int(raw_input())
    i=0
    while i<cases:
        run()
        i=i+1
def run():
    numero=insertNum()
    suma=searchDiv(numero)
    clasifSuma(numero, suma)

def insertNum():
    num=int(raw_input())
    return num

def searchDiv(numero):
    i=1
    sum=0
    while i<numero:
        if (numero % i  == 0):
            sum=sum+i
        i=i+1
    return sum

def clasifSuma(numero, suma):
    if suma<numero:
        print("Deficient")
    elif suma>numero:
        print("Abundant")
    elif suma==numero:
        print("Perfect")
insertCases()