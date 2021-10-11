t=int(input())
while t:
    n=input()
    count=1
    for i in n:
        if int(i)!=0:
            count*=int(i)
    print(count)
    t-=1
