n=int(input())
lop=0
li=["1",]
a="1"
while lop<n-1: 
    a=a+str(lop+2) 
    li.append(a) 
    lop=lop+1
s=len(li) 
i =0
t=0
cont=0
while i<s: 
	x=lista[i] 
	z=len(x) 
	i=i+1
	u=0
	while u<z:
		p= int(x[u]) % 3
		if p == 0:
			cont=cont+1
		u=u+1
print(cont)

