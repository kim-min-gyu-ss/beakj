import sys
input = sys.stdin.readline
result_list = list(map(str,input().rstrip()))
a = int(input())
order = []
stack = []
for _ in range(a):
    order.append(list(map(str,input().split())))
for i in order:
    if i[0] == 'L':
        if result_list != []:
            stack.append(result_list.pop())
    elif i[0] == 'D':
        if stack != []:
            result_list.append(stack.pop())
    elif i[0] == 'B':
        if result_list != []:
            result_list.pop()
    elif i[0] == 'P':
        result_list.append(i[1])
plus = reversed(stack)
result_list += plus
print(*result_list, sep='')