def insertHora():
    hora_general=raw_input()
    hora_general=hora_general.split()
    if int(hora_general[0]) == 0 and int(hora_general[1]) == 0 and int(hora_general[2]) == 0 and int(hora_general[3]) == 0:
        quit()
    else: return hora_general

def definirActual(hora_general):
    hora_general[0]=int(hora_general[0])
    if hora_general[0]==0:
        hora_general[0]=24

    horas_actual=int(hora_general[0]*60)


    minutos_actual=int(hora_general[1])

    sumamin_act=horas_actual+minutos_actual
    return sumamin_act

def definirDespertador(hora_general):
    hora_general[2]=int(hora_general[2])
    if hora_general[2]==0:
        hora_general[2]=24

    horas_despertador=int(hora_general[2])*60
    minutos_despertador=int(hora_general[3])
    sumamin_desp=horas_despertador+minutos_despertador
    return sumamin_desp
def arrancar():
    i=0
    while i<i+1:

        horaGeneral=insertHora()
        actual=definirActual(horaGeneral)
        despertador=definirDespertador(horaGeneral)

        dia=1440
        if actual>despertador:
            rest=(dia+despertador)-actual
            #rest=(dia+actual)-despertador
        elif actual<despertador:

            rest=despertador-actual
        print(rest)
        i=i+1

arrancar()