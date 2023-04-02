import heapq

def dijkstra():
    q = []
    heapq.heappush(q,(0,0))
    distance[0] = 0
    while q:
        dist, now = heapq.heappop(q)

        #지금 힙큐에서 뺀게 now까지 가는데 최소비용이 아닐수도 있으니 체크
        if dist > distance[now]:
            continue

        for i in load[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))


N , D = map(int,input().split())
load = [[] for _ in range(D+1)]
distance = [int(1e9)] * (D+1)

#일단 거리 1로 초기화.
for i in range(D):
    load[i].append((i+1, 1))

#지름길 있는 경우에 업데이트
for _ in range(N):
    s, e, l = map(int,input().split())
    if e > D:# 고려 안해도 됨.
        continue
    load[s].append((e,l))

dijkstra()
print(distance[D])