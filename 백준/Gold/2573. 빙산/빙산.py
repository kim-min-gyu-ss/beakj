from collections import deque
di = [-1,1,0,0]
dj = [0,0,-1,1]
def bfs():
    global cnt
    while True:
        cnt += 1
        result = 0
        visited = [[False for _ in range(M)] for _ in range(N)]
        bing2 = [[0 for _ in range(M)]for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if bing[i][j]:
                    tmp = 0
                    for k in range(4):
                        new_i = i + di[k]
                        new_j = j + dj[k]
                        if not bing[new_i][new_j]:
                            tmp += 1
                    bing2[i][j] = tmp
        for l in range(N):
            for m in range(M):
                bing[l][m] -= bing2[l][m]
                if bing[l][m] <= 0:
                    bing[l][m] = 0
        for i in range(N):
            for j in range(M):
                if bing[i][j] and not visited[i][j]:
                    q = deque([[i, j]])
                    while q:
                        y, x = q.popleft()
                        for k in range(4):
                            new_y = y + di[k]
                            new_x = x + dj[k]
                            if bing[new_y][new_x] and not visited[new_y][new_x]:
                                visited[new_y][new_x] = True
                                q.append([new_y, new_x])
                    result += 1
        if result > 1:
            return cnt
        elif not result:
            cnt = 0
            return cnt


N, M = map(int,input().split())
bing = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
bfs()
print(cnt)