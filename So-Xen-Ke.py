t=int(input())
while t:
    n=input()
    count=0
    check=0
    for i in range (len(n)):
        if n[0]==n[1]:
            check=1
            break
        if i%2==0 and i>0:
            if n[0]!=n[i]:
                check=1
                break
        count+=1
    if count%2==0:
        check=1
    if check==1:
        print('NO')
    else:
        print('YES')
    t-=1
