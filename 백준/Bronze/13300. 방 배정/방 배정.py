a, room = map(int,input().split())
people = dict()
for i in range(a):
    x, y = map(int,input().split())
    people.setdefault((x,y),0)
    people[(x,y)] += 1
count = 0
for j in people.values():
    if j // room != 0:
        count += j//room
        if j % room != 0:
            count += 1
    else:
        if j % room != 0:
            count += 1
print(count)
    