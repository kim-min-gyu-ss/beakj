def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def min_tree():
    result = 0
    count = 0
    for start, end, wei in road:
        x = find(start)
        y = find(end)
        if x != y:
            parents[y] = x
            result += wei
            count += 1
    if count == N - 1:
        return result
    else:
        return -1

N, M = map(int, input().split())
uni = input().split()
road = []
for _ in range(M):
    u, v, d = map(int, input().split())
    if uni[u - 1] != uni[v - 1]:
        road.append([u, v, d])
road = sorted(road, key=lambda x: x[2])
parents = [i for i in range(N + 1)]
print(min_tree())