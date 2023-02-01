a = input()
b = input()
count = 0
while b in a:
    if b in a:
        a = a.replace(b,' ',1)
        count += 1
print(count)
