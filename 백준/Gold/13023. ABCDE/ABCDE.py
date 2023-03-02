def find(n,cnt):
    global state
    if cnt == 4:
        state = True
        return

    visited[n] = True
    for i in num_list[n]:
        if not visited[i]:
            find(i,cnt + 1)
            visited[i] = False


N, M = map(int,input().split())
num_list = [[]for _ in range(N)]
for _ in range(M):
    n_1, n_2 = map(int,input().split())
    num_list[n_1] += [n_2]
    num_list[n_2] += [n_1]
visited = [False for _ in range(N)]
state = False
for i in range(N):
    find(i,0)
    visited[i] = False
    if state:
        break
if state:
    print(1)
else:
    print(0)