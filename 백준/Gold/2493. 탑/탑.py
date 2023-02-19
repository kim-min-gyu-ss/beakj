len_list = int(input())
num_list = list(map(int,input().split()))
stack = []
result = []

for i in range(len_list):
    if i == 0:
        stack.append([i,num_list[i]])
        result.append(0)
    else:
        while stack:
            if stack[-1][-1] < num_list[i]:
                stack.pop()
            else:
                result.append(stack[-1][0] + 1)
                break
        if not stack:
            result.append(0)
        stack.append([i,num_list[i]])
print(*result)