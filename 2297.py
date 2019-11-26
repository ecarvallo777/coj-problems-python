def battlesPlayed():
    bp=int(input())
    i=0
    wonF=0
    while i<bp: 
        wons= battles()
        wonF=wonF+wons
        i=i+1
    print(wonF)
def battles():
    won=0
    combinations=input()
    combinations=combinations.upper()
    if "DC" in combinations:
        pass
    else:
        won=won+1
    return won


battlesPlayed()

