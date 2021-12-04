n = int(input())
guess_all = [str(i) for i in range(1,n+1)]
g = list(map(str, input().split()))

while g[0] != 'HELP':
    ans = input()
    if ans == 'YES':
        for t in guess_all:
            if t not in g:
                guess_all.remove(t)
                for t in guess_all:
                    if t not in g:
                        guess_all.remove(t)

    elif ans == 'NO':
        for t in guess_all:
            if t in g:
                guess_all.remove(t)
    g = list(map(str, input().split()))
print(*guess_all)
        