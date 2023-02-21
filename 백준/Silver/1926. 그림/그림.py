from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
N ,M = map(int,input().split())
picture = []
for _ in range(N):
    picture.append(list(map(int,input().split())))
visited = [[False for _ in range(M)] for _ in range(N)]
result = []
for i in range(N):
    for j in range(M):
        if picture[i][j] == 1:
            queue = deque([[i, j]])
            cnt = 0
            while queue:
                y, x = queue.popleft()
                if visited[y][x]:
                    continue
                visited[y][x] = True
                cnt += 1
                for k in range(4):
                    new_y = y + di[k]
                    new_x = x + dj[k]
                    if 0 <= new_x < M and 0 <= new_y < N and not visited[new_y][new_x] and picture[new_y][new_x] == 1:
                        queue.append([new_y,new_x])
            if cnt > 0:
                result.append(cnt)
print(len(result))
if len(result) == 0:
    print(0)
else:
    print(max(result))