N, K = map(int,input().split())
dongjyeon = [int(input()) for _ in range(N)]
dp = [0 for _ in range(10001)]
dp[0] = 1
for i in dongjyeon:
    for j in range(i,K+1):
        dp[j] += dp[j-i]
print(dp[K])