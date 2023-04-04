def find(i):
    if union[i] == i:
        return i
    union[i] = find(union[i])
    return union[i]

def hap(u,v):
    x = find(u)
    y = find(v)
    if x != y:
        union[y] = x

def check(u,v):
    x = find(u)
    y = find(v)
    if x != y:
        print('NO')
    else:
        print('YES')

N, M = map(int,input().split())
union = [i for i in range(N+1)]
for _ in range(M):
    s,a,b = map(int,input().split())
    if s:
        check(a,b)
    else:
        hap(a,b)