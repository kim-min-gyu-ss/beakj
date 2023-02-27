import sys
input = sys.stdin.readline
from collections import deque
D, N = map(int,input().split())
oven = list(map(int,input().split()))
for j in range(1,len(oven)):
    if oven[j] > oven[j-1]:
        oven[j] = oven[j-1]
pizza = deque(list(map(int,input().split())))
state = True
cnt = 0
while pizza:
    q = pizza.popleft()
    for i in range(D-1,-1,-1):
        if q <= oven[i]:
            D = i
            cnt += 1
            break
        if i == 0:
            D = i
    if (D == 0 and pizza) or cnt == 0:
        state = False
        break
if state == False:
    print(0)
else:
    print(D+1)