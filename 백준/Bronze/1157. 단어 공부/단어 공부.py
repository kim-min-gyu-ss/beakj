a = input()
a = a.lower()
result = dict()
for i in a:
    result.setdefault(i,0)
    result[i] += 1
result = sorted(result.items(), key= lambda x : x[1], reverse= True)
if len(result) == 1:
    print(result[0][0].upper())
elif result[0][1] == result[1][1]:
    print('?')
else:
    print(result[0][0].upper())