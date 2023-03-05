T = int(input())
for _ in range(T):
    tc, *tall = map(int,input().split())
    cnt = 0
    result = []
    for i in range(len(tall)):
        result.append(tall[i])
        if i:
            for j in range(len(result)-1,0,-1):
                if result[j] < result[j-1]:
                    result[j],result[j-1] = result[j-1],result[j]
                    cnt += 1
    print(tc,end=' ')
    print(cnt)