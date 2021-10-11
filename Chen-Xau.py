
lst2 = []
lst2 = [item for item in input().split()]
s=input()
k=int(input())
k-=1
for i in range(len(lst2)):
    if i==k:
        print(s,end='')
        print(lst2[i],end=" ")
    else:
        print(lst2[i], end=" ")
