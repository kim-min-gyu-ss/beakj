def back():
    if len(stack) == 6:
        store.add(tuple(sorted(stack)))
        return
    for i in range(k):
        if visited[i]:
            continue
        visited[i] = True
        stack.append(num_list[i])
        back()
        stack.pop()
        visited[i] = False


while True:
    k, *num_list = map(int,input().split())
    if k == 0:
        break
    visited = [False] * (k+1)
    store = set()
    stack = []
    back()
    store = sorted(store)
    for i in store:
        print(*i)
    print()