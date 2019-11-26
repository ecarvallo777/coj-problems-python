i=0
while i<10:
    child=raw_input()
    child=child.split()
    child=[int(u) for u in child]
    sum=child[0]+child[1]
    if sum>0:
      print(sum)
      i=i+1
    if (child[0] == 0 and child[1] == 0):
    	break
