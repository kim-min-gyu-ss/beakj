from collections import deque

dk = [-1, 1, 0, 0, 0, 0]
di = [0, 0, -1, 1, 0, 0]
dj = [0, 0, 0, 0, -1, 1]


def bfs(k, i, j, cnt):
    global result
    q = deque([[k, i, j, cnt]])

    while q:
        z, y, x, cnt = q.popleft()
        if building[z][y][x] == 'E':
            result = cnt
            break
        if visited[z][y][x]:
            continue
        visited[z][y][x] = True
        for l in range(6):
            new_z = z + dk[l]
            new_y = y + di[l]
            new_x = x + dj[l]
            if 0 <= new_z < L and 0 <= new_y < R and 0 <= new_x < C and not visited[new_z][new_y][new_x] and \
                    (building[new_z][new_y][new_x] == '.' or building[new_z][new_y][new_x] == 'E'):
                q.append([new_z, new_y, new_x, cnt + 1])

while True:
    L, R, C = map(int, input().split())
    if not L and not R and not C:
        break
    building = [[] for _ in range(L)]
    for i in range(L):
        for _ in range(R):
            building[i].append(list(map(str, input())))
        a = input()
    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]
    result = 0
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == 'S':
                    bfs(i, j, k, 0)
    if result:
        print(f'Escaped in {result} minute(s).')
    else:
        print(f'Trapped!')