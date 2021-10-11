def solve():
    a = input()
    b = len(a)
    if b == 1:
        print('1' + a)
    else:
        st = ''
        count = 1
        ex = a[0]
        for x1 in range(1, b):
            if a[x1] == ex:
                count += 1
            else:
                ex = a[x1]
                st += str(count)
                st += (str(a[x1 - 1]))
                count = 1
        st += str(count)
        st += (str(a[x1]))
        print(st)

t=int(input())
while t>0:
    solve()
    print('\n')
    t-=1