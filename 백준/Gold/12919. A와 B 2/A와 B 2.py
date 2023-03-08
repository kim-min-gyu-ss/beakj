def find(a,b):
    global result
    if len(a) == len(b):
        if a == b:
            result += 1
            return
        else:
            return
    if b[0] == 'B':
        d = b[::-1]
        d.pop()
        find(a,d)

    if b[-1] == 'A':
        w = b.pop()
        find(a,b)
        # b.append()


a = list(input())
b = list(map(str,input()))
result = 0
find(a,b)

if result:
    print(1)
else:
    print(0)