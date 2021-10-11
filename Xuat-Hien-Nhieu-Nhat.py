t=input()
t=int(t)
while t:
	n=int(input())
	a = list(map(int,input().strip().split()))[:n]
	k=max(a)
	check=[]
	for i in range(k+1):
		check.append(0)

	for i in range(n):
		check[a[i]]+=1
	if(max(check)>n/2):
		print(check.index(max(check)))
	else:
		print("NO")

	t-=1
