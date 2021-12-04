[n,k] = [int (x) for x in input().split()]
a = list(map(int, input().strip().split()))[:n]
a.sort()
count=0
test = 0
for i in range(1,n):
    if a[i] - a[i-1]<=k:
        test=1
    elif a[i] - a[i-1] > k and test ==1:
        test = 0
        count +=1
    if a[i] - a[i-1] >k and i==n-1:
        count+=1
    if i==n-1 and test ==1:
        count+=1

print(count)