a = float(input())
k = a
S = 1
while a != 0:
	if a != k:
		S+=1
	k = a
	a = float(input())
print(S)