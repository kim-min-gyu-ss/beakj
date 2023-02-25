T = int(input())
num_list = list(map(int, input().split()))
q = num_list[0]
visited = [False for _ in range(200000)]
bumo = [0] * 200000
tmp = 0
cnt = 0
for i in range(len(num_list)):
    if visited[num_list[i]]:
        tmp = num_list[i]
        continue
    if i == 0:
        visited[num_list[i]] = True
        tmp = num_list[i]
        cnt += 1
        continue
    visited[num_list[i]] = True
    bumo[num_list[i]] = tmp
    tmp = num_list[i]
    cnt += 1

print(cnt)
for j in range(cnt):
    if j == q:
        print(-1, end=' ')
        continue
    if visited[j]:
        print(bumo[j], end=' ')