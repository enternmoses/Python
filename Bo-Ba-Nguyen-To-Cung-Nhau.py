def uscln(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b


[l,r]=[int (x) for x in input().split()]
for i in range(l,r+1):
   for j in range(i+1,r+1):
       if uscln(i, j) == 1:
           for k in range(j+1,r+1):
               if uscln(i,k)==1 and uscln(j,k)==1:
                   print('(',i,',',' ',j,',',' ',k,')',sep='')