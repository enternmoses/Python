def ThuanNghich(n):
    n=str(n)
    s=n[::-1]
    if n==s:
        return True
    else:
        return False

def chan(n):
    if(n%2==0): return True
    else: return False

def chu_so_chan(n):
    while n>0:
        a=n%10
        if chan(a)==False:
            return False
        n//=10
    return True
if __name__ == '__main__':
    t=int(input())
    while t>0:
        n=int(input())
        for i in range(22,n):
            if ThuanNghich(i) and chan(len(str(i))) and chu_so_chan(i):
                print(i,end=" ")
        print()
        t-=1