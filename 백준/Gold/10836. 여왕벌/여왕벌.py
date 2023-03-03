import sys
input = sys.stdin.readline

def ch(y,x,z):
    cnt = 0
    worms = [[0 for _ in range(M)] for _ in range(M)]
    state = True
    while cnt < M * 2 - 1:
        worms[y][x] = change[z][cnt]
        if state:
            y -= 1
            if y == 0:
                state = False
        else:
            x += 1
        cnt += 1

    for i in range(1,M):
        for j in range(1,M):
            worms[i][j] = max(worms[i-1][j-1], worms[i-1][j], worms[i][j-1])

    for i in range(M):
        for j in range(M):
            bulrae[i][j] += worms[i][j]
    # print(worms)


M, N = map(int,input().split())
c = [list(map(int,input().split())) for _ in range(N)]  # 변화 빈도
bulrae = [[1 for _ in range(M)]for _ in range(M)]   # 총 벌레 수
worms = [[0 for _ in range(M)] for _ in range(M)]   # 임시 벌레 수
change = [[]for _ in range(N)]  # 날짜별 변화 빈도
for q in range(N):
    cnt = 0
    for w in c[q]:
        change[q] += [cnt] * w
        cnt += 1
# print(change)

for i in range(N):
    ch(M-1,0,i)
for l in bulrae:
    print(*l)