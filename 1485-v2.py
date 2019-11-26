c= raw_input()
c=c.split()
c.sort()
x=c[0]
cantLet=len(x)
i=0
u=0
s=[]
palabra=""
while i<cantLet: 
	s.append(x[i])
	i=i+1
s.sort()
while u<cantLet: 
	palabra=palabra+s[u]
	u=u+1

print(palabra)