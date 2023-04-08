def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def min_tree():
    result = 0
    for start, end, wei, ar in road:
        x = find(start)
        y = find(end)
        if x != y:
            parents[y] = x
            result += wei
    return result

N, M = map(int, input().split())
road = []
sum = 0
for _ in range(M):
    a,b,c,d = map(int, input().split())
    road.append([a,b,c,d])
    sum += c
road = sorted(road, key=lambda x: (-x[3], -x[2]))
parents = [i for i in range(N + 1)]
print(sum - min_tree())