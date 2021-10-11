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
    count=len(n)
    count_prime=0
    for i in n:
        if isPrimeNumber(int(i)):
            count_prime+=1
    if isPrimeNumber(count) and count_prime>count/2:
        print('YES')
    else:
        print('NO')
    t-=1
