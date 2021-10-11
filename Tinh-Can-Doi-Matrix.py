n=int(input())
a=[]
for i in range(n):
    arr=list(map(int, input().split()))
    a.append(arr)
k=int(input())
sum_up, sum_down = 0, 0
for i in range (n):
    for j in range (n):
        if j<i:
            sum_down+=a[i][j]
        if j>i:
            sum_up += a[i][j]
if abs(sum_up - sum_down)<= k:
    print("YES")
else:
    print("NO")
print(abs(sum_up - sum_down))