a = int(input())
forth = input()
num_list = []
for _ in range(a):
    num_list.append(int(input()))
stack = []
for i in forth:
    if i in ['+', '-', '*', '/']:
        b = stack.pop()
        a = stack.pop()
        if i == '+':
            stack.append(a+b)
        elif i == '-':
            stack.append(a - b)
        elif i == '*':
            stack.append(a * b)
        elif i == '/':
            stack.append(a / b)
    else:
        stack.append(int(num_list[ord(i) - 65]))

print('{:.2f}'.format(stack[0]))