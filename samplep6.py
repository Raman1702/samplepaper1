a=list(map(int,input().split()))
for i in range(1,101):
	if i not in a:
		b=b.append(i)
print(b)
