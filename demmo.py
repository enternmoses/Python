mod = 1e9+7
def sum(n,k):
    if k == 0:
        return 1
    if k == 1:
        return n
    elif k%2 == 0:
        return ((sum(n, k / 2)%mod) * (sum(n, k / 2)%mod))%mod
    elif k%2 != 0:
        return (n * (sum(n, k - 1) % mod)) % mod

while 1:
    [n,k] = (int(x) for x in input().split())
    if n==k and n==0:
        break
    else:
        re = int(sum(n,k))
        print(re)

