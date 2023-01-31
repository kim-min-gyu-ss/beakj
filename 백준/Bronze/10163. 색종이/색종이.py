import sys
input = sys.stdin.readline
result = [[0 for i in range(1001)] for j in range(1001)]
a = int(input())
for i in range(1, a + 1):
    x_1, y_1, x_2, y_2 = map(int,input().split())
    for j in range(x_1, x_1 + x_2):
        for k in range(y_1, y_1 + y_2):
            result[k][j] = i
for l in range(1,a + 1):
    count = 0
    for m in range(1001):
        for n in range(1001):
            if result[m][n] == l:
                count += 1
    print(count)