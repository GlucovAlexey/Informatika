a = int(input())
k = a
t = 1
flag = True
for i in range(14):
	a = int(input())
	if not(a>k) and flag:
		t = i+2
		flag = False
	k = a
print(t)