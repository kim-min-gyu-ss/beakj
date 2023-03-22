from collections import deque

di=[-1,1,0,0]
dj=[0,0,-1,1]

def bfs():
    result = 0
    q = deque([[0,0,0,False]])
    visited[0][0][0] = True
    while q:
        y,x,cnt,kal = q.popleft()
        if y == N-1 and x == M-1:
            result = cnt
            break
        for k in range(4):
            new_y = y + di[k]
            new_x = x + dj[k]
            if not kal:
                if 0 <= new_y < N and 0 <= new_x < M and not visited[0][new_y][new_x]:
                    if sung[new_y][new_x] == 2:
                        visited[0][new_y][new_x] = True
                        visited[1][new_y][new_x] = True
                        q.append([new_y,new_x,cnt+1,True])
                    elif not sung[new_y][new_x]:
                        visited[0][new_y][new_x] = True
                        q.append([new_y, new_x, cnt + 1, False])
            else:
                if 0 <= new_y < N and 0 <= new_x < M and not visited[1][new_y][new_x]:
                    visited[1][new_y][new_x] = True
                    q.append([new_y, new_x, cnt + 1, True])
    return result

N,M,T = map(int,input().split())
sung = [list(map(int,input().split()))for _ in range(N)]
visited = [[[False for _ in range(M)]for _ in range(N)] for _ in range(2)]
a = bfs()
if a > T or not a:
    print('Fail')
else:
    print(a)