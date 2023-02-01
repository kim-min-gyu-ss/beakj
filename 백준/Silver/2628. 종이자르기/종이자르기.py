a, b = map(int,input().split())
c = int(input())
garo = []
sero = []
for i in range(c):
    d, e = map(int,input().split())
    if d == 1:
        garo.append(e)
    else:
        sero.append(e)


garo.append(a)
garo.insert(0,0)
sero.append(b)
sero.insert(0,0)

garo = sorted(garo)
sero = sorted(sero)

garo_l = []
sero_l = []


if len(garo) == 1:
    garo_l.append(a)
else:
    for j in range(1,len(garo)):
        f = garo[j] - garo[j-1]
        garo_l.append(f)
if len(sero) == 1:
    sero_l.append(b)
else:
    for k in range(1,len(sero)):
        g = sero[k] - sero[k-1]
        sero_l.append(g)

print(max(garo_l) * max(sero_l))