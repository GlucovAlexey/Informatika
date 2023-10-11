a = float(input())
k = a
t = 1
flag = True
for i in range(14):
	a = float(input())
	if not(a>k) and flag:
		t = i+2
		flag = False
	k = a
if t==1:
   pint("OK")
else:
   print("Not OK:", t)