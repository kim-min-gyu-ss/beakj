import sys
input = sys.stdin.readline

di = [-1,1,0,0]
dj = [0,0,-1,1]

def dfs(y,x):

    if y == N-1 and x == M-1:
        return 1

    if dp[y][x] == -1:
        dp[y][x] = 0
        
        tmp = road[y][x]
        for k in range(4):
            new_y = y + di[k]
            new_x = x + dj[k]
            if 0 <= new_x < M and 0 <= new_y < N and tmp > road[new_y][new_x]:
                dp[y][x] += dfs(new_y,new_x)

    return dp[y][x]

N,M = map(int,input().split())  # 세로, 가로
road = [list(map(int,input().split())) for _ in range(N)]
dp = [[-1 for _ in range(M)]for _ in range(N)]
result = dfs(0,0)
# print(dp)
print(result)