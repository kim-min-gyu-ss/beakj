N, K = map(int,input().split())
bags = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
bag = []
for _ in range(K):
    bag.append(list(map(int, input().split())))

for i in range(1, K + 1):   # 시작?
    value = bag[i - 1][0]
    time = bag[i - 1][1]
    for j in range(1, N + 1):   # 시간
        if time > j:
            bags[i][j] = bags[i - 1][j] # 시간보다 낮으면 위에값으로 갱신
        else:
            bags[i][j] = max(bags[i - 1][j], value + bags[i-1][j - time])
            # 위에 값이랑 시간 뺸 위에값이랑 비교
print(bags[K][N])