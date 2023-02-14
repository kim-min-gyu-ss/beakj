a = int(input())
for _ in range(a):
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    for i in range(5,101):
        dp[i] = dp[i-1] + dp[i-5]
    n = int(input())
    print(dp[n])
