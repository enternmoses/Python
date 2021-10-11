t=int(input())
while t:
    n=input()
    sum=0
    prod=1
    for i in range(len(n)):
        if i%2!=0:
            sum+=int(n[i])
        else:
            if int(n[i])!=0:
                prod*=int(n[i])
    print(prod,sum)

    t-=1