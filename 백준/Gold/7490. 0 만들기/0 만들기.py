import copy

def back(tmp, cnt):
    if cnt == N - 1:
        lst.append(copy.deepcopy(tmp))
        return

    tmp.append(' ')
    back(tmp, cnt + 1)
    tmp.pop()

    tmp.append('+')
    back(tmp, cnt + 1)
    tmp.pop()

    tmp.append('-')
    back(tmp, cnt + 1)
    tmp.pop()


T = int(input())
for _ in range(T):
    lst = []
    N = int(input())
    back([], 0)

    for l in lst:
        result = ''
        for i in range(N - 1):
            result += str(i + 1) + l[i]
        result += str(N)
        if (eval(result.replace(' ', ''))) == 0:
            print(result)
    print()