di = [-1,1,0,0]
dj = [0,0,-1,1]

N = int(input())
jong_e = [[0 for _ in range(102)]for _ in range(102)]
result = 0
for _ in range(N):
    x,y = map(int,input().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            if not jong_e[i][j]:
                jong_e[i][j] = 1
# print(jong_e)
for i in range(100):
    for j in range(100):
        y,x = i,j
        tmp = 0
        if not jong_e[y][x]:
            continue
        for k in range(4):
            new_y = y + di[k]
            new_x = x + dj[k]
            if 0 <= new_y < 101 and 0 <= new_x < 101 and not jong_e[new_y][new_x]:
                tmp += 1
        if tmp:
            result += tmp
print(result)