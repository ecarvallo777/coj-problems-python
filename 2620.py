def cuantasA():
	radio= int(raw_input())
	diametro=radio*2*2
	return diametro
def dibujarA(diametro):
    dibujo=[]
    i=0
    u=0
    word=""
    dibujo.append("A")
    while i<diametro:
    	dibujo.append("a")
    	i=i+1
    dibujo.append("h")
    tam=len(dibujo)

    while u<tam:
    	word=word+dibujo[u]
    	u=u+1
    print(word)


def arrancar():
	a=cuantasA()
	dibujarA(a)
arrancar()