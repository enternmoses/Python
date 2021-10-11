import math
def isPrimeNumber(n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False;

    # check so nguyen to khi n >= 2
    squareRoot = int(math.sqrt(n));
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False;
    return True;

n= int(input())
a = list(map(int,input().strip().split()))[:n]
count = {}
for i in a:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in count:
    if(isPrimeNumber(i)):
        print(i, count[i])