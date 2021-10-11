def ThuanNghich(n):
    n=str(n)
    s=n[::-1]
    if n==s:
        return True
    else:
        return False

def ChiaHet2(n):
    if len(n)%2!=0:
        return False
    for i in range (0, len(n)):
        if int(n[i])%2!=0:
            return False
    return True

t=int(input())
for _ in range(t):
    n=int(input())
    s=""
    for i in range (22,n,22):
        if ThuanNghich(i) and ChiaHet2(str(i)):
            s=s+str(i)+" "
    print(s)
