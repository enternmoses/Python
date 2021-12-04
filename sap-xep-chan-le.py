n = int(input())
c = []
l = []
base = []
while n>0:
    data=input()
    base+=data.split()
    n-=len(data.split())
    # data.removeprefix(data)
    # print(n)
# print(base)
for i in base:
    i=int(i)
    if(int(i)%2==0):
        c.append(i)
    else:
        l.append(i)
c.sort()
l.sort(reverse=True)
i,j=0,0
for k in base:
    k = int(k)
    if (k % 2 == 0):
        print(c[i],end=' ')
        i+=1
    else:
        print(l[j],end=' ')
        j+=1