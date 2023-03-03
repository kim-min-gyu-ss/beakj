H, W = map(int, input().split())
rain = list(map(int, input().split()))
result = 0

for i in range(1, W - 1):
    mx_front = 0
    mx_back = 0
    for j in range(0,i):
        if mx_front < rain[j]:
            mx_front = rain[j]
    for k in range(i+1,W):
        if mx_back < rain[k]:
            mx_back = rain[k]
    mx = min(mx_front,mx_back)
    if rain[i] < mx:
        result += mx - rain[i]
print(result)