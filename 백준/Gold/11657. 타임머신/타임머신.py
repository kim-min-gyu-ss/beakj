def bellman(start):
    distace[start] = 0
    for i in range(N):
        for j in range(M):
            st, ed, cost = time[j]
            if distace[st] != 1e9 and distace[st] + cost < distace[ed]:
                distace[ed] = distace[st] + cost
                if i == N - 1:
                    return False
    return True

N, M = map(int,input().split())
time = [list(map(int,input().split())) for _ in range(M)]
distace = [1e9 for _ in range(N+1)]
if bellman(1):
    for i in distace[2:]:
        if i == 1e9:
            print(-1)
        else:
            print(i)
else:
    print(-1)