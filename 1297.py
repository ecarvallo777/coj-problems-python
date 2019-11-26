a = int(input())
i = 0
q= 495
x=0
while i < a:
    b = int(input())
    x = b % q
    if x != 0:
        print("NO")
    else:
        print ("YES")
    i=i+1
