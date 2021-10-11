t=int(input())
while t:
    n=int(input())
    check = []
    a = []
    for i in range(1004):
        check.append(0)
    for i in range(n):
        x = int(input())
        a.append(x)
        check[a[i]] += 1
    a.sort()
    k = max(check)
    for i in range(n):
        if check[a[i]]==k:
            print(a[i])
            break
    t-=1
