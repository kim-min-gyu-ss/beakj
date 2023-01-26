import sys
input = sys.stdin.readline
a, b = map(int,input().split())
money = []
for i in range(a):
    money.append(int(input()))
money = sorted(money, reverse= True)
count = 0
for i in money:
    if b // i > 0:
        count += b//i
        b = b % i
print(count)