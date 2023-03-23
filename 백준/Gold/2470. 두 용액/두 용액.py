N = int(input())
water = sorted(map(int,input().split()))
start = 0
end = N - 1
result = abs(water[start] + water[end])
idx = [water[start],water[end]]
while start < end:
    s = water[start] + water[end]
    if abs(s) < result:
        result = abs(s)
        idx = [water[start], water[end]]
    if s < 0:
        start += 1
    else:
        end -= 1
print(*idx)