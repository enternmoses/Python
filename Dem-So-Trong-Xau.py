t=int(input())
while t>0:
    s=input()
    n=input()
    k=0
    i=0
    check=0
    count=0
    # print(s)
    # for i in range(len(s)):
    #     print(s[i],end='')
    while i<len(s):
        if i<len(s) and s[i]==n[k] and k<len(n):
            # print(i, k)
            k+=1
            i+=1
        if k==len(n):
            count+=1
            k=0
        if i<len(s) and s[i] != n[k] and k!=0:
            k=0
        if i<len(s) and s[i] != n[k] and k==0:
            i+=1

    print(count)
    t-=1