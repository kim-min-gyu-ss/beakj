import sys
input = sys.stdin.readline
a, b = map(int,input().split())
num_list = list(range(1, a + 1))
# print(num_list)
count = b - 1
result = []
for i in range(a):
    result.append(num_list.pop(count))
    if len(num_list) == 0:
        break
    count += b - 1
    while count >= len(num_list):
        count = count % len(num_list)
print('<', end='')
print(*result,sep=', ',end = '')
print('>')
