a=list(map(int,input().split('')
b=len(a)
s=1
for i in range(1,b+1):
	s=s*i
print(s,end=',')
