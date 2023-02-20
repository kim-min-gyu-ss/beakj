from collections import deque

N, K = map(int, input().split())  # N = 칸수, K = 내구도 0인 칸 수
robot = deque([0] * N)
# print(robot)
belt = deque(list(map(int, input().split())))
result = 0
cnt = 0
while True:
    result += 1
    belt.appendleft(belt.pop())
    robot[-1] = 0
    robot.appendleft(robot.pop())
    robot[-1] = 0

    for i in range(N - 2, 0, -1):
        if robot[i] == 1 and robot[i + 1] == 0:
            if belt[i + 1] != 0:
                robot[i], robot[i + 1] = robot[i + 1], robot[i]
                belt[i + 1] -= 1
                if belt[i + 1] == 0:
                    cnt += 1

    if belt[0] != 0:
        belt[0] -= 1
        if belt[0] == 0:
            cnt += 1
        robot[0] += 1

    if cnt >= K:
        break
print(result)