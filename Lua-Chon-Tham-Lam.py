def Convert(string):
    list1=[]
    list1[:0]=string
    return list1
t=int(input())
while t>0:
    a=input()
    l=Convert(a)
    l.reverse()
    for i in range(len(l)):
        if i < len(l) -1:
            if int(l[i]) >= 5:
                for k in range(0, i + 1):
                    l[k] = 0
                l[i+1] = int(l[i+1]) +1
            elif i != len(l)-1:
                for k in range(0,i+1):
                    l[k] = 0
    l.reverse()
    str_int = [str(int) for int in l]
    print(''.join(str_int))
    t-=1