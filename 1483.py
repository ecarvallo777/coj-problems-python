a = raw_input()
a = a.split()

type= a[0]
r = "rectangle"
s = "square"

if type in r :
    print(int(a[1])*int(a[2]))
if type in s : 
    print(int(a[1])**2)