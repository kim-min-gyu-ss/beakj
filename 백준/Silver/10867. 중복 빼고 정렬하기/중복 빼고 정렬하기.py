a = int(input())
num_list = set(map(int,input().split()))
num_list = sorted(num_list)
for i in num_list:
    print(i, end = ' ')