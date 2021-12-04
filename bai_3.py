def mySort(n):
    for i in range(len(n)-1):
        for j in range(i+1,len(n)):
            if n[i] > n[j]:
                tmp = n[i]
                n[i] = n[j]
                n[j] = tmp
    return n

n=int(input())
a = list(map(int,input().strip().split()))[:n]
print(mySort(a))