c, r = map(int,input().split())
k = int(input())
a = c
b = r
x = 1
y = 1
x_2 = 2
y_2 = 1
count = 1
state = '1000'
final = True
while count < k:
    if count > a * b:
        final = False
        break

    if state == '1000':
        y += 1
        count += 1
        if y == r:
            state = '0100'
            r -= 1
    elif state == '0100':
        x += 1
        count += 1
        if x == c:
            state = '0010'
            c -= 1
    elif state == '0010':
        y -= 1
        count += 1
        if y == y_2:
            state = '0001'
            y_2 += 1
    elif state == '0001':
        x -= 1
        count += 1
        if x == x_2:
            state = '1000'
            x_2 += 1
if final == True:
    print(x, y)
else:
    print(0)