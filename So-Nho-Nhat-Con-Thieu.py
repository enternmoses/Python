n=int(input())
a = list(map(int,input().strip().split()))[:n]
k=max(a)
check=[]
for i in range(30000+1):
    check.append(0)

for i in range(n):
    check[a[i]]+=1
for i in range(1,max(a)+2):
    if check[i]==0:
        print(i)
        break