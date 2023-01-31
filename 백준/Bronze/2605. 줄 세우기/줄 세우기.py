a = int(input())
num = list(map(int,input().split()))
final = []
count = 1
for i in num:
    final.insert(i,count)
    count += 1
final = final[::-1]
for i in final:
    print(i, end = ' ')