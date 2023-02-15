import sys
input = sys.stdin.readline
def back():
    if len(stack) == M:
        for i in range(len(stack) - 1):
            if stack[i] > stack[i+1]:
                return
        print(*stack, sep = ' ')
        return
    for i in range(1, N+1):
        if visited[i]:
            continue
        # visited[i] = True
        stack.append(i)
        back()
        stack.pop()
        # visited[i] = False


N, M = map(int, input().split())
visited = [False] * (N + 1)
stack = []
back()