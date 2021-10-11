import math
def isPrimeNumber(n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False

    # check so nguyen to khi n >= 2
    squareRoot = int(math.sqrt(n))
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False
    return True
t=int(input())
while t:
    n=input()
    a=0
    b=0
    for i in range(3):
       a+=int(n[i])*int(pow(10,3-i-1))
    b=int(n)%1000
    if isPrimeNumber(a) and isPrimeNumber(b):
        print('YES')
    else:
        print('NO')
    t-=1
