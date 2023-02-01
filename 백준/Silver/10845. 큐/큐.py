import sys
input = sys.stdin.readline
a = int(input())
que = []
for i in range(a):
    b = list(map(str, input().split()))

    if b[0] == 'push':
        que.append(b[1])

    if b[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            c = que.pop(0)
            print(c)

    if b[0] == 'size':
        print(len(que))

    if b[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)

    if b[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])

    if b[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])