a = int(input())
stck = []
for i in range(a):
    b = int(input())
    if b == 0:
        stck.pop()
    else:
        stck.append(b)
print(sum(stck))