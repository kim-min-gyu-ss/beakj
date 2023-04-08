N, M = map(int,input().split())
cost = [[1e9 for _ in range(N+1)] for i in range(N+1)]

for i in range(M):
    a, b, c = map(int, input().split())
    cost[a][b] = c  # 일방통행

for k in range(1,N+1):  # 경유지
    for i in range(1,N+1):  # 출발
        for j in range(1,N+1):  # 도착
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
# print(cost)

result = 1e9
for i in range(1,N+1):
    result = min(result, cost[i][i])

if result == 1e9:
    print(-1)
else:
    print(result)