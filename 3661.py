def insertLine():
    i=0
    u=0
    while u==0:
        linea=raw_input()
        linea=linea.split()

        rotacion=int(linea[0])
        if rotacion==0:
            quit()
        word=linea[1]
        word=list(word)

        reversa= reverseLine(word)
        rotateLine(rotacion, reversa)

def reverseLine(word):
    word.reverse()

    return word
def rotateLine(rotar, reversa):
    diccionario= {91: 95, 92:46}

    tam=len(reversa)
    finalWord=[]
    i=0
    u=0
    while u<tam:

        chars=ord(reversa[u])
        if chars==95:
            chars=91
            reversa.remove(reversa[u])
            reversa.insert(u, chr(chars))
        if chars==46:
            chars=92
            reversa.remove(reversa[u])
            reversa.insert(u, chr(chars))
        u=u+1

    while i<tam:
        char=ord(reversa[i])+rotar
        if char>92:
            char=char-28
        if char==91:
            char=95
        if char==92:
            char=46


        char=chr(char)
        finalWord.append(char)
        i=i+1

    final=""
    final=final.join(finalWord)
    print(final)
insertLine()