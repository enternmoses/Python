t=int(input())
while t>0:
    n=list(input())
    sum=0
    lenn=len(n)
    for i in range(lenn):
        sum+=int(n[i])
    check=0
    if sum<=10:
        print('NO')
    else:
        sum=list(map(int,str(sum)))
        i=0

        while i<=len(sum)/2:
            if(sum[i]!=sum[len(sum)-i-1]):
                check=1
                break
            i+=1
        if check==0:
            print('YES')
        else:
            print('NO')
    t-=1
