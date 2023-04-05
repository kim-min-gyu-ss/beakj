def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def min_tree():
    result = 0
    for start, end, wei in com:
        # 정점 u와 정점 v에 대한 대표자를 확인
        x = find(start)
        y = find(end)
        if x != y:
            parent[y] = x
            result += wei
    return result

N = int(input())
M = int(input())
com = [list(map(int,input().split())) for _ in range(M)]
com = sorted(com, key= lambda x : x[2])
parent = [i for i in range(N+1)]
print(min_tree())