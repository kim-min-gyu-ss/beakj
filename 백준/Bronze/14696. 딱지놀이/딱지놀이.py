a = int(input())
for i in range(a):
    player_a = list(map(int,input().split()))
    player_b = list(map(int,input().split()))
    result_1 = []
    result_2 = []
    for i in range(4,0,-1):
        result_1.append(player_a.count(i))
        result_2.append(player_b.count(i))
        count = 0
    for i in range(4):
        if result_1[i] > result_2[i]:
            print('A')
            break
        elif result_1[i] < result_2[i]:
            print('B')
            break
        else:
            count += 1
            if count == 4:
                print('D')