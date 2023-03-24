N, K = map(int,input().split())
tall = list(map(int,input().split()))
dif = []
for i in range(1,N):
    dif.append(tall[i] - tall[i-1])
dif = sorted(dif)
result = 0
for i in range(len(dif)):
    if i >= N - K:
        continue
    else:
        result += dif[i]
print(result)