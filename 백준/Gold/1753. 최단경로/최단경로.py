import heapq

def check(start):
    distance = [1e9 for _ in range(V+1)]
    distance[start] = 0
    h = []
    heapq.heappush(h,(0,start))
    while h:
        dist, now = heapq.heappop(h)

        for spot,wei in lst[now]:
            cost = dist + wei
            if distance[spot] > cost:
                distance[spot] = cost
                heapq.heappush(h,(cost,spot))
    return distance


V, E = map(int,input().split())
start = int(input())
lst = [[]for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    lst[u].append([v,w])
ch = check(start)
# print(ch)
# print(lst)
for i in range(1,len(ch)):
    if ch[i] == 1e9:
        print('INF')
    else:
        print(ch[i])