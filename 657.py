n = float(input())

a = float(input())
b = a
flag = True

l = 1
k = a
for i in range(0, 7):
	a = float(input())
	if ((a - n) > 0) and flag:
		if abs(b-n) < abs(a-n):
			k = b
			l = i+1
		else:
			k = a
			l = i+2
		flag = False
	b = a
print(k," ",  l)
