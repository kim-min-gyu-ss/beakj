a = int(input())
for _ in range(a):
    k = int(input())
    n = int(input())
    dp = [[0 for _ in range(n+1)]for _ in range(k+2)]
    for i in range(1,n+1):
        dp[1][i] = i
    for j in range(2,k+2):
        for l in range(1,n+1):
            dp[j][l] = sum(dp[j-1][0:l+1])
    # print(dp)
    print(dp[k+1][-1])