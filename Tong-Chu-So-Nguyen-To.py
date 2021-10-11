import math
def Prime(n):
    if n<2:
        return False
    else:
        s = int(math.sqrt(n))
        for i in range(2, s + 1):
            if (n % i == 0):
                return False
        return True
t=int(input())
while t:
    n=input()
    count=0
    for i in n:
        count+=int(i)
    if Prime(count):
        print('YES')
    else:
        print('NO')
    t-=1
