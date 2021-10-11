def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)


[a,b]=[int (x) for x in input().split()]
count=0
for i in range(int(pow(10,b-1)),int(pow(10,b))):
    if uscln(a,i)==1:
        print(i,end=" ")
        count+=1
        if(count%10==0):
            print()


