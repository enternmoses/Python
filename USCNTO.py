import math
def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b);

def is_prime(n):
    if (n < 2):
        return False;
    # check so nguyen to khi n >= 2
    squareRoot = int(math.sqrt(n))
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False
    return True;

t=int(input())
while t>0:
    s=input().split()
    a=int(s[0])
    b=int(s[1])
    k=uscln(a,b)
    k=int(k)
    result=0
    while k>=1:
        result+=k%10
        k//=10
    result=int(result)

    if(is_prime(result)):
        print('YES')
    else:
        print('NO')
    t-=1
