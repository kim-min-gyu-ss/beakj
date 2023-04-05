import heapq
a = int(input())
num_list = []
for i in range(a):
    heapq.heappush(num_list,int(input()))

result = 0
while len(num_list) > 1:
    a = heapq.heappop(num_list)
    b = heapq.heappop(num_list)
    result += a + b
    heapq.heappush(num_list,a+b)

print(result)