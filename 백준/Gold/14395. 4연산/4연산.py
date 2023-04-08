from collections import deque

def check(goal, start):
    global result
    q = deque()
    q.append((start, result))
    visited.append(start)
    while q:
        hap, cnt = q.popleft()
        if hap == goal:
            result = cnt
            break

        if 0 < hap * hap <= 1000000000 and hap * hap not in visited:
            visited.append(hap * hap)
            q.append([hap * hap, cnt + '*'])

        if 0 < hap + hap <= 1000000000 and hap + hap not in visited:
            visited.append(hap + hap)
            q.append([hap + hap, cnt + '+'])

        if 0 < hap - hap <= 1000000000 and hap - hap not in visited:
            visited.append(hap - hap)
            q.append([hap - hap, cnt + '-'])

        if hap and 0 < hap / hap <= 1000000000 and hap / hap not in visited:
            visited.append(hap / hap)
            q.append([hap / hap, cnt + '/'])

S, T = map(int, input().split())
visited = []
result = ''
check(T, S)
if S == T:
    print(0)
elif not result:
    print(-1)
else:
    print(result)