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

[n,m]=[int (x) for x in input().split()]
a=[]
for i in range(n):
    arr=list(map(int, input().split()))
    a.append(arr)
for i in range (n):
    for j in range (m):
        if isPrimeNumber(a[i][j]):
            a[i][j]=1
        else:
            a[i][j]=0
for i in range (n):
    for j in range (m):
        print(a[i][j],end=' ')
    print()