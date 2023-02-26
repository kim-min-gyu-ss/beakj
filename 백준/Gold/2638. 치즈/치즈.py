from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def air(i,j):
    q = deque([[i, j]])
    while q:
        y, x = q.popleft()
        if visited[y][x]:
            continue
        visited[y][x] = True

        for k in range(4):
            new_y = y + di[k]
            new_x = x + dj[k]
            if 0 <= new_y < N and 0 <= new_x < M and not visited[new_y][new_x] and not cheese[new_y][new_x]:
                cheese[new_y][new_x] = 2
                q.append([new_y, new_x])

def melt(i,j):
    tmp = 0
    if cheese[i][j] == 1:
        for k in range(4):
            new_y = i + di[k]
            new_x = j + dj[k]
            if cheese[new_y][new_x] == 2:
                tmp += 1
        if tmp >= 2:
            result.append([i,j])

N, M = map(int, input().split())
cheese = []
for _ in range(N):
    cheese.append(list(map(int, input().split())))
visited = [[False for _ in range(M)] for _ in range(N)]
air(0,0)

final = 0
while True:
    result = []
    for i in range(N):
        for j in range(M):
            melt(i,j)
    if result:
        final += 1
        for k in result:
            cheese[k[0]][k[1]] = 2
            air(k[0],k[1])
    else:
        break

print(final)