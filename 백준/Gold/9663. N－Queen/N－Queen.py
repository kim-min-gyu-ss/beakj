def find(y,cnt):
    global result
    if cnt == N:
        result += 1
        return

    for x in range(N):
        if not visited1[x] and not visited2[y + x] and not visited3[y - x + N - 1]:
            visited1[x] = True
            visited2[x + y] = True
            visited3[y - x + N - 1] = True
            find(y + 1, cnt + 1)
            visited1[x] = False
            visited2[x + y] = False
            visited3[y - x + N - 1] = False

N = int(input())
visited1 = [0 for _ in range(N)]
visited2 = [0 for _ in range(2 * N - 1)]
visited3 = [0 for _ in range(2 * N - 1)]
result = 0
find(0,0)
print(result)