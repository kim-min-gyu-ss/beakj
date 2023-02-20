from collections import deque
N = int(input())
num_list = deque(list(range(1,N+1)))
result = []
while num_list:
    if len(num_list) == 1:
        result.append(num_list.popleft())
        break
    else:
        result.append(num_list.popleft())
    if len(num_list) == 1:
        result.append(num_list.popleft())
    else:
        num_list.append(num_list.popleft())
print(result[-1])