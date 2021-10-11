a=input()
count=1
if abs(int(a))>9:
    num=0
    count=0
    while abs(int(a))>9 :
        for i in range(len(a)):
            if a[i] != '-':
                num+=int(a[i])
            else:
                num+=ord(a[i])-ord('0')

        a=str(num)
        num=0
        count+=1
print(count)
