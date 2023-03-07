N = int(input())
meeting = [list(map(int,input().split())) for _ in range(N)]
meeting = sorted(meeting, key= lambda x : (x[1],x[0]))
# print(meeting)
first = 0
cnt = 0
for i in meeting:
    if first <= i[0]:
        first = i[1]
        cnt += 1
print(cnt)