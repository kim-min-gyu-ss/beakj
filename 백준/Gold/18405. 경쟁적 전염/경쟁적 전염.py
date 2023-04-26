from collections import deque

di = [-1,1,0,0]
dj = [0,0,-1,1]

def check():
    visited = [[False for _ in range(N)] for _ in range(N)]
    tmp = []

    for i in range(N):
        for j in range(N):
            if virus[i][j]:
                tmp.append([virus[i][j],0,i,j,])
                visited[i][j] = True
    tmp = sorted(tmp, key=lambda x : x[0])
    q = deque(tmp)

    while q:
        num, cnt, y, x = q.popleft()
        if cnt == S:
            break
        for k in range(4):
            new_y = y + di[k]
            new_x = x + dj[k]
            if 0 <= new_y < N and 0 <= new_x < N and not visited[new_y][new_x] and not virus[new_y][new_x]:
                visited[new_y][new_x] = True
                virus[new_y][new_x] = num
                q.append([num, cnt + 1, new_y, new_x])

N, K = map(int,input().split())
virus = [list(map(int,input().split())) for _ in range(N)]
S, Y, X = map(int,input().split())
check()
print(virus[Y-1][X-1])