def solve(a,count,sum):
    a = a + sum
    if (a > 25):
        count = int(a / 26)
        a = int(a - count * 26)
    return a

k=int(input())
while k>0:
    t=list(input())
    n=int(len(t))
    sum_first=0
    sum_second=0
    count_1=0
    count_2=0
    # lay nua chuoi dau
    for i in range(int(n/2)):
        t[i]=ord(t[i])
        t[i]-=65
        sum_first+=t[i]
    #lay nua chuoi sau
    for i in range(int(n/2),n):
        t[i]=ord(t[i])
        t[i]-=65
        sum_second+=t[i]
    #Rotate
    for i in range(n):
        if(i<int(n/2)):
            t[i] = solve(t[i],count_1,sum_first)
        else:
            t[i] = solve(t[i], count_2, sum_second)
    #Merge
    for i in range(n):
        if i<int(n/2):
            t[i]=t[i]+t[int(n/2)+i]
            if (t[i]>25):
                t[i]-=26
    #Output
    for i in range(int(n/2)):
        t[i]+=65
        print(chr(t[i]),end='')
    print("\n")
    k-=1
