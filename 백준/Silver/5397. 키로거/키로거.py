a = int(input())
for _ in range(a):
    L = input()
    stack_1 = []
    stack_2 = []
    for i in L:
        if i == '<':
            if len(stack_1) == 0:
                continue
            else:
                stack_2.append(stack_1.pop())
        elif i == '>':
            if len(stack_2) == 0:
                continue
            else:
                stack_1.append(stack_2.pop())
        elif i == '-':
            if len(stack_1) == 0:
                continue
            else:
                stack_1.pop()
        else:
            stack_1.append(i)
    if len(stack_2) != 0:
        stack_1 += reversed(stack_2)
    print(*stack_1, sep='')
