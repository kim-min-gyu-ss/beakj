from collections import deque

di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]


def shark(i, j):
    global result
    level = 2   # 레벨
    tmp = 0 # 레벨 상승위한 경험치
    y = i
    x = j

    while 1:
        cnt = 1
        visited = [[False for _ in range(N)] for _ in range(N)]
        distance = []
        q = deque([[y, x, cnt, level]])
        visited[y][x] = True
        s = True
        while q:
            y, x, cnt, level = q.popleft()
            for k in range(4):
                new_y = y + di[k]
                new_x = x + dj[k]
                if 0 <= new_y < N and 0 <= new_x < N and not visited[new_y][new_x] and fish[new_y][new_x] <= level: # 범위 안 이고 레벨 이하면 이동가능
                    if fish[new_y][new_x] and fish[new_y][new_x] < level:   # 레벨보다 낮으면 위치, 거리 저장
                        s = False
                        distance.append([new_y,new_x,cnt])
                    else:
                        visited[new_y][new_x] = True
                        q.append([new_y, new_x, cnt + 1, level])
        if not s:   # 먹었으면 while 종료
            # print(sorted(distance,key=lambda x : (x[2],x[0],x[1])))
            a,b,c = sorted(distance,key=lambda x : (x[2],x[0],x[1]))[0] # 가장 가까운, 가장 위, 가장 왼쪽 좌표로 갱신
            y = a
            x = b
            fish[a][b] = 0
            result += c
            tmp += 1
            if tmp == level:
                tmp = 0
                level += 1
            # break
        if s:   # 아무것도 못 먹었으면 전체 while 종료
            break

N = int(input())
fish = [list(map(int, input().split())) for _ in range(N)]
result = 0
for i in range(N):
    for j in range(N):
        if fish[i][j] == 9:
            fish[i][j] = 0
            shark(i, j) # 시작, 아기상어위치
print(result)