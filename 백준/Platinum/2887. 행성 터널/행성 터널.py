def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def min_tree():
    result = 0
    for start, end, wei in road:
        x = find(start)
        y = find(end)
        if x != y:
            parent[y] = x
            result += wei
    return result


N = int(input())
hang = [[i, list(map(int, input().split()))] for i in range(N)]
hang_x = sorted(hang, key= lambda x : (x[1][0]))
hang_y = sorted(hang, key= lambda x : (x[1][1]))
hang_z = sorted(hang, key= lambda x : (x[1][2]))

edges = []

for i in range(N-1):
    edges.append((hang_x[i][0], hang_x[i+1][0], abs(hang_x[i][1][0] - hang_x[i+1][1][0])))
    edges.append((hang_y[i][0], hang_y[i + 1][0], abs(hang_y[i][1][1] - hang_y[i + 1][1][1])))
    edges.append((hang_z[i][0], hang_z[i + 1][0], abs(hang_z[i][1][2] - hang_z[i + 1][1][2])))

# print(hang)
# road = []
# for i in range(N):
#     for j in range(N):
#         if i != j:
#             road.append([i + 1, j + 1, min(
#                 abs(hang[i][0] - hang[j][0]), abs(hang[i][1] - hang[j][1]), abs(hang[i][2] - hang[j][2]))])
road = sorted(edges, key=lambda x : x[2])
# print(road)
parent = [i for i in range(N + 1)]
print(min_tree())