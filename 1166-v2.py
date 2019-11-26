loop = int(input()) #Insertar cantidad de ciclos del programa general
i = 0 # Contador general del programa
while i<loop: #bucle general
    digCant= int(input()) #Cantidad de dígitos
    cadDig= input() #Cadena de digitos
    cadDig = cadDig.split() # Convertir String a lista separada por espacios
    u= 0 # Contador de lista a recorrer para separar números
    pair=0 # Contador de pares
    unpair=0# Contador de impares
    while u<digCant: #Bucle para contar pares/impares
    	if int(cadDig[u]) % 2 == 0: #Condición para sumar un par
    		pair=pair+1 #Aumentar contador pares
    	if int(cadDig[u]) % 2 != 0: #Condición para sumar impar
    		unpair=unpair+1 #Aumentar contador impares
    	u=u+1 #Contador bucle lista
    print(str(pair)+' even and ' +str(unpair) +' odd.') #Salida
    i=i+1 #contador bucle general
