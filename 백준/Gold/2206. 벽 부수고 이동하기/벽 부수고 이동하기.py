from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
N, M = map(int, input().split())
buyk = []
for _ in range(N):
    buyk.append(list(map(int, input())))
visited = [[False for _ in range(M)] for _ in range(N)]
visited_2 = [[False for _ in range(M)] for _ in range(N)]

c = False
q = deque([[0, 0, 1, True]])
while q:
    y, x, cnt, state = q.popleft()
    if y == N - 1 and x == M - 1:
        c = True
        result = cnt
        break
    if state:
        if visited[y][x]:
            continue
        visited[y][x] = True
    else:
        if visited_2[y][x]:
            continue
        visited_2[y][x] = True
    for k in range(4):
        new_y = y + di[k]
        new_x = x + dj[k]
        if state:
            if 0 <= new_y < N and 0 <= new_x < M and not visited[new_y][new_x] and buyk[new_y][new_x] == 1:
                q.append([new_y,new_x,cnt +1, False])
        if not state:
            if 0 <= new_y < N and 0 <= new_x < M and not visited_2[new_y][new_x] and buyk[new_y][new_x] == 0:
                q.append([new_y,new_x,cnt + 1, state])
                continue
        if 0 <= new_y < N and 0 <= new_x < M and not visited[new_y][new_x] and buyk[new_y][new_x] == 0:
            q.append([new_y, new_x, cnt + 1, state])

# print(buyk)
if c:
    print(result)
else:
    print(-1)