from collections import deque
a = int(input())
computer = dict()
n = int(input())
for _ in range(n):
    n_1, n_2 = map(int,input().split())
    computer.setdefault(n_1, [])
    computer[n_1] += [n_2]
    computer.setdefault(n_2, [])
    computer[n_2] += [n_1]
# print(computer)

virus = []
queue = deque([1])
while queue:
    q = queue.popleft()
    if q not in virus:
        virus.append(q)
    if q not in computer:
        continue
    temp = list(set(computer[q]) - set(virus))
    temp = sorted(temp)
    queue += temp
if 1 in virus:
    virus.remove(1)
print(len(virus))