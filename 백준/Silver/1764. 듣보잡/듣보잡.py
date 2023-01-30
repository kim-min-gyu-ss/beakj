a, b = map(int,input().split())
result = {}
for i in range(a+b):
    c = input()
    result.setdefault(c,0)
    result[c] += 1
count = 0
final = []
for j, k  in result.items():
    if k >= 2:
        count += 1
        final.append(j)
final = sorted(final)
print(count)
for l in final:
    print(l, end = ' ')