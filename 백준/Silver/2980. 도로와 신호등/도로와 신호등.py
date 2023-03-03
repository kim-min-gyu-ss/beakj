def check(num):
    global cnt
    state = False
    r, b = light[num][1], light[num][2]  # 신호등 상태
    stack = [r, b]
    tmp = cnt
    i = 0
    while i < tmp:
        if i == stack[0]:
            stack.append(stack.pop(0))
            if state:
                state = False
            else:
                state = True
            tmp -= i
            i = 0
        i += 1
    return state


N, L = map(int,input().split())
light = []
for _ in range(N):
    light.append(list(map(int,input().split())))
# print(light)
now = 0 # 현재위치
cnt = 0 # 걸린시간
num = 0 # 신호등 번호
while now < L:

    if num < N:
        tr = light[num][0]  # 가까운 신호등 위치
    if num != N:
        if now < tr:    # 신호등 도착 전
            now += 1
            cnt += 1
            continue
        else:
            state = check(num)
            if state:
                now += 1
                cnt += 1
                num += 1
                continue
            else:
                cnt += 1
                continue
    else:
        now += 1
        cnt += 1

print(cnt-1)