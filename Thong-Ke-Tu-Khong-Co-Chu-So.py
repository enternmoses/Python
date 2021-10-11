import re
n=int(input())
string= ''
while n>0:
    a = input()
    string= string + a + " "
    n-=1
string=string.lower()
count = {}
string=re.sub(r"[^a-zA-Z0-9]"," ",string)
string=re.sub(r"[0-9]"," ",string)
string=sorted(string.split())
for i in string:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
sort_orders = sorted(count.items(), key=lambda x: x[1], reverse=True)
for i in sort_orders:
        print(i[0], i[1])