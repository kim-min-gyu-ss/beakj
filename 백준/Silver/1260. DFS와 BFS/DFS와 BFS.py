# import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')

N, M, V = map(int,input().split())
nodes = dict()
for _ in range(M):
    N_1, N_2 = map(int,input().split())
    nodes.setdefault(N_1,[])
    nodes[N_1] += [N_2]
    nodes.setdefault(N_2,[])
    nodes[N_2] += [N_1]

dfs_list = []
dfs_stack = [V]
while dfs_stack:
    a = dfs_stack.pop()
    if a not in dfs_list:
        dfs_list.append(a)
    if a not in nodes:
        continue
    temp_1 = list(set(nodes[a]) - set(dfs_list))
    temp_1 = sorted(temp_1, reverse= True)
    dfs_stack += temp_1
print(*dfs_list)

bfs_list = []
bfs_queue = deque([V])
while bfs_queue:
    b = bfs_queue.popleft()
    if b not in bfs_list:
        bfs_list.append(b)
    if b not in nodes:
        continue
    temp_2 = list(set(nodes[b]) - set(bfs_list))
    temp_2 = sorted(temp_2)
    bfs_queue += temp_2
print(*bfs_list)

