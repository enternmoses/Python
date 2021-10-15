test=10
count=0
a = {}
for i in range(43):
    a[i] = 0
while test>0:
    data=input()
    base=data.split()
    test-=len(base)
    for i in base:
        i=int(i)
        if a[i%42]==0:
            count+=1
            a[i % 42] = 1
print(count)