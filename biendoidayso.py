check_end=0
while check_end==0:
	n=4
	a = list(map(int,input().strip().split()))[:n]
	if a[0]==0 and a[1]==0 and a[2]==0 and a[3]==0:
		check_end=1
	else:
		count = 0
		check = 0
		b=[]
		for i in range(n):
			b.append(a[i])
		while check==0:
			if a[0] == a[1] and a[1] == a[2] and a[2] == a[3]:
				break
			a[0] = abs(a[0] - b[1])
			a[1] = abs(a[1] - b[2])
			a[2] = abs(a[2] - b[3])
			a[3] = abs(a[3] - b[0])
			count += 1
			if a[0] == a[1] and a[1] == a[2] and a[2] == a[3]:
				break
			b.clear()
			for i in range(n):
				b.append(a[i])
		print(count)
