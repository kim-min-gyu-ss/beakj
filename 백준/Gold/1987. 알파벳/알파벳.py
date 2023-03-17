import sys
input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]

def dfs(i,j):
    global result
    global tmp
    # print(tmp)
    # if visited[alpha[i][j]]:
    #     if result < tmp:
    #         result = tmp
    #     tmp += 1
    #     return
    tmp += 1
    visited[alpha[i][j]] += 1
    for k in range(4):
        new_y = i + di[k]
        new_x = j + dj[k]
        if 0 <= new_y < R and 0 <= new_x < C and not visited[alpha[new_y][new_x]]:
            dfs(new_y,new_x)
            if result < tmp:
                result = tmp
            if tmp > 1:
                tmp -= 1
            visited[alpha[new_y][new_x]] -= 1

R, C = map(int,input().split())
alpha = [list(map(lambda x: ord(x)-65,input())) for _ in range(R)]
visited = [0] * 26
result = 0
tmp = 0
# print(alpha)
dfs(0,0)
if not result:
    print(1)
else:
    print(result)