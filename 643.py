a = 1
S = 1
p = 1
a = float(input())
k = a
S = 2#колворазных чисел
T = 0#колво первых повт
flag = True
while a != 1000:
    if k != a:
        S += 1
        flag = False
    if flag:
        T+=1
    k = a
    a = float(input())
print(T, S)
