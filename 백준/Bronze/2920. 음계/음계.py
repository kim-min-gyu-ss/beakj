a = list(map(int,input().split()))
result = ''
for i in range(1,len(a)):
    if a[0] == 8:
        if a[i] < a[i-1]:
            result = 'descending'
        else:
            result = 'mixed'
            break
    elif a[0] == 1:
        if a[i] > a[i-1]:
            result = 'ascending'
        else:
            result = 'mixed'
            break
    else:
        result = 'mixed'
        break
print(result)