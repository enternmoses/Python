t=int(input())
while t>0:
    s=input()
    n=len(s)
    head=s[0:2]
    tail=s[n-2:n]
    head=list(head)
    tail=list(tail)
    check=1
    for i in range (2):
        if head[i]!=tail[i]:
            print('NO')
            check=0
            break
    if(check==1):
        print("YES")

    t-=1
