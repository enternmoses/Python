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
        if i%2==0 and int(n[i])%2!=0:
            check=1
            break
        if i%2!=0 and int(n[i])%2==0:
            check=1
            break
        count+=int(n[i])
    if isPrimeNumber(count)==False:
        check=1
    if check==1:
        print('NO')
    else:
        print('YES')
    t-=1
