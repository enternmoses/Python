t=int(input())
while t>0:
    s=input()
    s=list(s)
    n=len(s)
    s.reverse()
    for i in range(n-1):
        if(int( s[i])>=5):
            s[i+1]=int(s[i+1])+1
    s.reverse()

    print(s[0],end='')
    for i in range(1,n):
        print("0",end='')
    print("\n")
    t-=1
