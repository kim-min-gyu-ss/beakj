import sys
input = sys.stdin.readline
a = int(input())
stack = []
for i in range(a):
    b = list(map(str,input().split()))
    if b[0] == 'push':
        stack.append(int(b[1]))
    elif b[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            p = stack.pop()
            print(p)
    elif b[0] == 'size':
        print(len(stack))
    elif b[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif b[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])