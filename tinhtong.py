t=input()
t=int(t)
while t:
	a=input()
	b=a[0]
	for e in a:
		if(b>e):
			print('NO')
			break
		else:
			b=e
	else:
		print('YES')
	t=t-1
