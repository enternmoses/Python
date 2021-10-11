check=0
[a,k,n] = [int(x) for x in input().split()]
i=1
while k*i < n:
    if(k*i - a > 0):
        check=1
        print(k*i - a,end=" ")
    i+=1
if(check==0):
    print('-1')