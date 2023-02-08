a = int(input())
dic = dict()
for _ in range(a):
    b = input()
    dic.setdefault(b, 0)
    dic[b] += 1
result = list(zip(dic.keys(),dic.values()))
result = sorted(result, key= lambda x : (-x[1], x[0]))
print(result[0][0])
