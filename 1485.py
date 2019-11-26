c= input()
c=c.split()
c.sort()
print(c)
x=c[0]
cantLet=len(x)
i=0
u=0
s=[]
palabra=""
while i<cantLet: #Separar letras de la palabra
	s.append(x[i])
	i=i+1
s.sort() #Ordenar letras de la palabra separada
while u<cantLet: #Volver a unir palabra ordenada
	palabra=palabra+s[u]
	u=u+1

print(palabra)