s1 = int(input())
num = 0
while s1>0:
    b=s1%1000
    i=0
    a=0
    while b>0:
        a+=b%10*int(pow(2,i))
        i+=1
        b//=10
    num=num*10+a
    s1//=1000
num=str(num)
print(num[::-1])

