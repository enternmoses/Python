p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
check=1
while check:
    t=input()
    if(t=='0'):
        break
    t = t.split()
    k=int(t[0])
    if(k==0):
        break
    s=t[1]
    n=len(s)
    a=[]
    b=[]
    for i in range(n):
        result=(p.index(s[i])+k)%26
        a.append(p[result])
    a.reverse()
    for i in range(n):
        print(a[i],end='')
    print("\n")
    a.clear()
    t.clear()