def check(x, y, N):
    ck = jong_e[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if jong_e[i][j] != ck:
                return False
    return True


def w_or_b(r, c, N):
    global count_w
    global count_b

    if N == 1:
        if jong_e[r][c] == 0:
            count_w += 1
        else:
            count_b += 1
        return

    result = check(r, c, N)
    if result:
        if jong_e[r][c] == 0:
            count_w += 1
        else:
            count_b += 1
        return

    mid = N // 2

    w_or_b(r, c, N // 2)
    w_or_b(r + mid, c, N // 2)
    w_or_b(r, c + mid, N // 2)
    w_or_b(r + mid, c + mid, N // 2)


M = int(input())
jong_e = []
count_w = 0
count_b = 0
for _ in range(M):
    jong_e.append(list(map(int, input().split())))

w_or_b(0, 0, M)
print(count_w)
print(count_b)
