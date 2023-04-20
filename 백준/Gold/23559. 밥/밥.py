import heapq
N, X = map(int,input().split())
money = []
for i in range(N):
    oh, chun = map(int,input().split())
    heapq.heappush(money,[-(abs(oh - chun)),-oh,-chun])
result = 0
for j in range(N):
    cha, oh, chun = heapq.heappop(money)
    oh, chun = -oh, -chun
    if oh > chun and X - 5000 >= 1000 * (N - j - 1):
        # print(X - 5000, 1000 * (N - j - 1))
        X -= 5000
        result += oh
    else:
        X -= 1000
        result += chun
print(result)