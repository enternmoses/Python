def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)

t=int(input())
while t:
    n=int(input())
    b=n
    a=0
    while n:
        a=a*10+n%10
        n//=10
    if uscln(a,b)==1:
        print("YES")
    else:
        print('NO')
    t-=1

