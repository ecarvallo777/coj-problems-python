def cases():
	casos=int(raw_input())
	i=0
	while i<casos:
		div()
		i=i+1
def div():
	num=int(raw_input())
	if num % 5 == 0:
		print("YES")
	else: print("NO")
cases()