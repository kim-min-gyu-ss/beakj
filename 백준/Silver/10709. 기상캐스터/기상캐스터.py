H,W = map(int,input().split())
sky = [list(map(str,input()))for _ in range(H)]
cloud = [[0 for _ in range(W)]for _ in range(H)]

for i in range(H):
    state = False
    tmp = 0
    for j in range(W):
        if sky[i][j] == 'c':
            cloud[i][j] = 0
            state = True
            tmp = 0
        else:
            if not state:
                cloud[i][j] = -1
            else:
                tmp += 1
                cloud[i][j] = tmp
for j in cloud:
    print(*j)