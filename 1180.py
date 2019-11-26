def cases():
    cases=int(raw_input())
    i=0
    while i<cases:
        arranque()
        i=i+1

def arranque():
    out=""
    linea=raw_input()
    linea=linea.split()
    i=0

    rest=0
    cPiezas=1
    while i<6:
        if int(linea[i])>cPiezas:
            rest=int(linea[i])-cPiezas
            out=out+str(-rest)+" "
        elif int(linea[i])==cPiezas:
            out=out+"0 "

        elif int(linea[i])<cPiezas:
            rest=cPiezas-int(linea[i])
            out=out+str(rest)+" "
        if i==1:
            cPiezas=2
        if i==4:
            cPiezas=8
        i=i+1
    print(out)
cases()