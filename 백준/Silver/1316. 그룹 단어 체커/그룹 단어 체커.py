a = int(input())
result = []
for i in range(a):
    result.append(input())
count = 0
for i in result:
    num = 1
    for j in range(1,len(i)):
        if i[j] != i[j-1]:
            num += 1
    if len(set(i)) == num:
        count += 1
print(count)