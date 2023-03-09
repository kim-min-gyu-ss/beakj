from collections import deque

d = [-1, 1]
def bfs(q):
    global result
    cnt = 0
    while q:
        n, num = q.popleft()
        for k in range(2):
            new_n = n + d[k]
            if new_n in visited:
                continue
            cnt += 1
            result += num
            visited.add(new_n)
            q.append([new_n, num + 1])
            if cnt == K:
                return

N, K = map(int, input().split())
sam = list(map(int, input().split()))
visited = set()
q = deque([])
for i in sam:
    q.append([i,1])
    visited.add(i)
result = 0
bfs(q)
print(result)