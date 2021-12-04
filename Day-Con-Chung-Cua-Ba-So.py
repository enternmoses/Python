t = int(input())
while t>0:
    [n,m,k]=[int(i) for i in input().split()]
    a = list(map(int, input().strip().split()))[:n]
    b = list(map(int, input().strip().split()))[:m]
    c = list(map(int, input().strip().split()))[:k]
    d = []
    check,i,j,l=0,0,0,0
    num=min(n,m,k)
    while i<n and j<m and l<k:
        if a[i] == b[j] == c[l]:
            print(a[i],end=' ')
            check =1
            i+=1
            j+=1
            l+=1
        elif a[i] < b[j]: i+=1
        elif b[j] < c[l]: j+=1
        else: l +=1
    if check == 0:
        print('NO')
    print()
    t-=1