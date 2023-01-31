a = list(map(int,input()))
count_1 = 0
count_0 = 0
if a[0] == 1:
    count_1 += 1
else:
    count_0 += 1

for j in range(1,len(a)):
    if a[j-1] == 0:
        if a[j-1] != a[j]:
            count_1 += 1
    elif a[j-1] == 1:
        if a[j-1] != a[j]:
            count_0 += 1

if count_0 > count_1:
    print(count_1)
else:
    print(count_0)