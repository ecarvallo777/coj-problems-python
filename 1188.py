a = raw_input() #input() for python 3.x
a = a.split()
x = a[0]
y = a[1]

i=len(x) # Longitud del primer número
u= len(y) # Longitud del segundo número
p=0 # Contador del primer número
cow=0 # Multiplicación
while p<i:
    o=0 #Contador del segundo número
    while o<u:
        cow= int(x[p])*int(y[o]) + cow
        o=o+1
    p=p+1
print(cow)
