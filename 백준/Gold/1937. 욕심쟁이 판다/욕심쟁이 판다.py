import sys
sys.setrecursionlimit(10 ** 6)

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def check(y,x):
    if dp[y][x] == -1:
        dp[y][x] = 1

        tmp = panda[y][x]
        for k in range(4):
            new_y = y + di[k]
            new_x = x + dj[k]
            if 0 <= new_x < N and 0 <= new_y < N and tmp < panda[new_y][new_x]:
                dp[y][x] = max(dp[y][x], check(new_y,new_x) + 1)
    return dp[y][x]



N = int(input())
panda = [list(map(int,input().split())) for _ in range(N)]
dp = [[-1 for _ in range(N)] for _ in range(N)]
result = 0
for i in range(N):
    for j in range(N):
        result = max(result,check(i,j))
print(result)