from collections import deque
from itertools import combinations

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(vrs):
    global state
    global result
    qq = z_cnt + s_cnt  # 0이랑 2 위치 더한값, 0 안되면 덜 퍼진곳 있음
    tmp = 0 # 일시적인 저장값
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in vrs:
        visited[i[0]][i[1]] = True
    while vrs:
        y, x, cnt, st = vrs.popleft()
        if not st:
            if tmp < cnt:   # 가장 오래 걸리는 값 갱신
                tmp = cnt
        qq -= 1 # 1씩 줄여 가면서 덜 퍼진 곳 확인
        for k in range(4):
            new_y = y + di[k]
            new_x = x + dj[k]
            if 0 <= new_x < N and 0 <= new_y < N and not visited[new_y][new_x] and not virus[new_y][new_x]:
                visited[new_y][new_x] = True
                vrs.append([new_y, new_x, cnt + 1, False])
            if 0 <= new_x < N and 0 <= new_y < N and not visited[new_y][new_x] and virus[new_y][new_x] == 3:
                visited[new_y][new_x] = True
                vrs.append([new_y, new_x, cnt + 1, True])

    if qq > 0:  # 덜 퍼졌으면 그냥 끝냄
        return
    else:
        if tmp < result:  # 다 퍼졌으면 결과값 비교
            result = tmp
        # print(tmp)
        state = True    # 한번이라도 퍼졌다는 표시
        return


N, M = map(int, input().split())
virus = [list(map(int, input().split())) for _ in range(N)]
vv = [] # 바이러스 있을수 있는 좌표
vrs = deque([])
state = False
z_cnt = 0   # 0 갯수
s_cnt = 0   # 바이러스 갯수
result = 1000000 # 결과값
for i in range(N):
    for j in range(N):
        if not virus[i][j]:
            z_cnt += 1
        elif virus[i][j] == 2:
            virus[i][j] = 3 # 바이러스 좌표넣고 3으로 바꿔줌
            vv.append([i, j])
            s_cnt += 1

for i in combinations(vv, M):   # 모든 경우의수
    # print(i)
    for j in i:
        virus[j[0]][j[1]] = 2   # 바이러스 2로 바꿔주고
        vrs.append([j[0], j[1], 0, False]) # 큐에 넣고 함수돌림

    bfs(vrs)

    for k in i:
        virus[k[0]][k[1]] = 3   # 다시 바이러스 0으로 바꿔줌

if state:   # 한번이라도 바이러스 다 퍼질수 있으면
    print(result)
else:   # 한번도 바이러스 다 못퍼지면
    print(-1)