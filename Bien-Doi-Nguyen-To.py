import math
def prime(n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False
    # check so nguyen to khi n >= 2
    squareRoot = int(math.sqrt(n))
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False
    return True
n=int(input())
a = list(map(int,input().strip().split()))[:n]
count=0
count_max=0
for i in a:
    count=0
    a=i
    b=i
    if prime(i)==False:
        while 1:
            a+=1
            b-=1
            count+=1
            if prime(a) or prime(b):
                break
        if count_max<count:
            count_max = count
print(count_max)
