import math
t=int(input())
while t>0:
    a = int(input())
    b = int(input())
    print(int(a*b//math.gcd(a,b)))
    t-=1
