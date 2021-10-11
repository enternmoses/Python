while 1:
    a=int(input())
    if a!=0:
        count=1
        while a>1:
            if a%2==0:
                a/=2
                count+=1
            else:
                a=a*3+1
                count+=1
        print(count)
    else:
        break
