def a(y, x, n):
    b = num[y][x]
    cnt = 0
    for i in range(y, y + n):
        for j in range(x, x + n):
            if num[i][j] == b:
                cnt += 1
    if cnt == n * n:
        result[b+1] += [1]
        return

    a(y, x, n // 3)
    a(y, x + n // 3, n // 3)
    a(y, x + n // 3 * 2, n // 3)
    a(y + n // 3, x, n // 3)
    a(y + n // 3 * 2, x, n // 3)
    a(y + n // 3, x + n // 3, n // 3)
    a(y + n // 3, x + n // 3 * 2, n // 3)
    a(y + n // 3 * 2, x + n // 3, n // 3)
    a(y + n // 3 * 2, x + n // 3 * 2, n // 3)


N = int(input())
num = []
for _ in range(N):
    num.append(list(map(int, input().split())))
result = [[],[],[]]
a(0,0,N)
for i in result:
    print(len(i))