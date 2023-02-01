a = int(input())
bulb = list(map(int,input().split()))
b = int(input())

for i in range(b):
    c, d = map(int,input().split())
    if c == 1:
        count = d
        if d == 1:
            for k in range(len(bulb)):
                if bulb[k] == 0:
                    bulb[k] = 1
                    continue
                else:
                    bulb[k] = 0
                    continue
        else:
            while count <= a:
                if bulb[count-1] == 0:
                    bulb[count-1] = 1
                    count += d
                else:
                    bulb[count-1] = 0
                    count += d
    elif c == 2:
        count = d - 1
        i = 1
        if count == 0 or count == len(bulb) - 1:
            if bulb[count] == 0:
                bulb[count] = 1
                continue
            else:
                bulb[count] = 0
                continue
        else:
            if bulb[count] == 0:
                bulb[count] = 1
            else:
                bulb[count] = 0
        while True:
            if bulb[count - i] == bulb[count + i]:
                if bulb[count - i] == 0:
                    bulb[count - i] = 1
                    bulb[count + i] = 1
                    if count - i == 0 or count + i == len(bulb) - 1:
                        break
                    else:
                        i += 1
                else:
                    bulb[count - i] = 0
                    bulb[count + i] = 0
                    if count - i == 0 or count + i == len(bulb) - 1:
                        break
                    else:
                        i += 1
            else:
                break

for j in range(1,a+1):
    print(bulb[j-1], end = ' ')
    if j % 20 == 0:
        print()