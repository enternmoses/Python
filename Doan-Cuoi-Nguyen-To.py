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
    n=int(input())
    a=n%10000
    if isPrimeNumber(a)==False:
        print('NO')
    else:
        print('YES')
    t-=1
