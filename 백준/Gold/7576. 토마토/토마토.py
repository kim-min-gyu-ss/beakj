from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
M ,N = map(int,input().split())
tomato = []
for _ in range(N):
    tomato.append(list(map(int,input().split())))
visited = [[False for _ in range(M)] for _ in range(N)]

# cnt = 0
queue = deque([])
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i, j,1])
result = []
while queue:
    y, x ,cnt = queue.popleft()
    if visited[y][x]:
        continue
    visited[y][x] = True

    for k in range(4):
        new_y = y + di[k]
        new_x = x + dj[k]
        if 0 <= new_x < M and 0 <= new_y < N and not visited[new_y][new_x] and tomato[new_y][new_x] == 0:
            queue.append([new_y,new_x, cnt+1])
            tomato[new_y][new_x] = 1
            result.append(cnt)
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            result = [-1]
            break
# print(tomato)
if not result:
    print(0)
else:
    print(max(result))