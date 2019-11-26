def cases():
    loops=int(input())
    i=0
    while i<loops:
        insertNcompare()
        i=i+1
def insertNcompare():
    numbers=input()
    numbers=numbers.split()
    a=int(numbers[0])
    b=int(numbers[1])
    count=0
    for i in range(a,b+1):
        growing=str(i)
        first=growing[0]
        last=growing[len(growing)-1]
        grow_ing=list(growing)
        grow_ing.sort()

        grow=""
        grow=grow.join(grow_ing)
        if growing==grow and first!=last:
            count=count+1
    print(count)

cases()
