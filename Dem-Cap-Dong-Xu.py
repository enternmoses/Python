n=int(input())
a=[]
for i in range(n):
    arr=input()
    a.append(arr)
count=0
count_1=0
for i in range(n):
    for j in range(n):
        for k in range(j+1,n):
            if a[i][j]=='C':
                if a[i][j]==a[i][k]:
                    count+=1
            if a[j][i]=='C':
                if a[j][i]==a[k][i]:
                    count+=1

print(count)