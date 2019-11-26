nums=input()
nums=nums.split()
nums=[int(i) for i in nums]
nums.sort()
i=0
while i<3:
	nums[i]=nums[i]
	i=i+1
a=nums[0]
b=nums[1]
c=nums[2]
append=""
order=input()
order=order.split()
x=order[0]
u=0
while u<3:
    if x[u] == "A":
    	append=append+str(a)+" "
    if x[u] == "B":
    	append=append+str(b)+" "
    if x[u] == "C":
    	append=append+str(c)+" "
    u=u+1
print(append)

