N = int(input())
N_list = sorted(list(map(int,input().split())))
M = int(input())
M_list = list(map(int,input().split()))


for i in M_list:
    start = 0
    end = len(N_list) - 1
    bb = True
    while start <= end:
        mid = (start + end) // 2
        if N_list[mid] == i:
            print(1, end = ' ')
            bb = False
            break
        if N_list[mid] < i:
            start = mid + 1
        elif N_list[mid] > i:
            end = mid - 1
    if bb == True:
        print(0, end = ' ')
