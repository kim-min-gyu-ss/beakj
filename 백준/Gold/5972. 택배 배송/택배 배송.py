import heapq
def dc(start):
    yoemul = [1e9 for _ in range(N+1)]
    yoemul[start] = 0
    h = []
    heapq.heappush(h, (0, start))
    while h:
        dist, now = heapq.heappop(h)

        for spot, wei in so[now]:
            cost = dist + wei
            if yoemul[spot] > cost:
                yoemul[spot] = cost
                heapq.heappush(h, (cost, spot))
    return yoemul


N, M = map(int,input().split())
so = [[]for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    so[a].append((b,c))
    so[b].append((a,c))
print(dc(1)[-1])