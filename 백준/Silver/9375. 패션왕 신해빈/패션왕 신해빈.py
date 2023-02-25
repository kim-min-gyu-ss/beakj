T = int(input())
for _ in range(T):
    N = int(input())
    result = dict()
    for _ in range(N):
        name, tp = map(str, input().split())
        result.setdefault(tp, 0)
        result[tp] += 1
    final = 1
    # print(result)
    for i in result.values():
        final = final * (i + 1)
    print(final - 1)