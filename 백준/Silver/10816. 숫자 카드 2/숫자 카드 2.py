# 씨잇팔
import sys
input = sys.stdin.readline
N = int(input())
N_list = sorted(list(map(int,input().split())))
M = int(input())
M_list = list(map(int,input().split()))

result = dict()
for j in N_list:
    result.setdefault(j,0)
    result[j] += 1
# print(result)
for i in M_list:
    start = 0
    end = len(N_list) - 1
    bb = True
    while start <= end:
        mid = (start + end) // 2
        if N_list[mid] == i:
            print(result[i], end = ' ')
            bb = False
            break
        if N_list[mid] < i:
            start = mid + 1
        elif N_list[mid] > i:
            end = mid - 1
    if bb == True:
        print(0, end = ' ')
