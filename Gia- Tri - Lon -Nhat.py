n=int(input())
a = list(map(int, input().strip().split()))[:n]
sum=0
for i in range (n):
    if a[i]>0:
     sum+=a[i]
print(sum*2)