from collections import deque
N = int(input())
num_list = [[] for _ in range(N+1)]
for _ in range(N-1):
    n_1, n_2 = map(int,input().split())
    num_list[n_1].append(n_2)
    num_list[n_2].append(n_1)
q = deque([1])
parents = [[] for _ in range(N+1)]
visited = [False] * (N+1)
visited[1] = True

while q:
    s = q.popleft()
    for i in num_list[s]:
        if not visited[i]:
            visited[i] = True
            parents[i] = s
            q.append(i)
for k in range(2,len(parents)):
    print(parents[k])