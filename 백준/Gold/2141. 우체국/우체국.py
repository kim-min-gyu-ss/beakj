N = int(input())
hap = 0
town = []
for _ in range(N):
    post, people = map(int,input().split())
    hap += people
    town.append([post,people])
town = sorted(town, key=lambda x : x[0])
cnt = 0
result = 0
for i in town:
    cnt += i[1]
    if cnt >= hap/2:
        result = i[0]
        break
print(result)