a = int(input())
b = []
for i in range(6):
    k = list(map(int,input().split()))
    b.append(k[-1])
c = []   # 홀
d = []   # 짝
for i in range(6):
    if i % 2 == 0:
        c.append(b[i])
    else:
        d.append(b[i])
mx_2 = c.index(max(c))  # 홀
mx_1 = d.index(max(d))  # 짝
max_result = 0
min_result = 0
if mx_1 == 1 == mx_2:
    max_result = max(c) * max(d)
    min_result = c[0] * d[-1]
elif mx_1 == 2 == mx_2:
    max_result = max(c) * max(d)
    min_result = d[0] * c[1]
elif mx_1 == 0 == mx_2:
    max_result = max(c) * max(d)
    min_result = c[-1] * d[1]
elif mx_1 == 2 and mx_2 == 0:
    max_result = max(c) * max(d)
    min_result = c[1] * d[1]
elif mx_1 == 0 and mx_2 == 1:
    max_result = max(c) * max(d)
    min_result = c[-1] * d[-1]
elif mx_1 == 1 and mx_2 == 2:
    max_result = max(c) * max(d)
    min_result = c[0] * d[0]
final = (max_result - min_result) * a
print(final)