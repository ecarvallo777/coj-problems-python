loop = int(input()) 
i = 0 
while i<loop:
    digCant= int(input()) 
    cadDig= raw_input()
    cadDig = cadDig.split() 
    u= 0 
    pair=0 
    unpair=0
    while u<digCant: 
    	if int(cadDig[u]) % 2 == 0: 
    		pair=pair+1 
    	if int(cadDig[u]) % 2 != 0: 
    		unpair=unpair+1 
    	u=u+1 
    print(str(pair)+' even and ' +str(unpair) +' odd.')
    i=i+1 
