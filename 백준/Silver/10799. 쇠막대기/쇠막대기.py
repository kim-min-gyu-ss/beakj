a = input()
stack = []
count = 0
for i in a:
    if i == '(':
        state = True
        stack.append(i)
    elif i == ')':
        if stack[-1] == '(':
            if state == False:
                stack.pop()
                count += 1
            else:
                stack.pop()
                count += len(stack)
                state = False
        elif stack[-1] == ')':
            stack.pop()
            count += 1
print(count)