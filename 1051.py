n=int(input())
loop=0
lista=["1",]
append="1"
while loop<n-1: #Crear lista con N elementos
    append=append+str(loop+2) #Concatenar digitos
    lista.append(append) #Agregar concatenación a lista
    loop=loop+1 #Aumentar contador
print(lista)

s=len(lista) # Número de elementos en la lista
i=0 #Contador para recorrer elementos de la lista
u=0 #Contador para recorrer digitos de los elementos de la lista
t=0
contDiv=0
while i<s: #Recorrer elementos de la lista 
	x=lista[i] #Crear lista de cada elemento de la lista inicial
	z=len(x) #Define cuantos digitos tiene el elemento actual
	i=i+1
	u=0
	#print(z)
	while u<z:
		p= int(x[u]) % 3
		#print(x[u])
		if p == 0:
			contDiv=contDiv+1
		u=u+1
print(contDiv)

