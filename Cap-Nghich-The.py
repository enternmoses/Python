n = int(input())
count = 0
a = list(map(int,input().strip().split()))[:n]
for i in range(n-1):
	for j in range(i+1,n):
		if (a[i]>a[j]) and (j<n):
			count+=1

print(count)
