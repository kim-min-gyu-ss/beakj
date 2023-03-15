from collections import deque

di = [-1,1,0,0]
dj = [0,0,-1,1]

def bfs(i,j,num):
    visited = [[False for _ in range(C)] for _ in range(R)]
    q = deque([[i,j,num]])
    visited[i][j] = True
    result[i][j] += [0]
    while q:
        y,x,cnt = q.popleft()
        for k in range(4):
            new_y = y + di[k]
            new_x = x + dj[k]
            if 0 <= new_x < C and 0 <= new_y < R and not visited[new_y][new_x] and not miro[new_y][new_x]:
                visited[new_y][new_x] = True
                q.append([new_y,new_x,cnt+1])
                result[new_y][new_x] += [cnt+1]


R,C = map(int,input().split())
miro = [list(map(int,input())) for _ in range(R)]
nsc = [list(map(int,input().split())) for _ in range(3)]
result = [[[] for _ in range(C)] for _ in range(R)]
day = 10002
many = 1
s = False
for i in nsc:
    bfs(i[0]-1,i[1]-1,0)
for i in range(R):
    for j in range(C):
        if result[i][j]:
            if len(result[i][j]) == 3:
                s = True
            if max(result[i][j]) < day:
                day = max(result[i][j])
                many = 1
            elif max(result[i][j]) == day:
                many += 1
if not s:
    print(-1)
else:
    print(day)
    print(many)