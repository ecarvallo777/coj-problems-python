casos=int(raw_input())
i=0

while i<casos:
    nums=int(raw_input())
    if (nums % 6) == 0:
        print("YES")
    else:
        print("NO")
    i=i+1