a = int(input())
result = dict()
num_list = []
for i in range(a):
    num_list.append(input())
for j in num_list:
    count = 1
    for k in range(len(j)):
        result.setdefault(j[-(1+k)],0)
        result[j[-(1+k)]] += count
        count = count * 10
result = sorted(result.items(),key = lambda x : x[1], reverse= True)
count2 = 9
for i in result:
    for j in range(len(num_list)):
        num_list[j] = num_list[j].replace(i[0],str(count2))
    count2 -= 1
final = []
for i in num_list:
    final.append(int(i))
print(sum(final))
final