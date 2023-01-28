import sys
input = sys.stdin.readline
a, b = map(str,input().split())
count = 1
while b != a:
    if int(b) < int(a):
        count = -1
        break
    elif b[-1] == '3' or b[-1] == '5' or b[-1] == '7' or b[-1] == '9':
        count = -1
        break
    elif b[-1] == '1':
        b = str(int(b)//10)
        count += 1
    else:
        b = str(int(int(b) / 2))
        count += 1
print(count)