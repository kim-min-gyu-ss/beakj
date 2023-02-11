a, b = map(str,input().split())
c = int(a[::-1])
d = int(b[::-1])
if c > d:
    print(c)
elif c < d:
    print(d)