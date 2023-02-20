from collections import deque

def find1(i,j,color1):
    global result1
    global count_1
    queue = deque([[i, j]])
    temp = 0
    while queue:
        y, x = queue.popleft()
        if visited_1[y][x]:
            continue
        temp += 1
        visited_1[y][x] = True
        for k in range(4):
            new_y = y + di[k]
            new_x = x + dj[k]
            if 0 <= new_x < N and 0 <= new_y < N and not visited_1[new_y][new_x] and color1 == rgb[new_y][new_x]:
                queue.append([new_y, new_x])
    if temp != 0:
        result1.append(temp)


def find2(i,j,color2):
    global result2
    global count_2
    queue = deque([[i, j]])
    temp = 0
    while queue:
        y, x = queue.popleft()
        if visited_2[y][x]:
            continue
        temp += 1
        visited_2[y][x] = True
        for k in range(4):
            new_y = y + di[k]
            new_x = x + dj[k]
            if 0 <= new_x < N and 0 <= new_y < N and not visited_2[new_y][new_x]:
                if color2 == 'B':
                    if rgb[new_y][new_x] == 'B':
                        queue.append([new_y, new_x])
                else:
                    if rgb[new_y][new_x] == 'R' or rgb[new_y][new_x] == 'G':
                        queue.append([new_y, new_x])
    if temp != 0:
        result2.append(temp)

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
N = int(input())
rgb = []
count_1 = 0
count_2 = 0
color1 = ''
color2 = ''
result1 = []
result2 = []
for _ in range(N):
    rgb.append(list(map(str,input())))
visited_1 = [[False for _ in range(N)] for _ in range(N)]
visited_2 = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        find1(i,j,rgb[i][j])
        find2(i,j,rgb[i][j])
print(len(result1), len(result2))