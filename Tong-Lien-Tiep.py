import math
def solve(n):
    count=0
    k=int(math.sqrt(n))
    a=0
    b=0
    c=0
    d=0
    for i in range(2,k+1):
        if n%i==0:
            c=n/i
            d=i
            if (c+d-1)%2==0:
                a=(c+d-1)/2
                b=c-a
                if b>=1 and a>b:
                    count+=1
    return count
t=int(input())
while t>0:
    num=int(input())
    print(solve(2*num))
    t-=1
