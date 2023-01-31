result = [[0 for i in range(100)] for j in range(100)]
for i in range(4):
    x_1, y_1, x_2, y_2 = map(int,input().split())
    for j in range(x_1, x_2):
        for k in range(y_1, y_2):
            result[k][j] = 1

count = 0
for i in range(100):
    for j in range(100):
        if result[i][j] == 1:
            count += 1
print(count)