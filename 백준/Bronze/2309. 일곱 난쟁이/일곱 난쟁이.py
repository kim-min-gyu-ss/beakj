nanjangs = []
pung = False
for i in range(9):
    nanjangs.append(int(input()))
tall_sum = sum(nanjangs) - 100
for j in range(len(nanjangs)-1):
    if pung == True:
        break
    for k in range(j+1,len(nanjangs)):
        if (nanjangs[j] + nanjangs[k]) == tall_sum:
            nanjangs[j] = 0
            nanjangs[k] = 0
            pung = True
            break
nanjangs = sorted(nanjangs)
for l in nanjangs:
    if l != 0:
        print(l)