N = int(input())
podoju = [0] + [int(input()) for _ in range(N)]
dp = [0 for _ in range(N + 1)]
dp[1] = podoju[1]
if N > 1:
    dp[2] = dp[1] + podoju[2]
for i in range(3, N + 1):
    dp[i] = max(dp[i - 1], dp[i - 3] + podoju[i - 1] + podoju[i], dp[i - 2] + podoju[i])
print(dp[-1])