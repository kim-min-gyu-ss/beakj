a = int(input())
for _ in range(a):
    result = []
    str_list = input()
    count = 0
    for i in str_list:
        if i == 'O':
            count += 1
            result.append(count)
        elif i == 'X':
            count = 0
    print(sum(result))