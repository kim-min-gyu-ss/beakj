a = int(input())
sum = 0
count = 0
while sum <= a:
    count += 1
    sum += count
count -= 1
print(count)