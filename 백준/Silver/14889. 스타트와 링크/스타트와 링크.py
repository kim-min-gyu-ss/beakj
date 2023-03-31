def dfs(y, x):
    global result

    if y == N // 2:
        hap1, hap2 = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    hap1 += mat[i][j]
                elif not visited[i] and not visited[j]:
                    hap2 += mat[i][j]
        result = min(result, abs(hap1 - hap2))
        return

    for i in range(x, N):
        if not visited[i]:
            visited[i] = True
            dfs(y + 1, i + 1)
            visited[i] = False



N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
result = 1000000
dfs(0, 0)
print(result)