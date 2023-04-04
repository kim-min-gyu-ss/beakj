import heapq
N,M = map(int,input().split())
graph = [[]for _ in range(N+1)] # 인접 리스트
for _ in range(M):  # 간선 정보 받기
    s,e,w = map(int,input().split())
    graph[s].append((e,w))
    graph[e].append((s,w))
def kruskal(graph):
    p = [i for i in range(len(graph))]
    def find(i):
        if p[i] == i:
            return i
        p[i] = find(p[i])
        return p[i]

    # 간선의 정보를 가중치로 오름차순 정렬
    edges = []
    for u in range(len(graph)):
        for v, w in graph[u]:
            edges.append((u, v, w))
    edges.sort(key=lambda x: x[2])

    # MST 간선 가중치의 합
    total_weight = 0

    for u, v, w in edges:
        # 정점 u와 정점 v에 대한 대표자를 확인
        x = find(u)
        y = find(v)

        if x != y:
            p[y] = x
            total_weight += w
    return total_weight
print(kruskal(graph))