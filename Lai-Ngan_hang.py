t=int(input())
while t>0:
    [n,x,m] = [float(x) for x in input().split()]
    i=1
    while n*pow(1+x/100,i)<m:
        i+=1
    print(i)
    t-=1
