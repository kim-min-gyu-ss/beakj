S = input()
stack = []
cnt = 0
result = 0
for i in range(len(S)):
    if S[i] in ['(',')']:
        if S[i] == '(':
            stack.append(S[i])
        else:
            while stack[-1] != '(':
                a = stack.pop()
                cnt += a
            stack.pop()
            a = stack.pop()
            stack.append(a * cnt)
            cnt = 0
    elif i < len(S) - 1 and S[i+1] == '(':
        stack.append(int(S[i]))
    else:
        stack.append(1)
# print(stack)
for r in stack:
    result += r
print(result)