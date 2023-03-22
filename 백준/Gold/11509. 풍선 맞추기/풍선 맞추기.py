import sys
input = sys.stdin.readline

N = int(input())
pung = list(map(int,input().split()))
arrow = [0 for _ in range(1000001)]
for i in pung:
    if not arrow[i]:
        arrow[i-1] += 1
    else:
        arrow[i] -= 1
        arrow[i-1] += 1
print(sum(arrow))