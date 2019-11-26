a = int(input())
i=0
t=[]
while i<a:
    s= int(input())
    t.append(s)
    i=i+1
t.sort()
w=0
k=len(t)
while w<k:
    print(t[w])
    w=w+1