T = int(input())
dp = [0] * 301
score = [0] * 302
for j in range(T):
    score[j+1] = int(input())
dp[1] = score[1]
dp[2]  = max(score[1] + score[2], score[0] + score[1])
for i in range(3, T + 1):
    dp[i] = max(score[i] + dp[i - 2], score[i - 1] + dp[i - 3] + score[i])

print(dp[T])