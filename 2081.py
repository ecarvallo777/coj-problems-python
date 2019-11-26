def cases():
    numeroCasos=int(input())
    i=0
    while i<numeroCasos:
        run()
        i=i+1

def run():
    ciudades=insertCities()
    costoPorEntrada= insertTravel(ciudades[1])
    insertQueries(costoPorEntrada)
    costoPorEntrada=addCities(costoPorEntrada)



def insertTravel(entrada):
    entrada=int(entrada)
    i=0
    costoPorEntrada=[]

    while i<entrada:
        viaje=input()
        viaje=viaje.split()
        costoPorEntrada.append((viaje[0]+"-"+viaje[1]+"-x"+viaje[2]))
        i=i+1
    return costoPorEntrada

def insertCities():
    linea=input()
    linea=linea.split()
    return linea
def addCities(costoPorEntrada):
    print(costoPorEntrada)
    inicio=[]
    final=[]
    i=0
    tam=len(costoPorEntrada)
    while i<tam:
        val=costoPorEntrada[i]
        inicio.append((val[0]))
        final.append(int(val[2]))
        i=i+1
    u=1
    t=0
    maximo=max(final)
    where=0
    while u<=maximo:
        if u in final:
            where=final.index(u)
            select=inicio[where]
            addCities2(u, select, inicio, final, costoPorEntrada)
        u=u+1
def addCities2(final, select, inicio, finalI, costoPorEntrada):
    #print(final)
    #print(inicio)
    convert=""
    where=0
    tam=len(costoPorEntrada)
    i=0
    if str(final) in inicio:
        where=inicio.index(str(final))
        convert=inicio[where] 
        convert2=finalI[where]

        searchINICIO=str(select)+"-"+str(final)
        searchFINAL=str(convert)+"-"+str(convert2)
        tamS=0
        costo=0
        while i<tam:
            servicio=costoPorEntrada[i]
            tamS=len(servicio)
            if searchINICIO in servicio:
                costo=costo+int(servicio[tamS-1])
            if searchFINAL in servicio:
                costo=costo+int(servicio[tamS-1])
            
            i=i+1
        print(costo)
        print(select, final)
        print(convert, convert2)
        quit()


def insertQueries(costoPorEntrada):
    numQueries=int(input())
    i=0
    querySet=""
    while i<numQueries:
        query=input()
        query=query.split()
        querySet=query[0]+"-"+query[1]
        lowCost(querySet, costoPorEntrada)
        i=i+1
def lowCost(querySet, costoPorEntrada):

    tam=len(costoPorEntrada)
    i=0
    tramo=""
    tramor=""
    costos=[]
    costo=0
    while i<tam:
        tramo=costoPorEntrada[i]
        tamaño=len(tramo)
        tramor=tramoR(querySet)
        costo=int(tramo[tamaño-1])
        if querySet in tramo or tramor in tramo:
            costos.append(costo)

        #print(costos)
        i=i+1

def tramoR(tramo):
    tramo=tramo[2]+"-"+tramo[0]
    return tramo

    


cases()