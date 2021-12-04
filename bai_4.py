def moreA(a,b):
    count_1 = 0
    count_2 = 0
    for idx,c in enumerate(a):
        if c=='a':
            count_1+=1
    for idx, c in enumerate(b):
        if c=='a':
            count_2+=1
    if count_1 == count_2:
        return
    elif count_1 > count_2:
        return a
    else:
        return b
a = input()
b = input()
print(moreA(a,b))