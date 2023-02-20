from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
N, M = map(int, input().split())
miro = []
visited = [[False for _ in range(M)] for _ in range(N)]
for _ in range(N):
    miro.append(list(map(int, input())))
# print(miro)
# print(visited)
queue = deque([[0, 0, 1]])

result = 0
while queue:
    y, x, cnt = queue.popleft()
    if y == N-1 and x == M-1:
        result = cnt
    if visited[y][x] == True:
        continue
    visited[y][x] = True
    for i in range(4):
        new_y = y + di[i]
        new_x = x + dj[i]
        if 0 <= new_y < N and 0 <= new_x < M and not visited[new_y][new_x] and miro[new_y][new_x] == 1:
            queue.append([new_y, new_x, cnt + 1])
print(result)