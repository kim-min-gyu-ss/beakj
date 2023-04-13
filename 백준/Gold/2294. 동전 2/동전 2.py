N, K = map(int,input().split())
dongjyeon = [int(input()) for _ in range(N)]
dp = [10001 for _ in range(K+1)]
dp[0] = 0
for i in dongjyeon:
    for j in range(i,K+1):
        dp[j] = min(dp[j],dp[j-i]+1)
if dp[K] == 10001:
    print(-1)
else:
    print(dp[K])