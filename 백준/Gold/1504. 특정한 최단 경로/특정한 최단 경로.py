import heapq

def check(start):
    distance = [1e9 for _ in range(V + 1)]
    distance[start] = 0
    h = []
    heapq.heappush(h, (0, start))
    while h:
        dist, now = heapq.heappop(h)

        for spot, wei in lst[now]:
            cost = dist + wei
            if distance[spot] > cost:
                distance[spot] = cost
                heapq.heappush(h, (cost, spot))
    return distance

V, E = map(int, input().split())
lst = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    lst[u].append([v, w])
    lst[v].append([u, w])
v1, v2 = map(int, input().split())
ch0 = check(1)
ch1 = check(v1)
ch2 = check(v2)
a = ch0[v1] + ch1[v2] + ch2[-1]
b = ch0[v2] + ch2[v1] + ch1[-1]
result = min(a, b)
if result >= 1e9:
    print(-1)
else:
    print(result)