import sys
import heapq
input = sys.stdin.readline

numbers = int(input())
h = []
for _ in range(numbers):
    n = int(input())
    if n != 0:
        heapq.heappush(h, (abs(n),n))
    else:
        try:
            print(heapq.heappop(h)[1])
        except:
            print(0)