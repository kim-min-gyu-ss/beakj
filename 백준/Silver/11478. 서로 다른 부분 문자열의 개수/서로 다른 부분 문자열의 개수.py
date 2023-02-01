a = input()
b = len(a)
result = []
count = 1
while count < len(a) + 1:
    for i in range(b):
        result.append(a[i:i+count])
    b -= 1
    count += 1
result = set(result)
print(len(result))