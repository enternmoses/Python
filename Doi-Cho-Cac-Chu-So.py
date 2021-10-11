t=int(input())
while t:
    n=list(input())
    a=[]
    b=[]
    check=0
    n.reverse()
    for i in range(len(n)):
        if i<len(n)-1:
            if n[i]<n[i+1]:
                for j in range(0,i+1):
                    a.append(n[j])
                    b.append(j)
                a.sort(reverse=True)

                for j in range(len(a)):
                    if int(n[i+1])>int(a[j]):
                        for k in range(len(b)):
                            if(n[b[k]]==a[j]):
                                if(k<len(b)-1):
                                    if(n[b[k]]==n[b[k+1]]):
                                        continue
                                    else:
                                        temp=n[i+1]
                                        n[i+1]=n[b[k]]
                                        n[b[k]]=temp
                                        check=1
                                        break
                                else:
                                    temp = n[i + 1]
                                    n[i + 1] = n[b[k]]
                                    n[b[k]] = temp
                                    check = 1
                                    break
                        if check==1:
                            break
                if check == 1:
                    break
    n=''.join(n)
    n=n[::-1]
    if check==1 and n[0]!='0':
        print(int(n))
    else:
        print("-1")
    t-=1
