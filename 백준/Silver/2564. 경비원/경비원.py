garo, sero = map(int,input().split())
b = int(input())
store = []   # 1 = 위 2 = 밑 왼쪽부터 거리,  3 = 왼 4 = 오 위부터 거리
for i in range(b):
    store.append(list(map(int,input().split())))
dong = list(map(int,input().split()))
count = 0
for j in store:
    if j[0] == 1:
        if dong[0] == 1:
            count += abs(j[1] - dong[1])
        elif dong[0] == 2:
            count += min(sero + dong[1] + j[1], sero + 2 * garo - dong[1] - j[1])
        elif dong[0] == 3:
            count += j[1] + dong[1]
        elif dong[0] == 4:
            count += garo - j[1] + dong[1]
    elif j[0] == 2:
        if dong[0] == 1:
            count += min(sero + dong[1] + j[1], sero + 2 * garo - dong[1] - j[1])
        elif dong[0] == 2:
            count += abs(j[1] - dong[1])
        elif dong[0] == 3:
            count += sero + j[1] - dong[1]
        elif dong[0] == 4:
            count += garo + sero - j[1] - dong[1]
    elif j[0] == 3:
        if dong[0] == 1:
            count += j[1] + dong[1]
        elif dong[0] == 2:
            count += sero - j[1] + dong[1]
        elif dong[0] == 3:
            count += abs(j[1] - dong[1])
        elif dong[0] == 4:
            count += min(garo + dong[1] + j[1], garo + 2 * sero - dong[1] - j[1])
    elif j[0] == 4:
        if dong[0] == 1:
            count += garo + j[1] - dong[1]
        elif dong[0] == 2:
            count += garo + sero - j[1] - dong[1]
        elif dong[0] == 3:
            count += min(garo + dong[1] + j[1], garo + 2 * sero - dong[1] - j[1])
        elif dong[0] == 4:
            count += abs(j[1] - dong[1])
print(count)