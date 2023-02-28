from collections import deque

di = [-1,1,0,0]
dj = [0,0,-1,1]
def air(i,j):
    q = deque([[i,j]])
    while q:
        y, x = q.popleft()
        if visited_c[y][x]:
            continue
        visited_c[y][x] = True
        cheese[y][x] = 2
        for k in range(4):
            new_y = y + di[k]
            new_x = x + dj[k]
            if 0 <= new_y <sero and 0 <= new_x < garo and not visited_c[new_y][new_x] and not cheese[new_y][new_x]:
                q.append([new_y,new_x])


def melt(i,j):
    q = deque([[i,j]])
    y,x = q.popleft()
    for k in range(4):
        new_y = y + di[k]
        new_x = x + dj[k]
        if cheese[new_y][new_x] == 2:
            result.append([y,x])
            break


sero, garo = map(int,input().split())
cheese = [list(map(int,input().split())) for _ in range(sero)]
visited_c = [[False for _ in range(garo)] for _ in range(sero)]
cnt = 0
air(0,0)
tmp = 0
while True:
    result = []
    for i in range(sero):
        for j in range(garo):
            if cheese[i][j] == 1:
                melt(i,j)
    if result:
        cnt += 1
        for k in result:
            cheese[k[0]][k[1]] = 2
            air(k[0],k[1])
    else:
        break
    tmp = len(result)
# print(cheese)
print(cnt)
print(tmp)