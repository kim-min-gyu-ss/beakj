i = 1
while True:
    a ,b ,c = map(int,input().split())
    if a == 0:
        break
    else:
        day_1 = c // b
        day_2 = c % b
        if day_2 > a:
            day_2 = a
        result = day_1 * a + day_2
        print(f'Case {i}: {result}')
        i += 1