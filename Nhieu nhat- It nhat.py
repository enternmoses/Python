import math
def sum(list,a,b):
    sum_l=0
    for i in range(a,b):
        sum_l+=list[i]
    return sum_l

t = int(input())
while t>0:
    [n,p]=[(x) for x in input().split()]
    a = list(map(int, input().strip().split()))[:n]
    a.sort()
    sum_a=0
    j=0
    for i in range(n):
        if sum(a,i,j)>
    t-=1
