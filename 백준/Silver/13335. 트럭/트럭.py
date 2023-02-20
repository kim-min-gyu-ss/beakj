from collections import deque
N,W,L = map(int,input().split())    # 트럭 수, 다리 길이, 다리 최대 하중
truck = deque(list(map(int,input().split())))
bridge = deque([0] * W)
# print(bridge)
count = 0
while truck or bridge:
    bridge.popleft()
    if truck:
        if sum(bridge) + truck[0] <= L:
            bridge.append(truck.popleft())
        else:
            bridge.append(0)
    count += 1
print(count)