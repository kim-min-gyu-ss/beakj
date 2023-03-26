N = int(input())
card = list(map(int, input().split()))
result = 0
final = 0
for i in range(N):
    if not i % 2:
        result += card[i]
tmp1 = result
tmp2 = result

for i in range(N - 1, 0, -2):
    tmp1 += card[i]
    tmp1 -= card[i - 1]
    final = max(tmp1, final)

for i in range(N - 2, -1, -2):
    tmp2 -= card[i]
    tmp2 += card[i - 1]
    final = max(tmp2, final)

final = max(result, final)
print(final)