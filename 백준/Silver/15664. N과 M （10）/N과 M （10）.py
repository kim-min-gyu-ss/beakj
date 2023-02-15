def back():
    if len(stack) == M:
        for i in range(len(stack) - 1):
            if stack[i] > stack[i+1]:
                return
        # print(*stack, sep = ' ')
        store.add(tuple(stack))
        # print(store)
        return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        stack.append(num_list[i])
        back()
        stack.pop()
        visited[i] = False


N, M = map(int, input().split())
num_list = sorted(list(map(int,input().split())))
visited = [False] * (N+1)
store = set()
stack = []
back()
store = sorted(store)
for i in store:
    print(*i)