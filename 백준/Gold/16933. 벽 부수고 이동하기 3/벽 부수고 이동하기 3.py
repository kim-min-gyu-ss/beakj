import sys
input = sys.stdin.readline
from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
N, M, K = map(int, input().split())
buyk = []
for _ in range(N):
    buyk.append(list(map(int, input().strip())))
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(K + 1)]

c = False
day = True
stack = 0
q = deque([[0, 0, 0, day, stack]])
for i in range(K + 1):
    visited[i][0][0] = 1
while q:
    z, y, x, s ,t= q.popleft()
    if y == N - 1 and x == M - 1:
        c = True
        result = visited[z][y][x]
        break

    for k in range(4):
        new_y = y + di[k]
        new_x = x + dj[k]
        if 0 <= new_y < N and 0 <= new_x < M and not visited[z][new_y][new_x]:
            if buyk[new_y][new_x] == 1 and z < K and not visited[z+1][new_y][new_x]:
                if s:
                    if t:
                        visited[z+1][new_y][new_x] = visited[z][y][x] + 2
                    else:
                        visited[z + 1][new_y][new_x] = visited[z][y][x] + 1
                    q.append([z + 1, new_y, new_x, False, 0])
                else:
                    q.append([z, y, x, True, t+1])
            elif buyk[new_y][new_x] == 0:
                if s:
                    q.append([z, new_y, new_x,False, 0])
                    visited[z][new_y][new_x] = visited[z][y][x] + 1
                else:
                    q.append([z, new_y, new_x,True, 0])
                    visited[z][new_y][new_x] = visited[z][y][x] + 1

if c:
    print(result)
else:
    print(-1)