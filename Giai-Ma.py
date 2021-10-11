def solve():
    a=input()
    n=len(a)
    for i in range(n):
        if i%2!=0:
            count=int(a[i])
            for j in range(count):
                print(a[i-1],end='')

t=int(input())
while t>0:
    solve()
    print('\n')
    t-=1
