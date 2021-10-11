import re
a=input()
b = re.findall(r'\d+', a)
if(int(b[0])+int(b[1])==int(b[2])):
    print("YES")
else:
    print("NO")
