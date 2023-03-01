T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int,input().split())
    people = sorted(map(int,input().split()))
    # print(people)
    boong = [0] * 11111
    cnt = 0
    for i in range(1,11111):
        if not i % M:
            cnt += K
        boong[i] = cnt

    hap = 0
    for j in people:
        hap += 1
        if boong[j] < hap:
            print(f'#{tc} Impossible')
            break
    else:
        print(f'#{tc} Possible')