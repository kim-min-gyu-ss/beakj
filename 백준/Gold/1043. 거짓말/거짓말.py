N, M = map(int,input().split())
K, *f = list(map(str,input().split()))
tr_man = set(f)
people = []
result = M
for _ in range(M):
    q ,*person = list(map(str,input().split()))
    people.append(person)
for _ in range(M):
    for k in people:
        for l in range(len(k)):
            if k[l] in tr_man:
                tr_man = tr_man.union(k)
# print(tr_man)
for i in people:
    for j in range(len(i)):
        if i[j] in tr_man:
            result -= 1
            break
print(result)