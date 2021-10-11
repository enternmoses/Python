def convert_number(n, b):
    sb = ""
    m = 0
    remainder = n
    while (remainder > 0):
        if (b > 10):
            m = remainder % b
            if (m >= 10):
                sb = sb + str(chr(55 + m))
            else:
                sb = sb + str(m)
        else:
            sb = sb + str(remainder % b)
        remainder = int(remainder / b)
    return "".join(reversed(sb))
t=int(input())
while t:
    [n,b]=[int (x) for x in input().split()]
    print(convert_number(n,b))
    t-=1