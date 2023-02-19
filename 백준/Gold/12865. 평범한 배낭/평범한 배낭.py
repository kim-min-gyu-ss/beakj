N, K = map(int, input().split())
bags = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
bag = []
for _ in range(N):
    bag.append(list(map(int, input().split())))

for i in range(1, N + 1):
    kg = bag[i - 1][0]
    vl = bag[i - 1][1]
    for j in range(1, K + 1):
        if kg > j:
            bags[i][j] = bags[i - 1][j]
        else:
            bags[i][j] = max(bags[i - 1][j], vl + bags[i-1][j - kg])
print(bags[N][K])