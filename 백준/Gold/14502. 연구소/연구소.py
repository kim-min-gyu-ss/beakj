from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(vrs):
    qq = z_cnt + s_cnt - 3
    visited = [[False for _ in range(M)] for _ in range(N)]
    vrs2 = vrs.copy()
    while vrs2:
        y,x = vrs2.popleft()
        if visited[y][x]:
            continue
        visited[y][x] = True
        qq -= 1
        for k in range(4):
            new_y = y + di[k]
            new_x = x + dj[k]
            if 0 <= new_x < M and 0 <= new_y < N and not visited[new_y][new_x] and not virus[new_y][new_x]:
                vrs2.append([new_y,new_x])
    # print(qq)
    return qq


N, M = map(int, input().split())
virus = [list(map(int, input().split())) for _ in range(N)]
zero = []
vrs = deque([])
z_cnt = 0
s_cnt = 0
result = 0
for i in range(N):
    for j in range(M):
        if not virus[i][j]:
            zero.append([i, j])
            z_cnt += 1
        elif virus[i][j] == 2:
            vrs.append([i, j])
            s_cnt += 1
for i in range(z_cnt - 2):
    for j in range(i + 1, z_cnt - 1):
        for k in range(j + 1, z_cnt):
            virus[zero[i][0]][zero[i][1]] = 1
            virus[zero[j][0]][zero[j][1]] = 1
            virus[zero[k][0]][zero[k][1]] = 1
            a = bfs(vrs)
            if a > result:
                result = a
            virus[zero[i][0]][zero[i][1]] = 0
            virus[zero[j][0]][zero[j][1]] = 0
            virus[zero[k][0]][zero[k][1]] = 0
print(result)