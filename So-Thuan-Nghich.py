def ThuanNghich(n):
    s=n[::-1]
    if n==s:
        return True
    else:
        return False
def convert_number(n, b):
    sb = ""
    remainder = n
    while (remainder > 0):
        sb = sb + str(remainder % b)
        remainder = int(remainder / b)
    return sb

[a,b,m]=[int (x) for x in input().split()]
count=0
k=2
check={}
for i in range(a, b + 1):
    check[i]=0
while k<=m:
    for i in range (a,b+1):
        if check[i]==0:
            if ThuanNghich(convert_number(i,k))==False:
                check[i]=1
    k+=1
for i in range (a,b+1):
    if(check[i]==0):
        count+=1
print(count)