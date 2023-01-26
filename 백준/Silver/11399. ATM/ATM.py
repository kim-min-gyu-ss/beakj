a = int(input())
result = list(map(int,input().split()))
result = sorted(result)
fin_sum = 0
fin_result = []
for i in range(a):
    fin_sum += result[i]
    fin_result.append(fin_sum)
print(sum(fin_result))