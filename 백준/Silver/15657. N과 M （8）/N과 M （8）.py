import sys
input = sys.stdin.readline
def back():
    if len(stack) == M:
        for i in range(len(stack) - 1):
            if stack[i] > stack[i+1]:
                return
        print(*stack, sep = ' ')
        return
    for i in num_list:
        if visited[i]:
            continue
        # visited[i] = True
        stack.append(i)
        back()
        stack.pop()
        # visited[i] = False


N, M = map(int, input().split())
num_list = sorted(list(map(int,input().split())))
visited = [False] * (num_list[-1]+1)
stack = []
back()