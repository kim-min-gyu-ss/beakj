from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs2(i, j, num):
    buyk[i][j] = num
    cnt = 1
    q = deque([[i, j]])
    while q:
        y, x = q.popleft()
        for k in range(4):
            new_y = y + di[k]
            new_x = x + dj[k]
            if 0 <= new_x < M and 0 <= new_y < N and not buyk[new_y][new_x]:
                cnt += 1
                buyk[new_y][new_x] = num
                q.append([new_y, new_x])
    return cnt

N, M = map(int, input().split())
buyk = [list(map(int, input())) for _ in range(N)]
ans = [[0 for _ in range(M)] for _ in range(N)]
number = dict()
tmp = 2
for i in range(N):
    for j in range(M):
        if not buyk[i][j]:
            number.setdefault(tmp, 0)
            number[tmp] = bfs2(i, j, tmp)
            tmp += 1

for i in range(N):
    for j in range(M):
        s = set()
        p = 1
        if buyk[i][j] > 1:
            ans[i][j] = 0
        else:
            for k in range(4):
                new_i = i + di[k]
                new_j = j + dj[k]
                if 0 <= new_j < M and 0 <= new_i < N and buyk[new_i][new_j] not in s and buyk[new_i][new_j] != 1:
                    s.add(buyk[new_i][new_j])
            for l in s:
                p += number[l]
            ans[i][j] = p % 10

for i in ans:
    print(*i, sep='')