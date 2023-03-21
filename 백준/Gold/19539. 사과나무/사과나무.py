N = int(input())
apple = list(map(int,input().split()))
sum = 0
one = 0
two = 0
for i in apple:
    sum += i
    if i == 1:
        one += 1
    elif i >= 2 :
        two += i // 2

if sum % 3 or two < sum // 3:
    print('NO')
else:
    print('YES')