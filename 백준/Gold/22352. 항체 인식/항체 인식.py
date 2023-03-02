from collections import deque
di = [-1,1,0,0]
dj = [0,0,-1,1]

def bac(i,j):

    q = deque([[i,j]])
    now = before[i][j]
    new = after[i][j]
    while q:
        y,x = q.popleft()
        # if visited[y][x]:
        #     continue
        # visited[y][x] = True
        if before[y][x] != now:
            continue
        before[y][x] = new
        for k in range(4):
            new_y = y + di[k]
            new_x = x + dj[k]
            if 0 <= new_x < M and 0 <= new_y < N and before[new_y][new_x] == now:
                q.append([new_y,new_x])


N, M = map(int,input().split())
before = [list(map(int,input().split())) for _ in range(N)]
after = [list(map(int,input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if before[i][j] != after[i][j] and not visited[i][j]:
            bac(i,j)
            cnt += 1

#
# print(before)
# print(after)
state = True
if cnt <= 1:
    for k in range(N):
        for l in range(M):
            if before[k][l] != after[k][l]:
                print('NO')
                state = False
                break
        if not state:
            break
    else:
        print('YES')
else:
    print('NO')
