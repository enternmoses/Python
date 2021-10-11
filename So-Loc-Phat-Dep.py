a=input()
check=0
count=0
for i in range(len(a)):
    if a[i]!='6' and a[i] != '8':
        check=1
        break
    elif a[i]=='8':
        count+=1
        if count>2:
            check=1
            break
    else:
        count=0
if check==1 :
    print('NO')
else:
    print('YES')