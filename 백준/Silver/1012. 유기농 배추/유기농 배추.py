T = int(input())
dx = [-1,1,0,0]
dy = [0,0,1,-1]
for _ in range(T):
    M, N, K = map(int,input().split())   # 가로 세로
    bachoo = [[0 for _ in range(M)] for _ in range(N)]
    count = 0
    for _ in range(K):
        x, y = map(int,input().split())
        bachoo[y][x] = 1
    for i in range(N): # 세로
        for j in range(M):  # 가로
            if bachoo[i][j] == 1:
                bachoo[i][j] = 0
                stack = [(i,j)]
                while stack:
                    y1, x1 = stack.pop()
                    for k in range(4):
                        new_y = y1 + dy[k]
                        new_x = x1 + dx[k]
                        if 0 <= new_x < M and 0 <= new_y < N and bachoo[new_y][new_x] == 1:
                            bachoo[new_y][new_x] = 0
                            stack.append((new_y, new_x))
                count += 1
    print(count)