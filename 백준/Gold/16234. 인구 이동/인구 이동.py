from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs():
    visited = [[False for _ in range(N)] for _ in range(N)]
    s = f = False
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            tmp = [ingoo[i][j]]
            idx = [[i,j]]
            q = deque([[i,j]])
            while q:
                y,x = q.popleft()
                visited[y][x] = True
                for k in range(4):
                    new_y = y + di[k]
                    new_x = x + dj[k]
                    if 0 <= new_y < N and 0 <= new_x < N and not visited[new_y][new_x] and L <= abs(ingoo[new_y][new_x] - ingoo[y][x]) <= R:
                        tmp.append(ingoo[new_y][new_x])
                        idx.append([new_y,new_x])
                        q.append([new_y,new_x])
                        visited[new_y][new_x] = True
            hap = sum(tmp)
            na = len(idx)
            while idx:
                y,x = idx.pop()
                if ingoo[y][x] != hap//na:
                    f = True
                ingoo[y][x] = hap//na
    if f:
        return True
    else:
        return False


N, L, R = map(int, input().split())
ingoo = [list(map(int, input().split())) for _ in range(N)]
result = 0
while 1:
    aa = bfs()
    if not aa:
        break
    result += 1
print(result)