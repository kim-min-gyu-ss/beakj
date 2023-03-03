L = int(input())
cake = [0 for _ in range(L + 1)]
N = int(input())
mx_len = 0
mx_idx = 0
cnt_idx = 0
cnt_mx = 0
for j in range(N):
    a, b = map(int, input().split())
    len = b - a
    if mx_len < len:
        mx_len = len
        mx_idx = j + 1
    cnt = 0
    for i in range(a, b + 1):
        if not cake[i]:
            cake[i] = j + 1
            cnt += 1
    if cnt_mx < cnt:
        cnt_mx = cnt
        cnt_idx = j + 1
print(mx_idx)
print(cnt_idx)