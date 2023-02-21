from collections import deque
import pprint
di = [-1, 1, 0, 0, 0, 0]
dj = [0, 0, -1, 1, 0, 0]
dk = [0, 0, 0, 0, 1, -1]
M, N, H = map(int, input().split())
tomato = [[] for _ in range(H)]
for t in range(H):
    for _ in range(N):
        tomato[t].append(list(map(int, input().split())))

# pprint.pprint(tomato)
visited = [[[False for _ in range(M)] for _ in range(N)]for _ in range(H)]
# pprint.pprint(visited)

# cnt = 0
queue = deque([])
for l in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[l][i][j] == 1:
                queue.append([l, i, j, 1])
result = []
while queue:
    z, y, x, cnt = queue.popleft()
    if visited[z][y][x]:
        continue
    visited[z][y][x] = True

    for k in range(6):
        new_y = y + di[k]
        new_x = x + dj[k]
        new_z = z + dk[k]
        if 0 <= new_x < M and 0 <= new_y < N and 0 <= new_z < H and not visited[new_z][new_y][new_x] and tomato[new_z][new_y][new_x] == 0:
            queue.append([new_z, new_y, new_x, cnt + 1])
            tomato[new_z][new_y][new_x] = 1
            result.append(cnt)
for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[k][i][j] == 0:
                result = [-1]
                break
# print(tomato)
if not result:
    print(0)
else:
    print(max(result))