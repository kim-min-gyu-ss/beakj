S = input()
stack = []
result = []
state = True
for i in S:
    if i == '<':
        if len(stack) != 0:
            result += stack[::-1]
            stack = []
        stack.append(i)
        state = False
    elif i == '>':
        stack.append(i)
        result += stack
        stack = []
        state = True
    elif i == ' ':
        if state == False:
            stack.append(i)
        else:
            result += stack[::-1] + [' ']
            stack = []
    else:
        stack.append(i)
if len(stack) != 0:
    result += stack[::-1]
print(*result, sep= '')