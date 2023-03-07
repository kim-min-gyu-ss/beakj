def find(s, e):
    if s == e:
        return
    a = sorted(string[s:e])[0]
    idx = string[s:e].index(a) + s
    visited[idx] = True
    for i in range((n)):
        if visited[i]:
            print(string[i], end='')
    print()
    find(idx + 1, e)
    find(s, idx)

string = list(input())
visited = [False] * len(string)
n = len(string)
find(0, n)