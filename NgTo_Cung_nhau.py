def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)

n=int(input())
a = list(map(int,input().strip().split()))[:n]
a.sort()
for i in range(0,(n-1)):
    for j in range(i+1,n):
        if(uscln(a[i],a[j])==1 ):
            print(a[i],a[j])

