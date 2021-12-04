def prod(n):
    s=1
    while(n>0):
        s*=n%10
        n//=10
    return s
def swap(list,a,b):
    tmp = list[a]
    list[a] = list[b]
    list[b] = tmp
    return list

t=int(input())
while t>0:
    n=int(input())
    a = list(map(int, input().strip().split()))[:n]
    b=[]
    for i in range(n):
        b.append(prod(a[i]))

    for i in range(n-1):
        for j in range(i+1,n):
            if(b[i]>b[j]):
                swap(a,i,j)
                swap(b,i,j)
            if(b[i]==b[j]):
                if a[i]>a[j]:
                    swap(a, i, j)
                    swap(b, i, j)
    str_int= [str(int) for int in a]
    print(' '.join(str_int))
    t-=1
