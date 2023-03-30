def back(y, x, hp, num, state):
    global result

    if state:
        b = abs(y - t_y) + abs(x - t_x)
        if b <= hp:
            result = max(result, num)

    for i in range(len(mc)):
        a = abs(mc[i][0] - y) + abs(mc[i][1] - x)
        if a <= hp and not visited[i]:
            visited[i] = True
            back(mc[i][0], mc[i][1], hp - a + H, num + 1, True)
            visited[i] = False

N, M, H = map(int, input().split())
mincho = [list(map(int, input().split())) for _ in range(N)]
result = 0
mc = []
t_x = t_y = 0
for i in range(N):
    for j in range(N):
        if mincho[i][j] == 2:
            mc.append([i, j])
        elif mincho[i][j] == 1:
            t_y = i
            t_x = j
visited = [False for _ in range(len(mc))]
back(t_y, t_x, M, 0, False)
print(result)