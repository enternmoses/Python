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
    count=0
    check=0
    for i in range (len(n)):
        if isPrimeNumber(i) and isPrimeNumber(int(n[i]))==False:
            check=1
            break
        if isPrimeNumber(i)==False and isPrimeNumber(int(n[i])):
            check=1
            break
    if check==1:
        print('NO')
    else:
        print('YES')
    t-=1
