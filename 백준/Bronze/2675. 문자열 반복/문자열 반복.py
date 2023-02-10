a = int(input())
for _ in range(a):
    num, lst = input().split()
    for j in lst:
        for i in range(int(num)):
            print(j, end='')
    print()