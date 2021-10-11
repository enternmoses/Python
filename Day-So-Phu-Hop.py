
def solve():
    check=1
    n=int(input())
    a = list(map(int, input().strip().split()))[:n]
    b = list(map(int, input().strip().split()))[:n]
    a.sort()
    b.sort()
    for i in range(n):
        if(a[i]>b[i]):
            check=0
    return check

t=int(input())
while t>0:
    k=solve()
    if k==1:
        print("YES")
    else:
        print("NO")
    t-=1
