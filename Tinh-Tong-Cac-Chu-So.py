t=int(input())
while t:
    s=input()
    sum=0
    a=''
    for i in range(len(s)):
        if s[i]>='0' and s[i]<='9':
            sum+=int(s[i])
        else:
            a+=s[i]
    print(''.join(sorted(a)),end='')
    print(sum)

    t-=1
