a = int(input())
b = list(map(int,input().split()))
c = int(input())
d = list(map(int,input().split()))
e = len(b)-1
b = sorted(b)
result = []
count = 0
for i in d:
    count = 0
    start = 0
    end = e
    while start <= end:
        mid = (start + end) // 2
        if i == b[mid]:
            count += 1
            break
        elif i > b[mid]:
            start = mid + 1
        else:
            end = mid - 1
    if count == 1:
        result.append(1)
    else:
        result.append(0)
for i in result:
    print(i)