di = [-1,1,0,0]
dj = [0,0,-1,1]

def air():
    global misae
    tmp = [[0 for _ in range(C)]for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if misae[i][j]:
                if misae[i][j] >= 5:
                    cnt = 0
                    for k in range(4):
                        new_i = i + di[k]
                        new_j = j + dj[k]
                        if 0 <= new_i < R and 0 <= new_j < C:
                            if not new_j and new_i == start[0]:
                                continue
                            if not new_j and new_i == start[1]:
                                continue

                            tmp[new_i][new_j] += misae[i][j]//5
                            cnt += 1
                    tmp[i][j] += misae[i][j] - cnt * (misae[i][j]//5)
                else:
                    tmp[i][j] += misae[i][j]
    misae = tmp

def claen_up(s):
    di = [-1,0,1,0]
    dj = [0,1,0,-1]
    i = s
    j = 0
    state = 0
    c = 0
    while True:
        new_i = i + di[state]
        new_j = j + dj[state]
        if new_i == s and new_j == 0:
            misae[i][j] = 0
            break
        if new_i < 0 or new_i >= s + 1 or new_j < 0 or new_j >= C:
            state += 1
            c += 1
            continue
        if c:
            misae[i][j] = misae[new_i][new_j]
            i = new_i
            j = new_j
        else:
            i = new_i
            j = new_j
            c += 1
            continue


def claen_down(s):
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    i = s
    j = 0
    state = 0
    c = 0
    while True:
        new_i = i + di[state]
        new_j = j + dj[state]
        if new_i == s and new_j == 0:
            misae[i][j] = 0
            break
        if new_i < s or new_i >= R or new_j < 0 or new_j >= C:
            state += 1
            c += 1
            continue
        if c:
            misae[i][j] = misae[new_i][new_j]
            i = new_i
            j = new_j
        else:
            i = new_i
            j = new_j
            c += 1
            continue


R, C, T = map(int,input().split())
misae = [list(map(int,input().split())) for _ in range(R)]
start = []
for i in range(R):
    if misae[i][0] == -1:
        start.append(i)

cnt = result = 0
for _ in range(T):
    air()
    claen_up(start[0])
    claen_down(start[1])
for i in range(R):
    for j in range(C):
        if misae[i][j] > 0:
            result += misae[i][j]
print(result)