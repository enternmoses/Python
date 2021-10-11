import math
def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b);

def prime(n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False;
    # check so nguyen to khi n >= 2
    squareRoot = int(math.sqrt(n))
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False
    return True;

n=int(input())
while n>0:
    a = int(input())
    count=0
    for i in range(1, a):
        if uscln(i,a)==1:
            count+=1
    if prime(count):
        print('YES')
    else:
        print('NO')
    n-=1
