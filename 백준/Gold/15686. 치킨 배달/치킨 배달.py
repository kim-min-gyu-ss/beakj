from itertools import combinations

def check(chw):
    result = 0
    for i in range(N):
        for j in range(N):
            if chicken[i][j] == 1:
                tmp = []
                for k in chw:
                    tmp.append(abs(k[0]-i) + abs(k[1]-j))
                result += min(tmp)
    return result

N, M = map(int,input().split())
chicken = [list(map(int,input().split()))for _ in range(N)]
ch = []
for i in range(N):
    for j in range(N):
        if chicken[i][j] == 2:
            ch.append([i,j])

final = []
for i in combinations(ch,M):
    final.append(check(i))
print(min(final))