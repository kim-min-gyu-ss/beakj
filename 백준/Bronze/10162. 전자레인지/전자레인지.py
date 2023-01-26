a = int(input())
count1 = 0
count2 = 0
count3 = 0
check = 0
while a > 0:
    if a % 10 < 10 and a % 10 > 0:
        check += 1
        break
    elif a // 300 > 0:
        count1 += a // 300
        a = a % 300
    elif a // 60 > 0:
        count2 += a // 60
        a = a % 60
    elif a // 10 > 0:
        count3 += a // 10
        a = 0
if check == 1:
    print(-1)
else:
    print(count1, count2, count3)