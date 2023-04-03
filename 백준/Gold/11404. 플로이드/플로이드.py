N = int(input())
M = int(input())
cost = [[1e9 for _ in range(N)] for i in range(N)]

for i in range(M):
    a, b, c = map(int, input().split())
    if cost[a - 1][b - 1] > c:
        cost[a - 1][b - 1] = c

for k in range(N):  # 경유지
    for i in range(N):  # 출발
        for j in range(N):  # 도착
            if i != j and cost[i][j] > cost[i][k] + cost[k][j]:
                cost[i][j] = cost[i][k] + cost[k][j]
# print(cost)
for i in cost:
    for j in i:
        if j == 1e9:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()