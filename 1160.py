
def areIn(x, y):
    if x==y or x==y+2:
        return True
    else:
        return False
def where(x, y):
    if x%2==0 or y%2==0:
        return x+y
    if x%2!=0 or x%2!=0:
        return x+y-1




def cases():
    casos=int(input())
    i=0
    while i<casos:
        coords=input()
        coords=coords.split()
        x=int(coords[0])
        y=int(coords[1])
        result=areIn(x, y)
        if result==True:
            print(where(x,y))
        else: print("No number")
        i=i+1
cases()