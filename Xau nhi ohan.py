[p,n]=[(x) for x in input().split()]
n=int(n)
x = n * [65]
# count=0
# print(x)
# def finall(x):
#     for i in x:
#         if i != ord(p):
#             return True
#     return False
def check(x):
    for i in range(n):
        if i<n-1:
            if x[i]>x[i+1]:
                return False
    return True
def fine_print(x):
    tmp = ''
    for i in x:
        tmp += str(chr(i))
    return tmp


def bin_gen(i):
    for j in range(65, ord(p)+1):
        x[i] = j
        if i == n - 1:
            if check(x):
                print(fine_print(x))
        else:
            bin_gen(i + 1)


bin_gen(0)
