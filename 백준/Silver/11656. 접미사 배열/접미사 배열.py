a = list(map(str,input()))
result = []
for i in range(len(a)):
    result.append(''.join(a))
    del a[0]
result1 = sorted(result)
for i in result1:
    print(i)