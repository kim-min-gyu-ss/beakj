bingo = []
for i in range(5):
    bingo.append(list(map(int,input().split())))
test = []
for j in range(5):
    test += list(map(int,input().split()))
garo = [0, 0, 0, 0, 0]
sero = [0, 0, 0, 0, 0]
cross = [0,0]
count = 0
result = 0
rest = []
for k in test:
    for l in range(5):
        for q in range(5):
            if bingo[l][q] == k:
                garo[l] += 1
                sero[q] += 1
                if (l == 0 and q == 4) or (l == 1 and q == 3) or (l == 3 and q == 1) or (l == 4 and q == 0):
                    cross[1] += 1
                if l == q:
                    cross[0] += 1
                    if l == 2:
                        cross[1] += 1
                result += 1
                rest.append(k)
                break
        if k in rest:
            break
    count = 0
    for m in range(5):
        if garo[m] == 5:
            count += 1
        if sero[m] == 5:
            count += 1
    for n in range(2):
        if cross[n] == 5:
            count += 1

    if count >= 3:
        print(result)
        break