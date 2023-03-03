N = int(input())
a = 1
result = 0
while a * a <= N:
    cnt = a**2
    result += 1
    while cnt <N:
        cnt += a
        if cnt > N:
            break
        result += 1
    a += 1
if N == 1:
    print(1)
else:
    print(result)