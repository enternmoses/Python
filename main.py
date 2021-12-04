"""Ham sumFactor tong cac uoc cua mot so"""
def sumFactor(n):
    sum = 0
    for i in range(1,n+1):
        if(n%i==0):
            sum+=i
    return sum

n=int(input())
print(sumFactor(n))