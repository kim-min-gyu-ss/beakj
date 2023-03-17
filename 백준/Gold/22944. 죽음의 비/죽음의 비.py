from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(z, i, j, num, um, result):
    global u
    q = deque([[z, i, j, num, um, result]])
    result = -1
    while q:
        z, y, x, cnt, umb, final = q.popleft()
        if cnt == 0:
            continue
        if visited[z][y][x]:
            continue
        visited[z][y][x] = True
        for k in range(4):
            new_y = y + di[k]
            new_x = x + dj[k]
            if 0 <= new_x < N and 0 <= new_y < N and not visited[z][new_y][new_x]:
                if safe[new_y][new_x] == '.':
                    if umb:
                        q.append([z, new_y, new_x, cnt, umb-1, final + 1])
                    else:
                        q.append([z, new_y, new_x, cnt-1, umb, final + 1])
                elif safe[new_y][new_x] == 'U' and z < u and not visited[z+1][new_y][new_x]:
                    q.append([z + 1, new_y, new_x, cnt, D-1, final + 1])
                elif safe[new_y][new_x] == 'E':
                    result = final
                    return result
    return result

N, H, D = map(int, input().split())
safe = [list(map(str, input())) for _ in range(N)]
u = 0
a = []
s = []
for i in range(N):
    for j in range(N):
        if safe[i][j] == 'S':
            s.append([i, j])
        elif safe[i][j] == 'U':
            u += 1
visited = [[[False for _ in range(N)] for _ in range(N)] for _ in range(u + 1)]
rst = bfs(0, s[0][0], s[0][1], H, 0, 1)
print(rst)