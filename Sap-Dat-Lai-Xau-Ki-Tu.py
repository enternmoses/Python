t = int(input())
for k in range (t):
    s1 = [item for item in input()]
    s2 = [item for item in input()]
    if len(s1) != len(s2):
        print("Test ",k+1,":",' NO',sep="")
    else:
        check=[]
        test=0
        s1.sort()
        s2.sort()
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                print("Test ",k+1,":",' NO',sep="")
                test=1
                break
        if test==0:
            print("Test ",k+1,":",' YES',sep="")
    t-=1
