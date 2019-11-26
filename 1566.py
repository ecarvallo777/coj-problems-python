def insert():
    i=0
    u=0
    while i==u:
        insertPiramide=int(raw_input())
        if insertPiramide==0:
            quit()
        generate(insertPiramide)
def generate(insertPiramide):
    i=1
    value=0
    while i<=insertPiramide:
        value=value+(i*i)
        i=i+1
    print (value)
insert()