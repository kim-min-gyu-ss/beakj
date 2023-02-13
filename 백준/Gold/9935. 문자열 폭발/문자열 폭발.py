a = input()
b = list(map(str,input()))
stack = []
for i in a:
    stack.append(i)
    if stack[-1:-len(b)-1:-1] == b[::-1]:
        for _ in range(len(b)):
            stack.pop()
if len(stack) == 0:
    print('FRULA')
else:
    print(*stack, sep ='')
