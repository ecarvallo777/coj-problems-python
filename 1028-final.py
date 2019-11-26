i=0
u=20
while i<20:
    phrase= raw_input()
    phrase=phrase.split()

    word_1=phrase[0]
    word_2=phrase[1]

    tam_1=len(word_1)
    tam_2=len(word_2)

    def verificar(tam1, tam2, word_1, word_2):
        i=0
        u=0
        result=[]
        while i<tam1:
            if word_1[i] in word_2[u]:
                result.append(word_2[u])
                i=i+1
                u=u+1
            else:
                u=u+1
            if u>=tam2:
                i=tam1
        return result
    def convert(result):
        i=0
        tam=len(result)
        string=""
        while i<tam:
            string=string+result[i]
            i=i+1
        return string
    def comparar(word_1, string):
        if word_1 in (string):
            print("Yes")
        else:
            print("No")

    result= verificar(tam_1, tam_2, word_1, word_2)
    string=convert(result)

    comparar(word_1, string)
    i=i+1

