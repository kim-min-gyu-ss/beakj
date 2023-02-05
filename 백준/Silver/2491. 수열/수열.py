# 2491
a = int(input())
num_list = list(map(int, input().split()))
count = 0
result = [0]
for i in range(1, len(num_list)):
    if num_list[i - 1] <= num_list[i]:
        count += 1
    else:
        result.append(count)
        count = 0
    if i == len(num_list) - 1:
        result.append(count)
count = 0
for j in range(1, len(num_list)):
    if num_list[j - 1] >= num_list[j]:
        count += 1
    else:
        result.append(count)
        count = 0
    if i == len(num_list) - 1:
        result.append(count)
print(max(result) + 1)
