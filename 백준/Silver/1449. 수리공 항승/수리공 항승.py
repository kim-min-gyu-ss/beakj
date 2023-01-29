a, b = map(int,input().split())
hole = list(map(int,input().split()))
hole = sorted(hole)
point = 0
count = 1
if b == 1:
    count = len(hole)
else:
    for i in range(1,len(hole)):
        point += hole[i] - hole[i-1]
        if point >= b:
            point = 0
            count += 1
print(count)